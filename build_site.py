import os
import markdown
import glob

# Configuration
SOURCE_DIR = "/Users/yoyocubano/Desktop/École - trabajo /PIF_Documentation"

# HTML Template with 21st.dev inspired style + MathJax
TEMPLATE_PAGE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        :root {{
            --bg-color: #f9fafb;
            --text-color: #111827;
            --card-bg: #ffffff;
            --accent: #2563eb;
            --border: #e5e7eb;
            --code-bg: #f3f4f6;
            --heading: #1f2937;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.7;
            margin: 0;
            padding: 0;
        }}
        .navbar {{ background: #fff; border-bottom: 1px solid var(--border); padding: 1rem 2rem; position: sticky; top: 0; z-index: 10; display: flex; justify-content: space-between; align-items: center; }}
        .navbar a {{ color: var(--heading); font-weight: 600; text-decoration: none; font-size: 0.95rem; }}
        .navbar a:hover {{ color: var(--accent); }}
        
        .container {{ max-width: 800px; margin: 2rem auto; padding: 0 1.5rem; }}
        
        h1, h2, h3 {{ color: var(--heading); letter-spacing: -0.02em; font-weight: 700; }}
        h1 {{ font-size: 2.25rem; margin-bottom: 1.5rem; }}
        h2 {{ font-size: 1.5rem; margin-top: 2.5rem; border-bottom: 1px solid var(--border); padding-bottom: 0.5rem; }}
        
        a {{ color: var(--accent); text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        
        pre {{ background: var(--code-bg); padding: 1.25rem; border-radius: 8px; overflow-x: auto; border: 1px solid var(--border); }}
        code {{ background: var(--code-bg); padding: 0.2rem 0.4rem; border-radius: 4px; font-size: 0.9em; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }}
        
        blockquote {{ border-left: 4px solid var(--accent); margin: 1.5rem 0; padding-left: 1rem; color: #4b5563; font-style: italic; background: #eff6ff; padding: 1rem; border-radius: 0 8px 8px 0; }}
        
        table {{ width: 100%; border-collapse: collapse; margin: 2rem 0; }}
        th, td {{ padding: 0.75rem; border-bottom: 1px solid var(--border); text-align: left; }}
        th {{ font-weight: 600; background: var(--code-bg); }}
        
        /* MathJax */
        .MathJax {{ font-size: 1.1em !important; }}
        
        .footer {{ text-align: center; padding: 3rem; color: #6b7280; font-size: 0.85rem; border-top: 1px solid var(--border); margin-top: 4rem; }}
    </style>
    <script>
    MathJax = {{
      tex: {{ inlineMath: [['$', '$'], ['\\(', '\\)']], displayMath: [['$$', '$$']] }},
      svg: {{ fontCache: 'global' }}
    }};
    </script>
    <script type="text/javascript" id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
</head>
<body>
    <nav class="navbar">
        <a href="index.html">← PIF Study Hub</a>
        <span style="color: #9ca3af; font-size: 0.85rem;">Centro de Estudio</span>
    </nav>
    <div class="container">
        <h1>{title}</h1>
        {content}
    </div>
    <div class="footer">
        Generado para el éxito en el PIFQU • 2026
    </div>
</body>
</html>
"""



# JSON Data Structure for UI Components (Simulating 21st.dev / CMS)
SITE_DATA = {
    "hero": {
        "title": "La Aventura del <span class='text-blue-600'>Instalador</span>",
        "subtitle": "Centro de Estudio Digital PIF • 2026",
        "bg_image": "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?q=80&w=2070&auto=format&fit=crop", # Cinematic Industrial
        "tag": "PROJET INTÉGRÉ FINAL",
    },
    "sections": [
        {
            "id": "predictions",
            "title": "🔮 Predicción Estratégica",
            "layout": "grid-1",
            "items": [
                {
                    "title": "Predicción del Examen 2026",
                    "desc": "Análisis de frecuencia y preguntas aseguradas para este año.",
                    "link": "POSIBLES_PREGUNTAS_NUEVO_PIF.html",
                    "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=2015&auto=format&fit=crop", # Strategy / Chart
                    "badge": "⭐ LO MÁS IMPORTANTE"
                }
            ]
        },
        {
            "id": "notes",
            "title": "🧠 Conocimiento Maestro",
            "layout": "grid-2",
            "items": [
                {
                    "title": "Notas Maestras",
                    "desc": "Compendio de 40 fuentes y fórmulas.",
                    "link": "Resumen_Tecnico_y_Formulas.html",
                    "image": "https://images.unsplash.com/photo-1517842645767-c639042777db?q=80&w=800&auto=format&fit=crop", # Notes / Study
                    "badge": "Esencial"
                },
                {
                    "title": "Notas Mac (Importado)",
                    "desc": "Archivo digital de tus notas personales.",
                    "link": "Notas_Personales.html",
                    "image": "https://images.unsplash.com/photo-1512314889357-e157c22f938d?q=80&w=2071&auto=format&fit=crop", 
                    "badge": "Personal"
                },
                {
                    "title": "📚 Estudio Interactivo",
                    "desc": "Visor de fórmulas, calculadora de caída de tensión y tablas de referencia.",
                    "link": "Estudio_Interactivo.html",
                    "image": "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?q=80&w=1973&auto=format&fit=crop", # Book / Study
                    "badge": "Nuevo"
                }
            ]
        },
        {
            "id": "international",
            "title": "🇩🇪 Recursos Internacionales",
            "layout": "grid-2",
            "items": [
                {
                    "title": "Formación en Alemán (DE)",
                    "desc": "Acceso directo a Carnet, Grille y Planning oficial en Alemán.",
                    "link": "https://ssl.education.lu/eSchoolBooks/Web/FP/20/Documents/Download?doctypeId=4&formationId=12658&language=de",
                    "image": "https://images.unsplash.com/photo-1527192491265-7e15c65f1dea?q=80&w=800&auto=format&fit=crop", # Technical / Office
                    "badge": "OFICIAL DE"
                },
                {
                    "title": "Cuestionario PIF DE (2024)",
                    "desc": "Versión alemana del Proyecto Integrado Final más reciente.",
                    "link": "https://ssl.education.lu/eSchoolBooks/Web/FP/19/Documents/Download?doctypeId=8&formationId=12441&language=de",
                    "image": "https://images.unsplash.com/photo-1516321497487-e288fb19713f?q=80&w=800&auto=format&fit=crop", # Exam / Test
                    "badge": "PIF DE"
                }
            ]
        },
        {
            "id": "practice",
            "title": "📝 Simulacros por Año",
            "layout": "grid-3",
            "items": [
                {
                    "title": "Examen 2024",
                    "desc": "Simulacro completo reciente.",
                    "link": "Examen_2024.html",
                    "image": "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?q=80&w=800&auto=format",
                    "badge": "Nuevo"
                },
                {
                    "title": "Examen 2023",
                    "desc": "Preguntas clave de motores y lógica.",
                    "link": "Examen_2023.html",
                    "image": "https://images.unsplash.com/photo-1554224154-260327c00c40?q=80&w=800&auto=format",
                },
                {
                    "title": "Examen 2022",
                    "desc": "Enfoque en domótica y seguridad.",
                    "link": "Examen_2022.html",
                    "image": "https://images.unsplash.com/photo-1554224155-6726b3ff858f?q=80&w=800&auto=format",
                },
                {
                    "title": "Examen 2021",
                    "desc": "Cálculos de potencia complejos.",
                    "link": "Examen_2021.html",
                    "image": "https://images.unsplash.com/photo-1596495577886-d920f1fb7238?q=80&w=800&auto=format",
                },
                {
                    "title": "Examen 2020",
                    "desc": "Fundamentos y normativa.",
                    "link": "Examen_2020.html",
                    "image": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=800&auto=format",
                }
            ]
        },
         {
            "id": "narrative",
            "title": "Narrativa Técnica",
            "layout": "full-text",
            "content_file": "NARRATIVAS_DEL_PIF.md",
             "image": "https://images.unsplash.com/photo-1542831371-29b0f74f9713?q=80&w=2070&auto=format&fit=crop" # Coding / Systems
        }
    ]
}

TEMPLATE_INDEX = """
<!DOCTYPE html>
<html class="dark" lang="es">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>PIF Master Control Room Dashboard</title>
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
    <script id="tailwind-config">
        tailwind.config = {{
            darkMode: "class",
            theme: {{
                extend: {{
                    colors: {{
                        "primary": "#833cf6",
                        "background-light": "#f7f5f8",
                        "background-dark": "#050505",
                        "card-dark": "#171022",
                    }},
                    fontFamily: {{
                        "display": ["Space Grotesk"]
                    }},
                    borderRadius: {{"DEFAULT": "0.5rem", "lg": "1rem", "xl": "1.5rem", "full": "9999px"}},
                }},
            }},
        }}
    </script>
    <style>
        .glass {{
            background: rgba(23, 16, 34, 0.7);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }}
        .glow-primary {{
            box-shadow: 0 0 20px rgba(131, 60, 246, 0.3);
        }}
        .cli-text {{
            font-family: 'Courier New', Courier, monospace;
        }}
        .custom-scrollbar::-webkit-scrollbar {{ width: 6px; }}
        .custom-scrollbar::-webkit-scrollbar-track {{ background: rgba(0,0,0,0.1); }}
        .custom-scrollbar::-webkit-scrollbar-thumb {{ background: rgba(131, 60, 246, 0.4); border-radius: 10px; }}
    </style>
</head>
<body class="bg-background-light dark:bg-background-dark font-display text-slate-900 dark:text-white min-h-screen overflow-x-hidden">
<div class="layout-container flex h-full grow flex-col">
    <!-- Top Navigation -->
    <header class="flex items-center justify-between border-b border-solid border-white/10 px-6 py-4 glass sticky top-0 z-50">
        <div class="flex items-center gap-4 text-white">
            <div class="size-6 text-primary">
                <span class="material-symbols-outlined text-3xl">bolt</span>
            </div>
            <h2 class="text-white text-lg font-bold leading-tight tracking-tight">PIF MASTER CONTROL ROOM</h2>
        </div>
        <div class="flex flex-1 justify-end gap-6 items-center">
            <nav class="hidden md:flex items-center gap-8">
                <a class="text-white text-sm font-medium hover:text-primary transition-colors" href="index.html">Dashboard</a>
                <a class="text-white/60 text-sm font-medium hover:text-white transition-colors" href="Estudio_Interactivo.html">Misiones</a>
                <a class="text-white/60 text-sm font-medium hover:text-white transition-colors" href="Resumen_Tecnico_y_Formulas.html">Fórmulas</a>
                <a class="text-white/60 text-sm font-medium hover:text-white transition-colors" href="Notas_Personales.html">Notas</a>
            </nav>
            <div class="flex items-center gap-4">
                <button class="flex min-w-[120px] items-center justify-center rounded-full h-10 px-4 bg-primary text-white text-sm font-bold shadow-lg shadow-primary/20">
                    <span class="flex items-center gap-2">
                        <span class="size-2 bg-green-400 rounded-full animate-pulse"></span>
                        SYSTEM LIVE
                    </span>
                </button>
            </div>
        </div>
    </header>

    <main class="max-w-[1400px] mx-auto w-full p-6 space-y-6">
        <!-- Page Heading -->
        <div class="flex flex-wrap justify-between items-end gap-3 pb-4">
            <div class="flex flex-col gap-1">
                <p class="text-white text-4xl font-black tracking-tight">{hero_title_raw}</p>
                <p class="text-slate-400 text-lg">{hero_subtitle}</p>
            </div>
            <div class="flex gap-2 text-sm text-slate-400 bg-white/5 p-2 rounded-lg border border-white/10">
                <span class="material-symbols-outlined text-sm">schedule</span>
                <span>Actualizado: {date}</span>
            </div>
        </div>

        <!-- Bento Grid Layout -->
        <div class="grid grid-cols-1 md:grid-cols-4 grid-rows-auto gap-6">
            
            <!-- Narrative Hero Block (Span 2x2) -->
            <div class="md:col-span-2 md:row-span-2 glass rounded-xl overflow-hidden flex flex-col group relative">
                <div class="absolute inset-0 bg-gradient-to-t from-background-dark via-transparent to-transparent z-10"></div>
                <div class="h-[450px] w-full bg-center bg-cover transition-transform duration-700 group-hover:scale-105" style='background-image: url("{narrative_bg}");'></div>
                <div class="absolute top-6 left-6 z-20">
                    <span class="bg-primary/90 text-white px-3 py-1 rounded-full text-xs font-bold uppercase tracking-widest">Misión Principal</span>
                </div>
                <div class="p-8 relative z-20 flex-1 flex flex-col justify-end gap-4">
                    <div>
                        <p class="text-primary text-sm font-bold tracking-widest uppercase mb-2">Technical Narrative</p>
                        <h3 class="text-white text-3xl font-bold leading-tight">La Aventura del Instalador</h3>
                    </div>
                    <!-- Segmented Selection Placeholder -->
                    <div class="flex h-12 items-center justify-center rounded-xl bg-white/5 p-1 border border-white/10 w-full max-w-md">
                        <a href="NARRATIVAS_DEL_PIF.html" class="flex grow items-center justify-center rounded-lg px-2 bg-primary text-white text-sm font-bold transition-all">
                            <span>Comenzar Lectura</span>
                        </a>
                    </div>
                    <div class="flex items-center justify-between">
                        <p class="text-slate-300 max-w-xs italic">"Cada chispa es una lección; cada tablero, una victoria."</p>
                        <a href="NARRATIVAS_DEL_PIF.html" class="flex min-w-[140px] items-center justify-center rounded-xl h-12 px-6 bg-primary text-white font-bold hover:scale-105 transition-transform glow-primary">
                            Ir a la Historia
                        </a>
                    </div>
                </div>
            </div>

            <!-- Technical Readouts Block -->
            <div class="glass rounded-xl p-6 flex flex-col gap-4">
                <div class="flex items-center justify-between">
                    <h4 class="text-white font-bold flex items-center gap-2">
                        <span class="material-symbols-outlined text-primary">data_thresholding</span>
                        Technical Mastery
                    </h4>
                    <span class="text-[10px] text-green-400 font-mono">EN TIEMPO REAL</span>
                </div>
                <div class="space-y-4">
                    <div class="p-3 bg-white/5 border border-white/5 rounded-lg">
                        <div class="flex justify-between mb-1">
                            <span class="text-xs text-slate-400">Ley de Ohm & Potencia</span>
                            <span class="text-xs text-green-400">95%</span>
                        </div>
                        <div class="w-full bg-white/10 h-1.5 rounded-full mt-2 overflow-hidden">
                            <div class="bg-primary h-full w-[95%]"></div>
                        </div>
                    </div>
                    <div class="p-3 bg-white/5 border border-white/5 rounded-lg">
                        <div class="flex justify-between mb-1">
                            <span class="text-xs text-slate-400">Cálculo de Secciones</span>
                            <span class="text-xs text-green-400">88%</span>
                        </div>
                        <div class="w-full bg-white/10 h-1.5 rounded-full mt-2 overflow-hidden">
                            <div class="bg-primary h-full w-[88%]"></div>
                        </div>
                    </div>
                    <div class="p-3 bg-white/5 border border-white/5 rounded-lg">
                        <div class="flex justify-between mb-1">
                            <span class="text-xs text-slate-400">Motores & Esquemas</span>
                            <span class="text-xs text-green-400">76%</span>
                        </div>
                        <div class="w-full bg-white/10 h-1.5 rounded-full mt-2 overflow-hidden">
                            <div class="bg-primary h-full w-[76%]"></div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- System Status Block (CLI) -->
            <div class="glass rounded-xl p-6 bg-black/40 border-primary/20">
                <div class="flex items-center gap-2 mb-4 border-b border-white/10 pb-2">
                    <div class="flex gap-1.5">
                        <div class="size-2 bg-red-500/50 rounded-full"></div>
                        <div class="size-2 bg-yellow-500/50 rounded-full"></div>
                        <div class="size-2 bg-green-500/50 rounded-full"></div>
                    </div>
                    <span class="text-[10px] text-slate-500 font-mono ml-2">TERMINAL - AntiGravity CLI</span>
                </div>
                <div class="cli-text text-xs space-y-2">
                    <p class="text-primary"><span class="text-slate-500">&gt;</span> Gemini Engine: <span class="text-green-400">AUTORIZADO</span></p>
                    <p class="text-primary"><span class="text-slate-500">&gt;</span> Audit Protocol: <span class="text-blue-400">ACTIVE_TUNNEL</span></p>
                    <p class="text-primary"><span class="text-slate-500">&gt;</span> Local Storage: <span class="text-slate-400">SSD_PIF_2026</span></p>
                    <p class="text-primary uppercase mt-4"><span class="text-slate-500">&gt;</span> STATUS: <span class="text-white animate-pulse">DALES GAS_</span></p>
                </div>
            </div>

            <!-- Sections Container -->
            {sections_html}

            <!-- PDF Archivo Central (Full Width at bottom) -->
            <div id="downloads" class="md:col-span-4 glass rounded-xl overflow-hidden mt-6">
                <div class="p-6 border-b border-white/10 flex justify-between items-center bg-white/5">
                    <div>
                        <h2 class="text-2xl font-bold text-white">📂 Archivo Central de PDFs</h2>
                        <p class="text-slate-400 text-sm">Biblioteca técnica oficial y exámenes históricos.</p>
                    </div>
                    <span class="text-[10px] font-mono bg-white/10 text-slate-400 px-3 py-1 rounded-full">SYNC: CLOUD_STORAGE</span>
                </div>
                <div class="divide-y divide-white/5 max-h-80 overflow-y-auto custom-scrollbar bg-black/20">
                    {pdf_list}
                </div>
            </div>

        </div>
    </main>
    <footer class="py-12 px-10 border-t border-white/5 flex flex-col md:flex-row justify-between items-center text-slate-500 text-[10px] uppercase font-bold tracking-widest gap-4">
        <div>© 2026 PIF TECHNICAL COMMAND • DESIGN BY STITCH (21ST.DEV)</div>
        <div class="flex items-center gap-6">
            <span class="flex items-center gap-2"><span class="size-1.5 bg-green-500 rounded-full animate-pulse"></span> FIREBASE OPERATIONAL</span>
            <span class="flex items-center gap-2"><span class="size-1.5 bg-blue-500 rounded-full animate-pulse"></span> CLI TUNNEL OPEN</span>
        </div>
    </footer>
</div>
</body>
</html>
"""

def build_interactive_study_page():
    # Gather images - ONLY from extracted_notes as requested
    img_dirs = [
        os.path.join(SOURCE_DIR, "assets", "extracted_notes")
    ]
    
    image_paths = []
    for d in img_dirs:
        if os.path.exists(d):
            for f in os.listdir(d):
                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    # Create relative path for HTML
                    rel = os.path.relpath(os.path.join(d, f), SOURCE_DIR)
                    image_paths.append(rel)
    
    # Sort for consistency
    image_paths.sort()

    book_style_html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Estudio Interactivo - Modo Libro</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;1,400&family=Inter:wght@400;600&display=swap" rel="stylesheet">
        <style>
            body {{
                font-family: 'Merriweather', serif;
                background-color: #f9f7f1; /* Cream / Paper color */
                color: #2d3748;
            }}
            .sans {{ font-family: 'Inter', sans-serif; }}
            .book-container {{
                max-width: 900px;
                margin: 0 auto;
                background: #fff;
                padding: 3rem;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
                min-height: 100vh;
                border-left: 1px solid #e2e8f0;
            }}
            /* Slider Styling */
            .slider-container {{
                position: relative;
                width: 100%;
                height: 600px;
                overflow: hidden;
                border-radius: 8px;
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
                background: #000;
                margin-bottom: 2rem;
            }}
            .slide {{
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                opacity: 0;
                transition: opacity 0.8s ease-in-out;
                display: flex;
                align-items: center;
                justify-content: center;
            }}
            .slide.active {{ opacity: 1; }}
            .slide img {{
                max-width: 100%;
                max-height: 100%;
                object-fit: contain;
            }}
            .slider-nav {{
                position: absolute;
                bottom: 20px;
                left: 50%;
                transform: translateX(-50%);
                display: flex;
                gap: 10px;
                z-index: 10;
            }}
            .nav-dot {{
                width: 12px;
                height: 12px;
                border-radius: 50%;
                background: rgba(255,255,255,0.5);
                cursor: pointer;
            }}
            .nav-dot.active {{ background: white; }}
            
            /* Table Styling */
            .fixed-table {{
                width: 100%;
                border-collapse: collapse;
                margin: 2rem 0;
                font-size: 0.95rem;
            }}
            .fixed-table th, .fixed-table td {{
                border: 1px solid #cbd5e0;
                padding: 12px;
                text-align: left;
            }}
            .fixed-table th {{
                background-color: #edf2f7;
                font-weight: 700;
                color: #2d3748;
            }}
            .fixed-table tr:nth-child(even) {{ background-color: #f7fafc; }}
            
            /* Input Styling */
            input, select {{
                font-family: 'Inter', sans-serif;
            }}
        </style>
    </head>
    <body>
        <div class="book-container">
            <header class="mb-10 text-center border-b pb-6 border-gray-200">
                <a href="index.html" class="inline-block mb-4 text-sm text-gray-500 hover:text-gray-800 sans">← Volver al Hub</a>
                <h1 class="text-4xl font-bold mb-2">Compendio de Estudio Técnico</h1>
                <p class="text-gray-600 italic">Visualización de fórmulas, cálculo y referencia.</p>
            </header>

            <!-- SLIDER SECTION -->
            <section class="mb-12">
                <h2 class="text-2xl font-bold mb-4 border-l-4 border-blue-500 pl-4">Galería de Fórmulas y Notas</h2>
                <div class="slider-container" id="mainSlider">
                    <!-- Slides injected here -->
                    {''.join([f'<div class="slide {"active" if i==0 else ""}"><img src="{img}" alt="Slide {i}"></div>' for i, img in enumerate(image_paths)])}
                    
                    <!-- Navigation Controls -->
                    <button onclick="changeSlide(-1)" class="absolute left-4 top-1/2 transform -translate-y-1/2 bg-black/30 hover:bg-black/50 text-white p-3 rounded-full">❮</button>
                    <button onclick="changeSlide(1)" class="absolute right-4 top-1/2 transform -translate-y-1/2 bg-black/30 hover:bg-black/50 text-white p-3 rounded-full">❯</button>
                    
                    <div class="slider-nav">
                        {''.join([f'<div class="nav-dot {"active" if i==0 else ""}" onclick="goToSlide({i})"></div>' for i in range(len(image_paths))])}
                    </div>
                </div>
                <div class="text-center sans">
                    <button onclick="toggleAutoPlay()" id="playBtn" class="px-4 py-2 bg-gray-200 rounded hover:bg-gray-300 text-sm">❚❚ Pausar Slide</button>
                </div>
            </section>

            <!-- CALCULATOR SECTION -->
            <section class="mb-12 bg-blue-50 p-8 rounded-xl border border-blue-100">
                <h2 class="text-2xl font-bold mb-6 border-l-4 border-blue-500 pl-4">Calculadora de Caída de Tensión (ΔU)</h2>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 sans">
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-2">Longitud del Cable (m)</label>
                        <input type="number" id="calc_L" class="w-full p-3 border rounded-lg" placeholder="Ej: 50">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-2">Corriente (A)</label>
                        <input type="number" id="calc_I" class="w-full p-3 border rounded-lg" placeholder="Ej: 16">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-2">Sección (mm²)</label>
                        <select id="calc_S" class="w-full p-3 border rounded-lg bg-white">
                            <option value="1.5">1.5 mm²</option>
                            <option value="2.5">2.5 mm²</option>
                            <option value="4">4 mm²</option>
                            <option value="6">6 mm²</option>
                            <option value="10">10 mm²</option>
                            <option value="16">16 mm²</option>
                            <option value="25">25 mm²</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-2">Material / Sistema</label>
                        <select id="calc_Mat" class="w-full p-3 border rounded-lg bg-white">
                            <option value="mono_cu">Monofásico (Cobre)</option>
                            <option value="tri_cu">Trifásico (Cobre)</option>
                            <option value="mono_al">Monofásico (Aluminio)</option>
                            <option value="tri_al">Trifásico (Aluminio)</option>
                        </select>
                    </div>
                </div>
                
                <div class="mt-6 flex items-center justify-between bg-white p-4 rounded-lg shadow-sm">
                    <button onclick="calculateDrop()" class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-8 rounded-lg shadow-lg transform transition hover:-translate-y-1">Calcular</button>
                    <div class="text-right">
                        <div class="text-sm text-gray-500">Caída de Tensión Resultante</div>
                        <div class="text-3xl font-bold text-blue-900" id="result_V">0.00 V</div>
                        <div class="text-sm font-bold text-gray-400" id="result_P">(0.00%)</div>
                    </div>
                </div>
                <div id="calc_warning" class="mt-2 text-red-500 text-sm font-bold hidden">⚠️ Caída de tensión excesiva (>3%)</div>
                
                <!-- FIXED UPLOADED TABLES -->
                <div class="mt-12 border-t pt-8">
                    <h3 class="text-xl font-bold mb-6 text-gray-800">Tablas de Referencia (Pose & Corrientes)</h3>
                    <div class="space-y-6">
                        <div class="bg-white p-4 rounded-lg shadow-md">
                             <p class="text-sm text-gray-500 mb-2 font-bold sans">Tableau 1: Types de pose</p>
                            <img src="assets/tables/tableau_pose.png" alt="Tabla Tipos de Pose" class="w-full h-auto rounded border border-gray-200">
                        </div>
                        <div class="bg-white p-4 rounded-lg shadow-md">
                            <p class="text-sm text-gray-500 mb-2 font-bold sans">Tableau 2: Courants Admissibles</p>
                            <img src="assets/tables/tableau_courants.png" alt="Tabla Corrientes Admisibles" class="w-full h-auto rounded border border-gray-200">
                        </div>
                    </div>
                </div>
            </section>
        </div>

        <script>
            // --- SLIDER LOGIC ---
            let currentSlide = 0;
            const slides = document.querySelectorAll('.slide');
            const dots = document.querySelectorAll('.nav-dot');
            let isPlaying = true;
            let slideInterval;

            function showSlide(n) {{
                slides[currentSlide].classList.remove('active');
                if (dots[currentSlide]) dots[currentSlide].classList.remove('active');
                
                currentSlide = (n + slides.length) % slides.length;
                
                slides[currentSlide].classList.add('active');
                if (dots[currentSlide]) dots[currentSlide].classList.add('active');
            }}

            function changeSlide(n) {{
                showSlide(currentSlide + n);
            }}

            function goToSlide(n) {{
                showSlide(n);
            }}

            function toggleAutoPlay() {{
                const btn = document.getElementById('playBtn');
                if (isPlaying) {{
                    clearInterval(slideInterval);
                    btn.innerText = "▶ Reanudar Slide";
                }} else {{
                    slideInterval = setInterval(() => changeSlide(1), 4000);
                    btn.innerText = "❚❚ Pausar Slide";
                }}
                isPlaying = !isPlaying;
            }}

            // Start Autoplay
            slideInterval = setInterval(() => changeSlide(1), 4000); // 4 seconds per slide

            // --- CALCULATOR LOGIC ---
            function calculateDrop() {{
                const L = parseFloat(document.getElementById('calc_L').value) || 0;
                const I = parseFloat(document.getElementById('calc_I').value) || 0;
                const S = parseFloat(document.getElementById('calc_S').value) || 1.5;
                const sys = document.getElementById('calc_Mat').value;

                let K; // Conductivity: Cu=56, Al=35 aprox (or resistivity rho)
                // Formula: dU = b * (rho * L * I / S) 
                // b=2 for mono, b=sqrt(3) for tri
                // rho Cu = 0.0178 (1/56), Al = 0.028 (1/35)
                
                let b = (sys.includes('mono')) ? 2 : 1.732;
                let rho = (sys.includes('cu')) ? 0.0178 : 0.028;
                
                // dU = b * rho * L * I / S
                // Using 0.0178 aprox implies Ohm*mm2/m
                
                let dU = (b * rho * L * I) / S;
                let percent = 0;
                let baseV = (sys.includes('mono')) ? 230 : 400;

                percent = (dU / baseV) * 100;

                document.getElementById('result_V').innerText = dU.toFixed(2) + " V";
                document.getElementById('result_P').innerText = "(" + percent.toFixed(2) + "%)";
                
                const warn = document.getElementById('calc_warning');
                if (percent > 3) {{
                    warn.classList.remove('hidden');
                }} else {{
                    warn.classList.add('hidden');
                }}
            }}
        </script>
    </body>
    </html>
    """
    
    with open(os.path.join(SOURCE_DIR, "Estudio_Interactivo.html"), "w", encoding="utf-8") as f:
        f.write(book_style_html)
    print("Generated Interactive Study Page")


def generate_sections_html(data, narrative_html):
    html = ""
    for section in data["sections"]:
        
        # Skip narrative as it is now the main Hero Bento block
        if section["id"] == "narrative": continue

        # Grid Setup based on layout type (Adapted for 4-col Bento)
        # Default for grid-1 items: 1 column
        col_span = "md:col-span-1"
        if section["layout"] == "grid-2": col_span = "md:col-span-2"
        if section["layout"] == "grid-3": col_span = "md:col-span-3"
        if section["layout"] == "full-text": col_span = "md:col-span-4"

        html += f'<div id="{section["id"]}" class="{col_span} space-y-6">'
        
        # Render Items
        if section.get("items"):
            # If it's a grid-3 or similar, make it a nested grid
            grid_cols = "grid-cols-1"
            if section["layout"] == "grid-2": grid_cols = "grid-cols-1 md:grid-cols-2"
            if section["layout"] == "grid-3": grid_cols = "grid-cols-1 md:grid-cols-3"

            html += f'<div class="grid {grid_cols} gap-6 h-full">'
            for item in section["items"]:
                badge = f'<span class="absolute top-4 right-4 bg-primary/90 backdrop-blur text-[10px] font-bold px-2 py-1 rounded-full text-white shadow-sm z-20">{item["badge"]}</span>' if item.get("badge") else ""
                
                html += f"""
                <a href="{item['link']}" class="group relative flex flex-col justify-end overflow-hidden rounded-xl bg-gray-900 h-64 md:h-80 transition-all duration-500 hover:scale-[1.02] border border-white/10">
                    <img src="{item['image']}" alt="" class="absolute inset-0 h-full w-full object-cover opacity-60 transition-transform duration-700 group-hover:scale-110 group-hover:opacity-100">
                    <div class="absolute inset-0 bg-gradient-to-t from-background-dark via-background-dark/20 to-transparent"></div>
                    {badge}
                    <div class="relative p-6 z-10">
                        <h3 class="text-xl font-bold text-white mb-2 group-hover:text-primary transition-colors">{item['title']}</h3>
                        <p class="text-slate-400 text-xs line-clamp-2">{item['desc']}</p>
                    </div>
                </a>
                """
            html += '</div>'
            
        html += '</div>'
    return html


# Sub-routine to build the Mac Notes Dashboard
# Sub-routine to build the Mac Notes Dashboard
def build_mac_notes_dashboard():
    notes_dir = os.path.join(SOURCE_DIR, "Notas_Mac")
    if not os.path.exists(notes_dir): return
    
    # Gather all notes first to organize them
    notes_data = [] # List of {folder, title, path}
    
    for root, dirs, files in os.walk(notes_dir):
        if "media" in root: continue
        folder_name = os.path.basename(root)
        if folder_name == "Notas_Mac": folder_name = "General"
        
        for file in files:
            if file.endswith(".html"):
                title = file.replace(".html", "")
                rel_path = os.path.relpath(os.path.join(root, file), SOURCE_DIR)
                notes_data.append({"folder": folder_name, "title": title, "path": rel_path})

    # Generate HTML content
    # Using a dedicated premium template for this dashboard
    
    cards_html = ""
    for note in notes_data:
        cards_html += f"""
        <a href="{note['path']}" class="group relative bg-white border border-gray-100 rounded-2xl p-6 hover:shadow-2xl hover:-translate-y-1 transition-all duration-300 flex flex-col h-full">
            <div class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-blue-400 to-indigo-500 rounded-t-2xl opacity-0 group-hover:opacity-100 transition-opacity"></div>
            
            <div class="flex items-start justify-between mb-4">
                <div class="px-3 py-1 bg-blue-50 text-blue-600 rounded-full text-xs font-bold uppercase tracking-wider">
                    {note['folder']}
                </div>
                <div class="text-gray-300 group-hover:text-blue-500 transition-colors">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                </div>
            </div>
            
            <h3 class="text-xl font-bold text-gray-900 mb-2 leading-snug group-hover:text-blue-600 transition-colors">
                {note['title']}
            </h3>
            
            <p class="text-sm text-gray-400 mt-auto pt-4 border-t border-gray-50 flex items-center">
                <span>Leer nota completa</span>
                <span class="ml-2 group-hover:translate-x-1 transition-transform">→</span>
            </p>
        </a>
        """

    dashboard_html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Notas Mac - Dashboard</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">
        <style>
            body {{ font-family: 'Inter', sans-serif; background-color: #f8fafc; }}
            .text-balance {{ text-wrap: balance; }}
        </style>
    </head>
    <body class="min-h-screen">
    
        <!-- Navigation -->
        <nav class="fixed top-0 w-full bg-white/80 backdrop-blur-md border-b border-gray-100 z-50">
            <div class="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
                <a href="index.html" class="text-sm font-semibold text-gray-500 hover:text-gray-900 flex items-center">
                    <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
                    Volver al Hub
                </a>
                <span class="text-xs font-mono text-gray-400">SYNC: MAC -> WEB</span>
            </div>
        </nav>

        <!-- Hero Section 21.dev Style -->
        <header class="pt-32 pb-20 px-6 text-center max-w-4xl mx-auto">
            <div class="relative w-24 h-24 mx-auto mb-8 bg-blue-600 rounded-3xl flex items-center justify-center shadow-xl shadow-blue-500/30 transform rotate-3 hover:rotate-0 transition-transform duration-500 cursor-default">
                <svg class="w-12 h-12 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path></svg>
                <!-- Decorative dot -->
                <span class="absolute top-0 right-0 -mt-2 -mr-2 w-6 h-6 bg-yellow-400 rounded-full border-4 border-white"></span>
            </div>
            
            <h1 class="text-5xl md:text-6xl font-extrabold text-gray-900 mb-6 tracking-tight text-balance">
                Tu Cerebro Digital
            </h1>
            <p class="text-xl text-gray-500 max-w-2xl mx-auto leading-relaxed">
                Colección curada de tus notas personales de Apple Notes. 
                Sincronizadas, limpias y listas para el estudio.
            </p>
        </header>

        <!-- Grid Content -->
        <main class="max-w-7xl mx-auto px-6 pb-24">
            <div class="flex items-center justify-between mb-8 border-b border-gray-200 pb-4">
                <h2 class="text-2xl font-bold text-gray-800">Recientes</h2>
                <span class="bg-gray-100 text-gray-600 px-3 py-1 rounded-full text-sm font-medium">{len(notes_data)} Notas</span>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                {cards_html}
            </div>
        </main>
        
        <footer class="text-center py-12 text-gray-400 text-sm border-t border-gray-100">
            Generado automáticamente por AntiGravity Engine
        </footer>

    </body>
    </html>
    """
    
    with open(os.path.join(SOURCE_DIR, "Notas_Personales.html"), "w", encoding="utf-8") as f:
        f.write(dashboard_html)
    print("Generated Mac Notes Dashboard")

def build_site():
    import datetime
    
    # 0. Build Mac Notes Dashboard
    build_mac_notes_dashboard()
    
    # 0.1 Build Interactive Study Page
    build_interactive_study_page()
    
    # 1. Process Markdown Files to Pages (Standard Pages)
    md_files = glob.glob(os.path.join(SOURCE_DIR, "*.md"))
    narrative_html = ""
    
    for file_path in md_files:
        filename = os.path.basename(file_path)
        
        # Read Narrative Content for embedding
        if filename == "NARRATIVAS_DEL_PIF.md":
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                content_body = "".join(lines[2:]) # Skip title
                narrative_html = markdown.markdown(content_body)
            # note: we still generate the HTML page for narrative just in case, or skip it.
            # let's generate it too.
            
        html_filename = filename.replace(".md", ".html")
        title = filename.replace(".md", "").replace("_", " ")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
            
        html_content = markdown.markdown(md_content, extensions=['fenced_code', 'tables'])
        final_html = TEMPLATE_PAGE.format(title=title, content=html_content)
        
        output_path = os.path.join(SOURCE_DIR, html_filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_html)

    # 2. Build PDF List
    pdfs = glob.glob(os.path.join(SOURCE_DIR, "*.pdf"))
    pdf_list_html = ""
    for pdf in pdfs:
        name = os.path.basename(pdf)
        pdf_list_html += f"""
        <div class="flex items-center justify-between p-4 hover:bg-gray-50 transition-colors group">
            <div class="flex items-center space-x-4">
                <div class="w-10 h-10 rounded-lg bg-red-100 text-red-600 flex items-center justify-center group-hover:bg-red-600 group-hover:text-white transition-colors">
                     PDF
                </div>
                <span class="font-medium text-gray-700">{name}</span>
            </div>
            <a href="{name}" class="text-sm font-bold text-blue-600 hover:underline">Descargar</a>
        </div>
        """

    # 3. Build Sections HTML from JSON
    sections_html = generate_sections_html(SITE_DATA, narrative_html)

    # 4. Build Final Index
    final_index = TEMPLATE_INDEX.format(
        hero_title_raw=SITE_DATA["hero"]["title"].replace("<span class='text-blue-600'>", "").replace("</span>", ""),
        hero_subtitle=SITE_DATA["hero"]["subtitle"],
        narrative_bg=SITE_DATA["sections"][-1]["image"], # Use narrative section image
        sections_html=sections_html,
        pdf_list=pdf_list_html,
        date=datetime.datetime.now().strftime("%d %b %Y, %H:%M")
    )
    
    with open(os.path.join(SOURCE_DIR, "index.html"), 'w', encoding='utf-8') as f:
        f.write(final_index)
    print("Generated Premium Index Dashboard")

if __name__ == "__main__":
    build_site()
