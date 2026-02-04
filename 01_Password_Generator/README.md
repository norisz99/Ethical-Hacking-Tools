# 🔐 Strong Password Generator

## 📌 Áttekintés
Ez a Python script erős, véletlenszerű jelszavakat generál, amelyek ellenállnak a szótárazó (Dictionary) és a Brute Force támadásoknak. A program garantálja, hogy a jelszó tartalmazzon kisbetűt, nagybetűt, számot és speciális karaktert is.

## 🛠️ Használt Technológiák
* **Python 3.x**
* `random` modul: A véletlenszerű kiválasztáshoz.
* `string` modul: A karakterkészletek (ASCII) kezeléséhez.

## 🚀 Hogyan működik?
1. A program bekéri a kívánt jelszóhosszt (alapértelmezett: 12 karakter).
2. Létrehoz egy "pool"-t (karakterkészletet) betűkből, számokból és szimbólumokból.
3. **Biztonsági garancia:** Külön biztosítja, hogy minden típusból (szám, nagybetű, stb.) legalább egy bekerüljön.
4. Összekeveri (shuffle) a karaktereket, hogy a sorrend ne legyen megjósolható.

## 💻 Használat
```bash
python password_gen.py