# 🤖 Guía Maestra: Gemini CLI & Hacks de IA

Esta guía documenta el uso del **Gemini CLI** instalado en tu sistema para potenciar tu flujo de trabajo en el PIF y desarrollo general.

## 🛠️ Instalación y Acceso
El comando principal es `gemini`. Está disponible en cualquier terminal de tu sistema.

## 🚀 Comandos de Poder (Hacks)

### 1. El Consultor Instantáneo
No necesitas abrir el navegador. Pregunta cualquier cosa técnica del PIF directamente:
```bash
gemini "¿Cuál es la caída de tensión máxima permitida para iluminación según la normativa?"
```

### 2. Modo Chat (Cerebro Persistente)
Si quieres una sesión de brainstorming larga:
```bash
gemini chat
```
*Escribe `exit` para salir.*

### 3. Auditor de Código y Archivos
Pasa archivos completos para que Gemini los revise o mejore:
```bash
gemini "Mejora el rendimiento de este script de Python y añade manejo de errores" build_site.py
```

### 4. Flujo de Tubería (Terminal Hacks)
Puedes enviar la salida de cualquier comando a Gemini para que la procese:
```bash
# Ejemplo: Analizar errores en los logs
cat error.log | gemini "¿Qué está causando este error y cómo lo arreglo?"

# Ejemplo: Documentar carpetas
ls -R | gemini "Explica la estructura de este proyecto a un nuevo desarrollador"
```

## 🔐 Configuración de Identidad
Si encuentras errores de permisos, asegúrate de estar autenticado con Google Cloud:
```bash
gcloud auth login
gcloud auth application-default login
```

## 📂 Integración con el PIF
Puedes usar Gemini para generar contenido para tu sitio automáticamente:
```bash
gemini "Crea una narrativa estilo anime sobre el Acto 7: La Puesta a Tierra" > ACTO_7.md
```

---
*Generado por AntiGravity para el Centro de Estudio PIF 2026*
