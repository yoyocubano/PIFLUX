import time
from playwright.sync_api import sync_playwright

def shop_auchan():
    print("🛒 Starting Auchan Auto-Shopper by Antigravity...")
    
    # Items list (Cuban/Italian/Promos) based on user request (< 60EUR)
    # Using generic terms to ensure hits
    shopping_list = [
        "Sauté de porc",    # Meat
        "Pain de mie",      # Basics
        "Riz long grain",   # Cuban base
        "Oeufs 18",         # Protein
        "Jambon cuit",      # Ham
        "Filet de Saxe",    # Smoked loin substitute
        "Spaghetti",        # Italian
        "Haricots noirs",   # Cuban
        "Manioc",           # Yuca
        "Bananes",          # Fruit
        "Crackers",         # Snacks
        "Fruits rouges congelés" # Frozen fruit
    ]

    with sync_playwright() as p:
        # Launch headed so user can verify/login
        print("🚀 Launching Browser on your screen...")
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("🌐 Going to Auchan Drive...")
        page.goto("https://www.auchan.lu/fr/magasins/drive-kirchberg") 
        # Using Kirchberg as default, user can change if needed or redirection handles it
        
        # Give user time to see what's happening or log in if they want to interrupt
        # But we will try to just add to cart.
        # Note: Auchan often requires login to add to cart, or asks for postal code.
        
        print("\n⚠️  ATENCIÓN: Si te pide Login, inicia sesión manualmente en la ventana abierta.")
        print("⏳ Waiting 15 seconds for page load / login check...")
        time.sleep(15)

        total_price = 0
        
        for item in shopping_list:
            print(f"\n🔍 Searching: {item}")
            try:
                # Search bar interaction
                page.fill("input[type='search']", item)
                page.press("input[type='search']", "Enter")
                page.wait_for_load_state("networkidle")
                time.sleep(2) # Human pause

                # Find first "Add to cart" button
                # Selectors for Auchan can be tricky, looking for generic product tiles
                # Usually a button with "Ajouter" or an icon
                
                # Let's try to grab price first
                first_product = page.locator(".product-item").first
                if first_product.is_visible():
                    name = first_product.locator(".product-item__title").inner_text()
                    price_text = first_product.locator(".product-item__price").inner_text()
                    print(f"   found: {name} - {price_text}")
                    
                    # Add to cart
                    print("   ➕ Adding to cart...")
                    # Try clicking the add button. Often specific class.
                    # Fallback to generic text search if class fails
                    try:
                        first_product.locator("button.add-to-cart").click(timeout=2000)
                    except:
                        # Fallback click
                        first_product.click() # Open details
                        page.locator("button:has-text('Ajouter')").click()
                        page.go_back()
                    
                    print("   ✅ Added.")
                else:
                    print("   ❌ Not found (no results).")
                    
            except Exception as e:
                print(f"   ⚠️ Error adding {item}: {e}")
            
            time.sleep(2)

        print("\n🛒 Shopping Loop Complete!")
        print("✨ Por favor, revisa tu carrito en la ventana del navegador.")
        print("Mantendré el navegador abierto por 5 minutos para que finalices la compra.")
        time.sleep(300) # Keep open for user
        browser.close()

if __name__ == "__main__":
    shop_auchan()
