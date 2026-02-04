# Secure Login System (bcrypt)

## 📌 Áttekintés
Ez a projekt a biztonságos jelszókezelés alapjait mutatja be. A cél a "Plain Text" jelszótárolás elkerülése és a szivárgások elleni védelem demonstrálása.

## 🛠 Technikai részletek
A rendszer a **bcrypt** algoritmust használja, amely:
- **Salting:** Automatikusan sót (véletlenszerű adatot) ad a jelszóhoz a szivárványtáblás (rainbow table) támadások ellen.
- **Key Stretching:** Kriptográfiailag lassítja a folyamatot, így védve a Brute Force támadásoktól.
- **Adaptive Hashing:** A számítási költség (cost factor) állítható a jelszó kódolásakor.

## 🚀 Használat
1. Szükséges modul: `pip install bcrypt`
2. A program bekér egy jelszót, kiszámolja a hash-t, majd egy bejelentkezési kísérlettel ellenőrzi azt.