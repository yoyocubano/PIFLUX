import subprocess
import os
import re

# List of specific note titles to export (Fuzzy match)
TARGET_TITLES = [
    "Preparation d’outillage", 
    "Montage coge triangle", 
    "Moteur triphasé",
    "CIRCUITES LOGIQUES",
    "Resistance du conducteur", 
    "Calcule du période",
    "Calcula capacitancia",
    "Calcula resistividad",
    "montage practique",
    "motore",
    "pasted graphic",
    "examen entretien",
    "Simulacro",
    "PIF"
]

OUTPUT_ROOT = "/Users/yoyocubano/Desktop/École - trabajo /PIF_Documentation/Notas_Mac"

def run_applescript(script):
    try:
        # Increase timeout or handle errors
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"Error running AppleScript: {e}")
        return ""

def clean_filename(title):
    keep = (' ','.','_','-')
    cleaned = "".join(c for c in title if c.isalnum() or c in keep).strip()
    return cleaned if cleaned else "Untitled"

def export_notes():
    if not os.path.exists(OUTPUT_ROOT):
        os.makedirs(OUTPUT_ROOT)
    
    # We create a single folder for these selected notes to keep it clean
    dest_dir = os.path.join(OUTPUT_ROOT, "Seleccion_PIF")
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        
    print("📢 Conectando con Apple Notes globalmente...")
    
    # Get total count
    count_str = run_applescript('tell application "Notes" to get count of notes')
    try:
        total = int(count_str)
    except:
        print("❌ Error counting notes")
        return

    print(f"🔍 Escaneando {total} notas en busca de {len(TARGET_TITLES)} objetivos...")
    
    found_count = 0
    
    # Process in batches or one by one. One by one is fine for 169 notes.
    for i in range(1, total + 1):
        name = run_applescript(f'tell application "Notes" to get name of note {i}')
        if not name: continue
        
        # Check match
        is_match = False
        for tgt in TARGET_TITLES:
            if tgt.lower() in name.lower():
                is_match = True
                break
        
        if is_match:
            print(f"  ✅ Encontrada: {name}")
            body = run_applescript(f'tell application "Notes" to get body of note {i}')
            
            # Save
            fname = clean_filename(name) + ".html"
            fpath = os.path.join(dest_dir, fname)
            
            with open(fpath, "w", encoding="utf-8") as f:
                 header = f"""
                <!DOCTYPE html>
                <html>
                <head><meta charset="utf-8"><title>{name}</title>
                <style>
                    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; padding: 40px; max-width: 800px; margin: 0 auto; line-height: 1.6; color: #333; background: #f9fafb; }}
                    img {{ max-width: 100%; height: auto; border-radius: 8px; margin: 20px 0; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
                    h1 {{ color: #111; border-bottom: 2px solid #e5e7eb; padding-bottom: 10px; }}
                </style>
                </head>
                <body>
                <h1>{name}</h1>
                {body}
                </body></html>
                """
                 f.write(header)
            
            found_count += 1
            
    print(f"🎉 Exportación finalizada. {found_count} notas guardadas en {dest_dir}")

if __name__ == "__main__":
    export_notes()
