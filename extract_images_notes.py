import subprocess
import os

# Destination on Desktop
DEST_DIR = "/Users/yoyocubano/Desktop/Imagenes_Notas_Exportadas"

def run_applescript(script):
    try:
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"Error: {e}")
        return ""

def extract_images():
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)
        
    print(f"🚀 Iniciando extracción de imágenes a: {DEST_DIR}")
    
    # AppleScript to iterate through selected notes and save attachments
    # We will target the same notes we found earlier or ALL notes if requested.
    # User said "todas las imagenes de mis notas" (all images from my notes).
    # This might be huge. Let's try to target the "Seleccion_PIF" notes first or just iterate all.
    # Given the user context "mis notas", I'll check *all* generally, but maybe limit to the PIF ones to avoid 1000s of unrelated icons.
    # Let's iterate the 'Notes' folder which usually has the main stuff, or just 'Seleccion_PIF' logic.
    # User said "extraction todas las images de mis notas". I will try to be broad but safe.
    
    script = f'''
    set exportPath to (POSIX file "{DEST_DIR}") as string
    
    tell application "Notes"
        repeat with aNote in notes
            if (count of attachments of aNote) > 0 then
                set noteName to name of aNote
                set safeName to do shell script "echo " & quoted form of noteName & " | sed 's/[^a-zA-Z0-9]/_/g'"
                
                repeat with anAtt in attachments of aNote
                    try
                        set attName to name of anAtt
                        if attName is missing value then set attName to "image"
                        
                        -- Generate filename: NoteName_AttachmentName
                        set fName to safeName & "_" & attName
                        set fullPath to exportPath & fName
                        
                        save anAtt in file fullPath
                    on error errMsg
                        -- Ignore errors for non-saveable attachments
                    end try
                end repeat
            end if
        end repeat
    end tell
    '''
    
    print("⏳ Ejecutando AppleScript (esto puede tardar)...")
    out = run_applescript(script)
    print("✅ Proceso finalizado. Verifica la carpeta en tu escritorio.")

if __name__ == "__main__":
    extract_images()
