def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
        
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            # Eltolás kiszámítása az ábécén belül
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char
    return result

msg = "Hello Merok!"
encrypted = caesar_cipher(msg, 3)
print(f"Titkosított: {encrypted}") # Khoor Phurn!
# A fájl vége legyen ez:
if __name__ == "__main__":
    print("--- CAESAR CIPHER TOOL ---")
    user_msg = input("Add meg az üzenetet: ")
    user_shift = int(input("Add meg az eltolás mértékét (szám): "))
    
    encoded = caesar_cipher(user_msg, user_shift)
    print(f"\nTitkosított üzenet: {encoded}")
    
    decoded = caesar_cipher(encoded, user_shift, mode='decrypt')
    print(f"Visszafejtett üzenet: {decoded}")