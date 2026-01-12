import os
import concurrent.futures
import time
from scraper_utils import BASE_URL, CURRENT_YEAR_ID, TARGET_ROOT, fetch_json, clean_name, download_file

def get_all_formations(nodes, path_prefix=""):
    formations = []
    for node in nodes:
        node_text = clean_name(node.get('text', 'Unnamed'))
        # Identify formation vs category
        # Based on previous recon, data-id is key for formations
        formation_id = node.get('li_attr', {}).get('data-id')
        
        if formation_id:
            # It's a formation
            formations.append({
                'id': formation_id,
                'name': node_text,
                'path': path_prefix
            })
        
        if node.get('children'):
            # It's a category (CCP, DAP, etc.), recurse
            new_prefix = os.path.join(path_prefix, node_text)
            formations.extend(get_all_formations(node.get('children'), new_prefix))
    return formations

def process_formation_task(formation):
    formation_id = formation['id']
    formation_name = formation['name']
    relative_path = formation['path']
    
    # Path: DRIVE/Category/FormationName
    full_path = os.path.join(TARGET_ROOT, relative_path, formation_name)
    os.makedirs(full_path, exist_ok=True)
    
    docs_url = f"{BASE_URL}/{CURRENT_YEAR_ID}/Documents/List/?formationId={formation_id}"
    docs = fetch_json(docs_url)
    
    results = []
    if docs:
        for doc in docs:
            doc_id = doc.get('Id')
            raw_title = doc.get('Title', f"doc_{doc_id}")
            lang = doc.get('Language', '').upper()
            
            filename = clean_name(raw_title) + ".pdf"
            if lang:
                filename = f"[{lang}] {filename}"
                
            target_file = os.path.join(full_path, filename)
            download_url = f"{BASE_URL}/{CURRENT_YEAR_ID}/Documents/RedirectToDownload/{doc_id}"
            
            # Execute download
            status = download_file(download_url, target_file)
            results.append(status)
            
            if status == "SUCCESS":
                print(f"✅ [DESCARGADO] {relative_path}/{formation_name} -> {filename}")
            elif status == "SKIPPED":
                pass # Silent skip
            else:
                print(f"❌ [FALLO] {filename}: {status}")
                
    return len(results)

def main():
    print("🚀 Iniciando SWARM DE DESCARGA PARALELA (Multiscript/Threaded)...")
    print(f"🎯 Destino: {TARGET_ROOT}")
    
    # 1. Fetch Structure
    tree_url = f"{BASE_URL}/{CURRENT_YEAR_ID}/Structure/GetStructureForTree"
    print("📡 Obteniendo mapa estratégico de formaciones...")
    tree_data = fetch_json(tree_url)
    
    if not tree_data:
        print("❌ Error crítico: No se pudo obtener el árbol de formaciones.")
        return

    # 2. Flatten List
    all_formations = get_all_formations(tree_data)
    print(f"📋 Objetivos identificados: {len(all_formations)} formaciones educativas.")
    
    # 3. Parallel Execution
    # Usamos 10 workers para multiplicar la velocidad por 10x respecto al script anterior
    max_workers = 12 
    print(f"⚡ Desplegando {max_workers} agentes de descarga simultáneos...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_formation_task, f): f for f in all_formations}
        
        total_processed = 0
        for future in concurrent.futures.as_completed(futures):
            try:
                # We just consume the results to ensure exceptions are caught
                res = future.result()
                total_processed += 1
                if total_processed % 5 == 0:
                    print(f"📊 Progreso: {total_processed}/{len(all_formations)} formaciones procesadas.")
            except Exception as e:
                print(f"⚠️ Error en un agente: {e}")

    print("\n✨ Misión 'Swarm' Completada: Todo el material está seguro en Google Drive.")

if __name__ == "__main__":
    main()
