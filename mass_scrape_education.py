import os
import json
import urllib.request
import urllib.parse
from urllib.error import HTTPError, URLError
import time
import ssl

# Configuración
BASE_URL = "https://ssl.education.lu/eSchoolBooks/Web/FP"
CURRENT_YEAR_ID = 20  # 2025/2026
TARGET_ROOT = os.getenv("PIFLUX_TARGET_ROOT", "./downloads/PROYECTO_EDUCATIVO_LUXEMBURGO_2026")

# SECURE SSL Context (Enforced)
ctx = ssl.create_default_context()
# SECURITY FIX: Enforced strict SSL verification
ctx.check_hostname = True
ctx.verify_mode = ssl.CERT_REQUIRED

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest'
}

def clean_name(name):
    """Limpia nombres para que sean seguros como carpetas"""
    return "".join([c if c.isalnum() or c in (' ', '-', '_') else '_' for c in name]).strip()

def fetch_json(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=30) as response:
            if response.status == 200:
                return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"⚠️ Error al acceder a {url}: {e}")
    return None

def download_file(url, filepath):
    if os.path.exists(filepath):
        print(f"  ⏭️ Ya existe: {filepath}")
        return
    
    try:
        print(f"  ⬇️ Descargando: {os.path.basename(filepath)}...")
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=60) as response:
            with open(filepath, 'wb') as f:
                f.write(response.read())
        print(f"  ✅ Guardado.")
    except Exception as e:
        print(f"  ❌ Fallo descarga: {e}")

def process_formation(formation_node, path):
    formation_id = formation_node.get('li_attr', {}).get('data-id')
    formation_name = clean_name(formation_node.get('text', 'Unknown'))
    
    if not formation_id:
        return

    formation_path = os.path.join(path, formation_name)
    os.makedirs(formation_path, exist_ok=True)
    # print(f"📂 Procesando Formación: {formation_name} (ID: {formation_id})")

    # Obtener documentos
    docs_url = f"{BASE_URL}/{CURRENT_YEAR_ID}/Documents/List/?formationId={formation_id}"
    docs = fetch_json(docs_url)

    if docs:
        for doc in docs:
            doc_id = doc.get('Id')
            doc_name = clean_name(doc.get('Title', f"doc_{doc_id}")) + ".pdf" # Asumimos PDF 
            # Si el documento tiene metadata de lenguaje, agregarlo al nombre
            lang = doc.get('Language', '').upper()
            if lang:
                doc_name = f"[{lang}] {doc_name}"
            
            download_url = f"{BASE_URL}/{CURRENT_YEAR_ID}/Documents/RedirectToDownload/{doc_id}"
            file_path = os.path.join(formation_path, doc_name)
            
            download_file(download_url, file_path)

def traverse_tree(nodes, current_path):
    for node in nodes:
        node_text = clean_name(node.get('text', 'Unnamed'))
        node_type = node.get('type', 'default')
        
        # Si es una hoja (formación) o una rama (categoría)
        # La estructura suele ser: Metier -> Formation
        
        # Check if it's a formation (usually has data-role='formation' or specific type)
        # Based on previous recon, formation nodes have data-id. Categories might not have documents directly.
        
        is_formation = node.get('li_attr', {}).get('data-role') == 'formation'
        
        if is_formation:
            process_formation(node, current_path)
        else:
            # Es una categoría (sector, DAP, CCP, etc.)
            new_path = os.path.join(current_path, node_text)
            if node.get('children'):
                # print(f"📁 Entrando en categoría: {node_text}")
                traverse_tree(node.get('children'), new_path)

def main():
    print("🚀 Iniciando Extracción Masiva del Proyecto Educativo Global...")
    
    # 1. Obtener Estructura del Árbol (Todos los aprendizajes)
    tree_url = f"{BASE_URL}/{CURRENT_YEAR_ID}/Structure/GetStructureForTree"
    print(f"📡 Obteniendo mapa de formaciones desde: {tree_url}")
    
    tree_data = fetch_json(tree_url)
    
    if not tree_data:
        print("❌ No se pudo obtener el árbol de formaciones. Abortando.")
        return

    # 2. Crear carpeta raíz
    os.makedirs(TARGET_ROOT, exist_ok=True)
    
    # 3. Recorrer y descargar
    traverse_tree(tree_data, TARGET_ROOT)
    
    print("\n✨ Misión Cumplida: Todo el material educativo ha sido clonado.")

if __name__ == "__main__":
    main()
