import subprocess
import sys
import os

def run_gemini_task(prompt, file_path=None):
    """Executes a task using the local Gemini CLI."""
    cmd = ["gemini", prompt]
    if file_path:
        if not os.path.exists(file_path):
            return f"Error: File {file_path} not found."
        cmd.append(file_path)
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        if "Please set an Auth method" in e.stderr:
            return "❌ ERROR DE AUTENTICACIÓN: El equipo de ayuda no tiene permisos. Por favor, corre 'gcloud auth application-default login' en tu terminal para activar el túnel."
        return f"Error ejecutando Gemini CLI: {e.stderr}"
    except FileNotFoundError:
        return "Error: gemini CLI no found in system path."

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 ai_audit_team.py [audit|optimize|explain] <archivo/concepoto>")
        return

    task = sys.argv[1].lower()
    
    if task == "audit" and len(sys.argv) == 3:
        file = sys.argv[2]
        print(f"🔍 [AI TEAM] Auditando {file}...")
        report = run_gemini_task("Analiza este archivo de código en busca de bugs, errores de sintaxis o vulnerabilidades. Responde en español.", file)
        print("\n--- INFORME DE AUDITORÍA ---\n")
        print(report)
        
    elif task == "optimize" and len(sys.argv) == 3:
        file = sys.argv[2]
        print(f"⚡ [AI TEAM] Maximizando rendimiento en {file}...")
        report = run_gemini_task("Sugiere optimizaciones de rendimiento y legibilidad para este código. Responde en español.", file)
        print("\n--- SUGERENCIAS DE OPTIMIZACIÓN ---\n")
        print(report)
        
    elif task == "explain":
        concept = " ".join(sys.argv[2:])
        print(f"📖 [AI TEAM] Explicando: {concept}...")
        report = run_gemini_task(f"Explica el concepto de '{concept}' aplicado a electricidad industrial o programación. Responde en español.")
        print("\n--- CLINIC DE CONOCIMIENTO ---\n")
        print(report)
    else:
        print("Comando no reconocido o argumentos insuficientes.")

if __name__ == "__main__":
    main()
