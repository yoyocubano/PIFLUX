import os
import glob

TARGET_DIR = "/Users/yoyocubano/Desktop/École - trabajo /PIF_Documentation/assets/extracted_notes"

# Keywords that suggest the image IS related to electricity/technical study (keep these)
KEEP_KEYWORDS = [
    "motor", "moteur", 
    "triangle", "delta",
    "logique", "logic",
    "resistance", "r_sistance", "resistencia",
    "courant", "current",
    "tension", "voltage",
    "calcule", "calcul", "calcula",
    "condensateur", "capacitor", "condenser",
    "capacitancia",
    "resistividad",
    "montage",
    "examen",
    "entretien",
    "f_rmula", "formula",
    "pasted_graphic", "graphic",
    "outillage", "tool",
    "circuit",
    "bloque",
    "continu",
    "electr", "lectrique",
    "frecuencia", "frequency",
    "relevador", "relais", "relay", "t_rmico", "termico",
    "plano", "shema", "schema",
    "fusible", "fuse",
    "malla", "tierra", "ground", "terre",
    "automatiza", "industrial",
    "curva", "mcb", "disjoncteur",
    "tgbt", "tablero", "panel",
    "luxometro", "interruptor", "breaker",
    "mantenimiento", "maintenance",
    "significado", "funciona"
]

# Keywords that are definitely NOT related (delete these)
DELETE_KEYWORDS = [
    "cinema", "cine",
    "usdt", "crypto",
    "lesson", "language",
    "certificat", "scolarit",
    "history", "histoire",
    "claro",
    "recette", "cooking"
]

def cleanup():
    if not os.path.exists(TARGET_DIR):
        print("Target directory not found.")
        return

    files = os.listdir(TARGET_DIR)
    deleted_count = 0
    kept_count = 0

    print(f"Scanning {len(files)} files...")

    for filename in files:
        filepath = os.path.join(TARGET_DIR, filename)
        if not os.path.isfile(filepath):
            continue

        lower_name = filename.lower()
        
        # Logic: 
        # 1. If explicit DELETE keyword -> Delete
        # 2. Else, if matches KEEP keyword -> Keep
        # 3. Else (unknown) -> Delete (User said "remove anything that is not electricity")
        
        should_delete = False
        
        # Check explicit delete
        if any(bad in lower_name for bad in DELETE_KEYWORDS):
            should_delete = True
        
        # Check explicit keep
        elif any(good in lower_name for good in KEEP_KEYWORDS):
            should_delete = False
        else:
            # If it doesn't match a known technical term, assume it's garbage/unrelated
            should_delete = True

        if should_delete:
            print(f"Deleting: {filename}")
            try:
                os.remove(filepath)
                deleted_count += 1
            except Exception as e:
                print(f"Error deleting {filename}: {e}")
        else:
            kept_count += 1

    print(f"\nCleanup complete.")
    print(f"Deleted: {deleted_count}")
    print(f"Kept: {kept_count}")

if __name__ == "__main__":
    cleanup()
