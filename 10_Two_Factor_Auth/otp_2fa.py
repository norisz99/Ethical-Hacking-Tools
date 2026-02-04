import pyotp
import qrcode
import time
import os

def generate_2fa_setup():
    print("--- 2FA SETUP (Szerver oldal) ---")
    
    # 1. Shared Secret generálása (Base32)
    # Ez a "titok", amit csak a szerver és a te telefonod tudhat
    secret = pyotp.random_base32()
    
    # 2. URI készítése a QR kódhoz
    uri = pyotp.totp.TOTP(secret).provisioning_uri(
        name="Portfolio_User", 
        issuer_name="CyberSec_Demo"
    )
    
    # 3. QR kód mentése
    img = qrcode.make(uri)
    img.save("qrcode.png")
    
    print(f"[*] Titkos kulcs: {secret}")
    print("[*] QR kód elmentve 'qrcode.png' néven.")
    print("👉 Olvasd be Google Authenticatorral!")
    
    # Kép megnyitása automatikusan (Windows)
    os.system("start qrcode.png")
    return secret

def login_step(secret):
    totp = pyotp.TOTP(secret)
    print("\n--- BEJELENTKEZÉS (Kliens oldal) ---")
    
    while True:
        user_code = input("Írd be a 6 jegyű kódot az appból: ")
        
        # Ellenőrzés: A kód érvényes-e a jelenlegi 30 másodperces ablakban?
        if totp.verify(user_code):
            print("✅ SIKERES HITELESÍTÉS!")
            print("Access Granted.")
            break
        else:
            print("❌ HIBÁS kód! (Lehet, hogy lejárt?)")

if __name__ == "__main__":
    # Setup fázis
    secret_key = generate_2fa_setup()
    
    # Login fázis
    login_step(secret_key)