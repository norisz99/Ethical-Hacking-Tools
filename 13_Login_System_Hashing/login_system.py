import bcrypt

# Jelszó elmentése (hashelés)
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

# Jelszó ellenőrzése
def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

if __name__ == "__main__":
    print("--- REGISZTRÁCIÓ ---")
    pw = input("Adj meg egy új jelszót: ")
    hashed_pw = hash_password(pw)
    print(f"Tárolt hash: {hashed_pw.decode()}\n")

    print("--- BEJELENTKEZÉS ---")
    attempt = input("Írd be a jelszavad a belépéshez: ")
    
    if check_password(attempt, hashed_pw):
        print("✅ Sikeres belépés!")
    else:
        print("❌ Hibás jelszó!")
    
    input("\nNyomj Enter-t a kilépéshez...")