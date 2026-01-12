import os
import time
import sys

TARGET_ROOT = "/Users/yoyocubano/Library/CloudStorage/GoogleDrive-yucolaguilar@gmail.com/Mi unidad/PROYECTO_EDUCATIVO_LUXEMBURGO_2026"

def get_size(start_path):
    total_size = 0
    file_count = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                try:
                    total_size += os.path.getsize(fp)
                    file_count += 1
                except:
                    pass
    return total_size, file_count

def monitor():
    print(f"📡 MONITOREO DE DESCARGAS ACTIVADO")
    print(f"📂 Objetivo: {TARGET_ROOT}")
    print("-" * 50)
    
    last_size = 0
    
    while True:
        try:
            size_bytes, count = get_size(TARGET_ROOT)
            size_mb = size_bytes / (1024 * 1024)
            size_gb = size_mb / 1024
            
            diff = size_mb - last_size
            last_size = size_mb
            
            # Timestamp
            ts = time.strftime("%H:%M:%S")
            
            if size_gb > 1:
                size_str = f"{size_gb:.2f} GB"
            else:
                size_str = f"{size_mb:.2f} MB"
                
            print(f"[{ts}] 📦 Archivos: {count} | 💾 Tamaño Total: {size_str} | 🚀 Velocidad (aprox): {diff:.2f} MB/s")
            
            time.sleep(5)
        except KeyboardInterrupt:
            print("\n🛑 Monitoreo detenido.")
            break
        except Exception as e:
            print(f"⚠️ Error de lectura: {e}")
            time.sleep(5)

if __name__ == "__main__":
    monitor()
