import time
import itertools

# Ez a "célpont" - egy szimulált bejelentkezési rendszer
TARGET_PASSWORD = "admin"

def try_login(password):
    # A valóságban itt egy HTTP kérést küldenénk a szervernek
    return password == TARGET_PASSWORD

def brute_force_attack():
    print("--- BRUTE FORCE SIMULATION ---")
    print("Cél: A jelszó feltörése szótár alapú módszerrel.\n")
    
    # Egy mini "szótár" a leggyakoribb jelszavakkal
    common_passwords = [
        "123456", "password", "qwerty", "secret", "login", 
        "master", "root", "admin", "12345678"
    ]
    
    start_time = time.time()
    attempts = 0
    
    # 1. Próbálkozás a szótárból
    print("[*] Szótár (Dictionary) támadás indítása...")
    for pwd in common_passwords:
        attempts += 1
        print(f"Próba {attempts}: {pwd}")
        if try_login(pwd):
            end_time = time.time()
            print(f"\n✅ JELSZÓ MEGTALÁLVA: '{pwd}'")
            print(f"⏱️ Idő: {end_time - start_time:.4f} másodperc")
            print(f"🔨 Próbálkozások száma: {attempts}")
            return

    print("\n❌ A szótár támadás nem sikerült.")

if __name__ == "__main__":
    brute_force_attack()
    input("\nNyomj Enter-t a kilépéshez...")