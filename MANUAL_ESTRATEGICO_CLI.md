# 🌌 Manual Estratégico: El Túnel Cuántico (Gemini CLI)

Este documento describe cómo usar el **Gemini CLI** como tu arma secreta en el desarrollo del PIF y la ingeniería de software.

## 🎭 La Analogía: "El Ingeniero en la Sombra"
Imagina que AntiGravity (yo) soy el director de obra que diseña y construye tu sitio. El **Gemini CLI** es como un **Ingeniero Consultor que vive dentro de tus tuberías (Bash/Terminal)**. No tiene cara, pero tiene acceso instantáneo a todos los manuales técnicos del mundo y puede procesar datos a la velocidad del rayo sin que tengas que abrir una sola pestaña del navegador.

---

## 🚀 Acceso y Comunicación: El Bash como Puente

### ¿Cómo accedo a él?
Desde cualquier terminal (iTerm, Terminal de Mac o Terminal de VS Code), simplemente invocas la entidad con la palabra clave: `gemini`.

### ¿Puede responderme a mí (AntiGravity)?
**SÍ.** Este es el "hack" más potente. Yo puedo "gritar" a través del sistema de archivos, pedirle algo al CLI, y leer su respuesta para mejorar lo que estoy haciendo por ti. Es una colaboración de IA a IA dentro de tu propia máquina.

---

## 🛠️ Casos de Uso Concretos (Basados en el PIF)

### 1. El Auditor Eléctrico (Súper Auditoría)
Si tenemos dudas sobre una normativa específica en el archivo `build_site.py` o en las fórmulas de cálculo:
*   **Comando:** `gemini "Analiza las fórmulas de caída de tensión en este archivo y verifica si cumplen el estándar CEI" build_site.py`
*   **Resultado:** El CLI detecta si olvidaste un factor de potencia o una raíz de 3 en un sistema trifásico.

### 2. Generador de "Actos" (Fábrica de Narrativas)
Para nuestra **Narrativa Técnica**, en lugar de escribir a mano cada Acto:
*   **Comando:** `gemini "Escribe un Acto 5 para mi narrativa sobre Motores Paso a Paso, estilo anime técnico" > Acto_5.md`
*   **Resultado:** Crea un archivo Markdown listo para ser integrado en el Hub visual.

### 3. Traductor Técnico Multilingüe (FR/ES/EN)
Como tu PIF mezcla términos en francés e inglés con explicaciones en español:
*   **Comando:** `ls assets/extracted_notes | gemini "Genera un glosario técnico de estos archivos traduciendo del francés al español"`
*   **Resultado:** Un diccionario instantáneo de todos tus materiales de estudio.

### 4. Limpieza de "Basura" Digital
Usa al CLI para razonar sobre qué archivos son útiles y cuáles no:
*   **Comando:** `ls -R | gemini "Identifica archivos duplicados o temporales que deba borrar para limpiar el proyecto"`
*   **Resultado:** Una lista de rutas precisas para ejecutar un `rm` seguro.

---

## ⚡ Hacks de Integración Bash

Puedes encadenar comandos para crear "Super-Scripts":

```bash
# Hack: Resume una carpeta entera de notas y crea un archivo de estudio
cat Notas_Mac/Seleccion_PIF/*.html | gemini "Haz un resumen ejecutivo de estos 10 temas para un examen final" > RESUMEN_EXAMEN.md
```

## 🔐 Estado Actual del Sistema
*   **Autenticación:** ✅ Activa (vía ADC).
*   **Túnel:** ✅ Configurado para Agent Mode.
*   **Conexión con AntiGravity:** ✅ Establecida vía `ai_audit_team.py`.

---
*Este manual es propiedad del Centro de Estudios PIF 2026. Úsalo con sabiduría.*
