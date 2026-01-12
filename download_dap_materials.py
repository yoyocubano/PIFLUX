import os
import urllib.request

# Mapa de archivos a descargar
download_map = {
    "de": [
        ("Carnet_Apprentissage_2025_DE.pdf", "https://ssl.education.lu/eSchoolBooks/Web/FP/20/Documents/RedirectToDownload/5892966"),
        ("Grille_Evaluation_2025_DE.pdf", "https://ssl.education.lu/eSchoolBooks/Web/FP/20/Documents/RedirectToDownload/5858462"),
        ("Planning_Competences_2025_DE.pdf", "https://ssl.education.lu/eSchoolBooks/Web/FP/20/Documents/RedirectToDownload/5858780"),
        ("PIF_Final_Questionnaire_2024_DE.pdf", "https://ssl.education.lu/eSchoolBooks/Web/FP/19/Documents/RedirectToDownload/5895825"),
        ("PIF_Intermediaire_Questionnaire_2024_DE.pdf", "https://ssl.education.lu/eSchoolBooks/Web/FP/19/Documents/RedirectToDownload/5895903"),
        ("Programme_Directeur_2024_DE.pdf", "https://ssl.education.lu/eSchoolBooks/Web/FP/19/Documents/RedirectToDownload/5896215")
    ],
    "fr": [
        ("Carnet_Apprentissage_2025_FR.pdf", "https://ssl.education.lu/eSchoolBooks/Web/FP/20/Documents/RedirectToDownload/5892968"),
        ("Grille_Evaluation_2025_FR.pdf", "https://ssl.education.lu/eSchoolBooks/Web/FP/20/Documents/RedirectToDownload/5858463"),
        ("Planning_Competences_2025_FR.pdf", "https://ssl.education.lu/eSchoolBooks/Web/FP/20/Documents/RedirectToDownload/5858781"),
        ("Programme_Directeur_2024_FR.pdf", "https://ssl.education.lu/eSchoolBooks/Web/FP/19/Documents/RedirectToDownload/5896216")
    ]
}

def download_files():
    print("🚀 Iniciando descarga masiva de materiales DAP Electricien (vía Urllib)...")
    for lang, files in download_map.items():
        base_dir = f"assets/{lang}/pdfs"
        os.makedirs(base_dir, exist_ok=True)
        
        for filename, url in files:
            target_path = os.path.join(base_dir, filename)
            print(f"📦 Descargando [{lang.upper()}]: {filename}...")
            try:
                # User-Agent para evitar bloqueos básicos
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=30) as response:
                    if response.status == 200:
                        with open(target_path, 'wb') as f:
                            f.write(response.read())
                        print(f"✅ Guardado: {target_path}")
                    else:
                        print(f"❌ Error {response.status} en URL: {url}")
            except Exception as e:
                print(f"❌ Fallo crítico en {filename}: {str(e)}")

if __name__ == "__main__":
    download_files()
    print("\n✨ Proceso de extracción finalizado.")
