import random
import string

def generate_password(length=12):
    print("--- 🔐 ERŐS JELSZÓ GENERÁTOR ---")
    
    # Karakterkészletek
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()"
    
    # Mindenből legyen legalább egy
    all_chars = lower + upper + digits + symbols
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # A maradék feltöltése véletlenszerűen
    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    
    # Összekeverés, hogy ne sorrendben legyenek
    random.shuffle(password)
    
    final_password = "".join(password)
    print(f"✅ Generált jelszó: {final_password}")
    return final_password

if __name__ == "__main__":
    hossz = input("Milyen hosszú legyen a jelszó? (Enter = 12): ")
    if not hossz:
        generate_password()
    else:
        generate_password(int(hossz))
    input("\nKilépéshez nyomj Entert...")