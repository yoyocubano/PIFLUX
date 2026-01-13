import os
import json

# Paths
source_dir = "/Users/yoyocubano/Desktop/École - trabajo /PIF_Documentation"
webapp_assets_dir = os.path.join(source_dir, "webapp_assets")
trades_dir = os.path.join(webapp_assets_dir, "trades")
output_file = os.path.join(webapp_assets_dir, "trades.json")

# Existing trades data mapping to preserve images and styles
# In a full future version, this meta-data could live in the individual trade folders too (e.g. meta.json)
TRADES_META_TEMPLATE = {
    "ELF": {
        "role": "Voltage Vanguard",
        "color": "bg-yellow-400",
        "desc": "Master of circuits, currents, and safety. The spark of the job site.",
        "icon": "bolt",
        "img": "images/electrician_anime.png"
    },
    "MAF": {
        "role": "The Gearhead",
        "color": "bg-red-500",
        "desc": "Engines, diagnostics, and moving parts. Fixing the beast.",
        "icon": "build",
        "img": "images/mechanic_anime.png"
    },
    "CUF": {
        "role": "Flame Alchemist",
        "color": "bg-orange-500",
        "desc": "Precision, timing, and flavor. Kitchen discipline is key.",
        "icon": "restaurant",
        "img": "images/chef_anime.png"
    },
    "IF": {
        "role": "Cyber Operator",
        "color": "bg-blue-500",
        "desc": "Networks, code, and systems. The digital backbone.",
        "icon": "terminal",
        "img": "images/it_anime.png"
    },
    "CS": {
        "role": "Thermal Titan",
        "color": "bg-orange-600",
        "desc": "Managing heat, flow, and pressure. Keeping the cold at bay.",
        "icon": "hvac",
        "img": "images/heating_anime.png"
    },
    "BL": {
        "role": "Dough Dominator",
        "color": "bg-amber-300",
        "desc": "Rising early, kneading strength. The foundation of sustenance.",
        "icon": "bakery_dining",
        "img": "images/baker_anime.png"
    },
    "BC": {
        "role": "Blade Master",
        "color": "bg-rose-700",
        "desc": "Precision cuts and knowledge of anatomy. Respect for the source.",
        "icon": "kitchen",
        "img": "images/butcher_anime.png"
    },
    "EDF": {
        "role": "Mind Shaper",
        "color": "bg-indigo-400",
        "desc": "Guiding the next generation with patience and wisdom.",
        "icon": "school",
        "img": "images/educator_anime.png"
    },
    "COF": {
        "role": "Style Scissor",
        "color": "bg-pink-400",
        "desc": "Sculpting image and confidence with every snip.",
        "icon": "content_cut",
        "img": "images/hairdresser_anime.png"
    },
    "ASAF": {
        "role": "Vital Guardian",
        "color": "bg-emerald-400",
        "desc": "Compassion meets resilience in the front lines of health.",
        "icon": "medical_services",
        "img": "images/nursing_anime.png"
    },
    "VEF": {
        "role": "Market Maven",
        "color": "bg-purple-500",
        "desc": "The art of persuasion and value. Moving the world forward.",
        "icon": "storefront",
        "img": "images/sales_anime.png"
    }
}

def generate_master_list():
    """
    Scans the 'trades' directory for any folder that contains json files
    and builds the master trades.json list.
    """
    if not os.path.exists(trades_dir):
        print(f"Directory not found: {trades_dir}")
        return

    master_list = []
    
    # List all subdirectories in trades/
    subdirs = [d for d in os.listdir(trades_dir) if os.path.isdir(os.path.join(trades_dir, d))]
    
    print(f"Found trade folders: {subdirs}")

    for code in subdirs:
        # Check if we have metadata for this code
        if code in TRADES_META_TEMPLATE:
            meta = TRADES_META_TEMPLATE[code]
            
            # Try to get the real name from the es.json inside
            name = f"Trade {code}" # Default
            possible_es_path = os.path.join(trades_dir, code, "es.json")
            if os.path.exists(possible_es_path):
                try:
                    with open(possible_es_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if "title" in data:
                            name = data["title"].replace(f" ({code})", "") # Clean up title if it matches pattern
                except Exception as e:
                    print(f"Error reading {possible_es_path}: {e}")
            
            # Construct entry
            entry = {
                "code": code,
                "name": name,
                "trait": meta
            }
            master_list.append(entry)
        else:
            print(f"Warning: No metadata found for trade code {code}. Skipping or add to template.")

    # Sort list by code to keep it stable
    master_list.sort(key=lambda x: x["code"])

    # Write to trades.json
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(master_list, f, indent=4, ensure_ascii=False)
    
    print(f"Successfully generated {output_file} with {len(master_list)} trades.")

if __name__ == "__main__":
    generate_master_list()
