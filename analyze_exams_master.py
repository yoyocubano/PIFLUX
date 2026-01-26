import os
import sys
import glob
import time
import google.generativeai as genai
from pypdf import PdfReader
import re

# --- 1. CONFIGURATION ---
# SECURITY FIX: Paths moved to environment variables
SOURCE_LIBRARY = os.getenv("PIFLUX_SOURCE_LIBRARY", "./library/PIF_MASTER_LIBRARY")
OUTPUT_DIR = os.getenv("PIFLUX_OUTPUT_RESULTS", "./results/PIF_ANALYSIS_RESULTS")

# API Key
# SECURITY FIX: Loaded from environment variable
from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.getenv("PIFLUX_GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("❌ ERROR: PIFLUX_GEMINI_API_KEY not found in environment variables.")
    print("   Please create a .env file with this key.")
    sys.exit(1)

# Using Flash for speed and high context window
MODEL_NAME = "gemini-2.0-flash"

# --- 2. AI CONNECTION ---
def get_ai_response(prompt):
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"❌ Error communicating with AI: {e}")
        time.sleep(10) # Wait a bit on error
        return None

# --- 3. PDF PROCESSING ---
def extract_text_from_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            t = page.extract_text()
            if t: text += t + "\n"
        return text
    except:
        return ""

# --- 4. BATCH PROCESSING ---
def process_batch(batch_files):
    """
    Analyzes a list of files in ONE single API call.
    """
    print(f"📦 Preparing Batch of {len(batch_files)} exams...")
    
    combined_prompt = """
    You are an expert tutor for the Luxembourg Professional Education system.
    
    TASK: Analyze multiple exams in bulk.
    
    OUTPUT INSTRUCTIONS:
    For EACH exam provided below, you must generate a separate analysis block.
    Start each analysis with the exact line: "### FILE_START: <filename>"
    End each analysis with the exact line: "### FILE_END: <filename>"
    
    Inside each block, follow this structure (in the language of the exam, FR or DE):
    1. **Question**: The extracted question.
    2. **Correct Answer**: Technical answer.
    3. **Justification**: Technical reasoning.
    4. **Analogy (Child-Friendly)**: Simple explanation.
    5. **Use Case**: Real job example.
    
    Here are the exams content:
    """
    
    file_map = {} # Store file paths by filename
    
    for fpath in batch_files:
        fname = os.path.basename(fpath)
        text = extract_text_from_pdf(fpath)
        if len(text) > 50:
            combined_prompt += f"\n\n--- START OF FILE: {fname} ---\n{text[:15000]}\n--- END OF FILE: {fname} ---\n"
            file_map[fname] = fpath
        else:
            print(f"⚠️ Skipping empty file: {fname}")

    # Call AI
    print(f"🚀 Sending Batch to AI ({len(batch_files)} files)...")
    response_text = get_ai_response(combined_prompt)
    
    if not response_text:
        print("❌ Batch failed (API Error).")
        return

    # Parse and Save Split Responses
    print("💾 Saving individual results...")
    
    # We look for "### FILE_START: filename" blocks
    # Fallback: If AI messes up format, we save everything to a "BATCH_DUMP" file.
    
    pattern = re.compile(r"### FILE_START: (.*?)\n(.*?)### FILE_END: \1", re.DOTALL)
    matches = pattern.findall(response_text)
    
    saved_count = 0
    if matches:
        for filename, content in matches:
            filename = filename.strip()
            out_name = filename.replace(".pdf", "_ANALYSIS.md")
            out_path = os.path.join(OUTPUT_DIR, out_name)
            
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(f"# 📝 Analysis: {filename}\n**Date:** {time.strftime('%Y-%m-%d')}\n\n{content}")
            saved_count += 1
            print(f"   ✅ Saved: {out_name}")
    else:
        # Fallback save if regex fails
        dump_name = f"BATCH_Rescue_{int(time.time())}.md"
        with open(os.path.join(OUTPUT_DIR, dump_name), "w", encoding="utf-8") as f:
            f.write(response_text)
        print(f"⚠️ Format warning. Saved full batch to {dump_name}")

    print(f"✨ Batch complete. {saved_count}/{len(batch_files)} processed.")


# --- 5. ORCHESTRATOR ---
def main():
    print("🚀 STARTING TURBO-BATCH EXAM ANALYSIS (Gemini 1.5 Flash)")
    
    # Scan for exams
    all_files = glob.glob(os.path.join(SOURCE_LIBRARY, "**/*.pdf"), recursive=True)
    exam_files = [f for f in all_files if "PIF" in f.upper() or "QUESTIONNAIRE" in f.upper() or "EXAMEN" in f.upper()]
    
    # Filter out already done
    todo_files = []
    for f in exam_files:
        out_name = os.path.basename(f).replace(".pdf", "_ANALYSIS.md")
        if not os.path.exists(os.path.join(OUTPUT_DIR, out_name)):
            todo_files.append(f)
            
    print(f"📋 Found {len(exam_files)} exams. {len(todo_files)} pending.")
    
    # Batch Size (Gemini 1.5 has 1M context, we can fit ~10-15 exams easily)
    BATCH_SIZE = 10
    
    for i in range(0, len(todo_files), BATCH_SIZE):
        batch = todo_files[i:i+BATCH_SIZE]
        process_batch(batch)
        print("⏳ Cooldown 5s...")
        time.sleep(5) # Minimal sleep between batches

if __name__ == "__main__":
    main()
