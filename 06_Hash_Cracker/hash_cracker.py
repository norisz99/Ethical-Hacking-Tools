import hashlib
import time
import os  # Ez nagyon fontos a fájl megtalálásához!

def crack_hash(target_hash, wordlist_file):
    # 1. Megkeressük a script saját mappáját
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Összerakjuk a teljes útvonalat (Mappa + Fájlnév)
    full_path = os.path.join(script_dir, wordlist_file)

    print(f"[*] Keresés itt: {full_path}")

    if not os.path.exists(full_path):
        print(f"❌ HIBA: A fájl nem található ezen az útvonalon!")
        return

    try:
        # A 'latin-1' kódolás segít a speciális karaktereknél
        with open(full_path, "r", encoding="latin-1") as file:
            start_time = time.time()
            count = 0
            
            print("[*] Támadás indítása...")
            
            for line in file:
                count += 1
                password = line.strip()
                
                # Jelszó hashelése
                hashed_attempt = hashlib.sha256(password.encode('utf-8')).hexdigest()
                
                # Összehasonlítás
                if hashed_attempt == target_hash:
                    elapsed = time.time() - start_time
                    print(f"\n[+] ✅ JELSZÓ MEGTALÁLVA!")
                    print(f"--> Jelszó: {password}")
                    print(f"--> Idő: {elapsed:.4f} másodperc")
                    print(f"--> Próbálkozások: {count}")
                    return

                # Státuszjelzés 5000-enként
                if count % 5000 == 0:
                    print(f"[*] {count} jelszó tesztelve...", end="\r")

            print("\n[-] ❌ A jelszó nincs a szótárban.")

    except Exception as e:
        print(f"\n❌ Váratlan hiba: {e}")

if __name__ == "__main__":
    print("--- 🔨 PROFESSIONAL HASH CRACKER (v2.0) ---")
    
    # Bekérjük a hash-t (vagy használjuk a teszt értéket)
    target = input("Add meg a SHA-256 Hash-t (Enter a demóhoz): ").strip()
    if not target:
        # Ez a 'secret123' hash-e
        target = "2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b"
        print(f"(Demo mód: 'secret123' keresése)")

    # Bekérjük a fájl nevét
    wlist = input("Add meg a szótárfájl nevét (pl. passwords.txt): ").strip()
    
    # Indítás
    crack_hash(target, wlist)
    input("\nNyomj Enter-t a kilépéshez...")