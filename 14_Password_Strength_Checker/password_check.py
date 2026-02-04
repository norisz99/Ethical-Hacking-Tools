import re

def check_password_strength(password):
    strength = 0
    remarks = []
    
    if len(password) >= 8: strength += 1
    else: remarks.append("Túl rövid (min. 8 karakter)")
    
    if re.search("[a-z]", password) and re.search("[A-Z]", password): strength += 1
    else: remarks.append("Hiányzik a kis- vagy nagybetű")
    
    if re.search("[0-9]", password): strength += 1
    else: remarks.append("Nincs benne szám")
    
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password): strength += 1
    else: remarks.append("Nincs benne speciális karakter")
    
    return strength, remarks

# Tesztelés
pw = input("Adj meg egy jelszót: ")
score, tips = check_password_strength(pw)
print(f"Erősség: {score}/4. Javaslatok: {tips}")