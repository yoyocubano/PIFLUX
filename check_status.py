import os
import time
import sys

# Configuración
TARGET_DIR = "/Users/yoyocubano/Library/CloudStorage/GoogleDrive-yucolaguilar@gmail.com/Mi unidad/PROYECTO_EDUCATIVO_LUXEMBURGO_2026"
TOTAL_FORMATIONS = 16510  # Total detectado en la última ejecución
# Si el script paró, asumimos que este es el 100% de "esfuerzo" realizado, 
# aunque no todos generaron archivos.

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def get_file_count(path):
    count = 0
    for _, _, files in os.walk(path):
        count += len(files)
    return count

def main():
    # 1. Chequear estado del proceso
    script_running = os.popen("ps aux | grep parallel_scraper.py | grep -v grep").read()
    
    print("\n📡  ESTADO DEL SISTEMA DE DESCARGA")
    print("====================================")
    
    if not script_running:
        print("✅  PROCESO FINALIZADO (El script 'parallel_scraper.py' terminó su misión).")
        current_files = get_file_count(TARGET_DIR)
        print(f"📦  Total Archivos Descargados: {current_files}")
        print_progress_bar(100, 100, prefix='Progreso:', suffix='Completado', length=40)
        print("\n")
    else:
        print("🚀  PROCESO EN EJECUCIÓN...")
        # Simulación de barra basada en archivos (ya que log parsing es complejo aquí)
        # Asumimos que si sigue corriendo, monitoreamos el crecimiento
        try:
            while True:
                files = get_file_count(TARGET_DIR)
                # Como no sabemos cuántos archivos EXACTOS van a ser (solo formaciones),
                # hacemos una barra "spinner" o mostramos conteo dinámico.
                sys.stdout.write(f"\r📦  Archivos capturados: {files}   (Control-C para salir)")
                sys.stdout.flush()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n")

if __name__ == "__main__":
    main()
