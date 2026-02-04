import hashlib
import os

def debug_hashes():
    # 1. GENERÁLJUK LE MI MAGUNK A REFERENCIÁT
    # Ez a "tökéletes" secret123 hash, ahogy a gép látja
    target_word = "secret123"
    reference_hash = hashlib.sha256(target_word.encode('utf-8')).hexdigest()
    
    print("\n--- 🕵️ HASH DIAGNOSZTIKA ---")
    print(f"1. A referencia szó: '{target_word}'")
    print(f"2. Ennek a várt hash-e: {reference_hash}")
    print("-" * 50)
    
    # 3. KERESSÜK MEG A FÁJLT
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "passwords.txt")
    
    if not os.path.exists(file_path):
        print("❌ HIBA: Nem találom a passwords.txt fájlt!")
        return

    print(f"3. Fájl olvasása: {file_path}")
    print("-" * 50)

    # 4. OLVASSUK BE SORONKÉNT ÉS HASONLÍTSUK ÖSSZE
    with open(file_path, "r", encoding="latin-1") as f:
        for i, line in enumerate(f):
            cleaned_word = line.strip() # Levágjuk az entert/szóközt
            current_hash = hashlib.sha256(cleaned_word.encode('utf-8')).hexdigest()
            
            # Kiírjuk, mit látunk
            match_status = "✅ EGYEZIK!" if current_hash == reference_hash else "❌ Nem egyezik"
            
            print(f"Sor {i+1}: '{cleaned_word}'")
            print(f"      Hash: {current_hash}")
            print(f"      Eredmény: {match_status}")
            print("-" * 20)

if __name__ == "__main__":
    debug_hashes()
    input("\nNyomj Enter-t a kilépéshez...")