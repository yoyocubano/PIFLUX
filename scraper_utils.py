import os
import json
import urllib.request
import ssl
import time

# Configuración Global
BASE_URL = "https://ssl.education.lu/eSchoolBooks/Web/FP"
CURRENT_YEAR_ID = 20
TARGET_ROOT = "/Users/yoyocubano/Library/CloudStorage/GoogleDrive-yucolaguilar@gmail.com/Mi unidad/PROYECTO_EDUCATIVO_LUXEMBURGO_2026"

# Contexto SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def clean_name(name):
    return "".join([c if c.isalnum() or c in (' ', '-', '_') else '_' for c in name]).strip()

def fetch_json(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=30) as response:
            if response.status == 200:
                return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        pass
    return None

def download_file(url, filepath):
    if os.path.exists(filepath):
        return "SKIPPED"
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=60) as response:
            with open(filepath, 'wb') as f:
                f.write(response.read())
        return "SUCCESS"
    except Exception as e:
        return f"ERROR: {e}"
