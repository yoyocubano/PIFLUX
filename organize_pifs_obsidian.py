import os
import shutil
import concurrent.futures
import sys
import time

# Configuración
SOURCE_ROOT = "/Users/yoyocubano/Library/CloudStorage/GoogleDrive-yucolaguilar@gmail.com/Mi unidad/PROYECTO_EDUCATIVO_LUXEMBURGO_2026"
DEST_PIF_LIB = "/Users/yoyocubano/Library/CloudStorage/GoogleDrive-yucolaguilar@gmail.com/Mi unidad/PIF_MASTER_LIBRARY"
DEST_OBSIDIAN = "/Users/yoyocubano/Library/CloudStorage/GoogleDrive-yucolaguilar@gmail.com/Mi unidad/CEREBRO_DIGITAL_OBSIDIAN/PROYECTO_EDUCATIVO_MAPA"

# Si no encontramos keywords, copiamos TODO, porque los nombres de archivo son genéricos (doc_XXXX.pdf).
# Estrategia: Copiar todo lo que sea PDF, organizando por carpetas.
# Si el usuario quiere SOLO PIF, tendríamos que inspeccionar el contenido o confiar en que si está en la carpeta de la formación, es relevante.
# Dado que los nombres son 'doc_XXXX.pdf', no podemos filtrar por nombre de archivo fácilmente sin metadatos.
# Asumiremos COPIA COMPLETA DE RECURSOS EDUCATIVOS dada la orden "copiar todas las carpetas".

def clean_name(name):
    return "".join([c if c.isalnum() or c in (' ', '-', '_') else '_' for c in name]).strip()

def process_file_task(task):
    src_file, dest_file, category, trade, filename = task
    try:
        # Check if destination exists
        if not os.path.exists(dest_file):
            shutil.copy2(src_file, dest_file)
            return {"status": "COPIED", "cat": category, "trade": trade, "file": filename, "path": dest_file}
        else:
            return {"status": "EXISTS", "cat": category, "trade": trade, "file": filename, "path": dest_file}
    except Exception as e:
        return {"status": "ERROR", "error": str(e)}

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    if iteration == total: 
        print()

def main():
    print("🚀 Iniciando Organización Masiva y Mapa Mental (Copia Total)...")
    
    os.makedirs(DEST_PIF_LIB, exist_ok=True)
    os.makedirs(DEST_OBSIDIAN, exist_ok=True)
    
    tasks = []
    
    print("🔍 Escaneando biblioteca completa en Drive...")
    for root, dirs, files in os.walk(SOURCE_ROOT):
        for file in files:
            if not file.lower().endswith('.pdf'):
                continue
                
            # Identificar Categoría y Oficio por la estructura de carpetas
            # Estructura: ROOT / Categoria / Oficio / archivo
            rel_path = os.path.relpath(root, SOURCE_ROOT)
            parts = rel_path.split(os.sep)
            
            if len(parts) >= 2:
                category = parts[0]
                trade = parts[-1]
            elif len(parts) == 1:
                category = "General"
                trade = parts[0]
            else:
                category = "Uncategorized"
                trade = "General"

            dest_trade_dir = os.path.join(DEST_PIF_LIB, category, trade)
            os.makedirs(dest_trade_dir, exist_ok=True)
            
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_trade_dir, file)
            
            tasks.append((src_file, dest_file, category, trade, file))

    total_tasks = len(tasks)
    print(f"📋 Archivos a procesar: {total_tasks}")
    
    knowledge_graph = {}
    copied_count = 0
    exists_count = 0
    error_count = 0
    
    print(f"⚡ Ejecutando copia paralela con barra de progreso...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=25) as executor:
        futures = {executor.submit(process_file_task, t): t for t in tasks}
        
        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            if (i+1) % 10 == 0 or (i+1) == total_tasks:
                 print_progress_bar(i + 1, total_tasks, prefix='Progreso:', suffix='Completado', length=40)
            
            res = future.result()
            
            if res["status"] in ["COPIED", "EXISTS"]:
                if res["status"] == "COPIED": copied_count += 1
                if res["status"] == "EXISTS": exists_count += 1
                
                cat = res.get("cat", "Unknown")
                trade = res.get("trade", "Unknown")
                
                if cat not in knowledge_graph: knowledge_graph[cat] = {}
                if trade not in knowledge_graph[cat]: knowledge_graph[cat][trade] = []
                
                knowledge_graph[cat][trade].append({
                    "name": res["file"],
                    "path": res["path"].replace(" ", "%20")
                })
            else:
                error_count += 1

    print("\n\n🧠 Generando Cerebro Digital en Obsidian...")
    
    index_content = "# 🗺️ Mapa Maestro del Sistema Educativo (Luxemburgo)\n\n"
    index_content += f"**Total Archivos:** {copied_count + exists_count}\n"
    index_content += f"**Copiados:** {copied_count} | **Existentes:** {exists_count}\n\n"
    
    for category, trades in knowledge_graph.items():
        cat_clean = clean_name(category)
        index_content += f"## 📂 {category}\n"
        
        cat_dir = os.path.join(DEST_OBSIDIAN, cat_clean)
        os.makedirs(cat_dir, exist_ok=True)
        
        for trade, files in trades.items():
            trade_clean = clean_name(trade)
            trade_md_path = os.path.join(cat_dir, f"{trade_clean}.md")
            
            trade_md = f"# 🛠️ {trade}\n\n"
            trade_md += f"**Categoría:** {category}\n\n"
            trade_md += "## 📚 Recursos Oficiales\n"
            
            for f in files:
                trade_md += f"- 📄 [{f['name']}](file://{f['path']})\n"
            
            with open(trade_md_path, 'w', encoding='utf-8') as f:
                f.write(trade_md)
            
            index_content += f"- [[{trade_clean}]] ({len(files)} docs)\n"
        
        index_content += "\n"

    with open(os.path.join(DEST_OBSIDIAN, "00_TABLERO_DE_MANDO_GLOBAL.md"), 'w', encoding='utf-8') as f:
        f.write(index_content)
        
    print(f"\n✨ Operación completada con éxito.")
    print(f"📦 Biblioteca Maestra: {DEST_PIF_LIB}")
    print(f"🧠 Obsidian Vault: {DEST_OBSIDIAN}")

if __name__ == "__main__":
    main()
