import hashlib

def get_file_hash(filename):
    sha256_hash = hashlib.sha256()
    try:
        with open(filename, "rb") as f:
            # Darabokban olvassuk a fájlt, hogy nagy fájloknál se fogyjon el a RAM
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    print("--- FILE INTEGRITY CHECKER ---")
    file_path = input("Add meg a fájl nevét/útvonalát (pl. teszt.txt): ")
    
    hash_value = get_file_hash(file_path)
    
    if hash_value:
        print(f"A fájl SHA-256 lenyomata:\n{hash_value}")
        print("\nMentsd el ezt a kódot! Ha a fájl egyetlen bitet is változik, a hash teljesen más lesz.")
    else:
        print("❌ A fájl nem található.")
        
    input("\nNyomj Enter-t a kilépéshez...")