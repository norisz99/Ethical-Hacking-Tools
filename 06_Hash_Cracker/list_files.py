import os
print("--- FÁJLOK A MAPPÁBAN ---")
files = os.listdir()
for f in files:
    print(f)
print("-------------------------")
input("Nyomj Entert...")