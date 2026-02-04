# File Integrity Checker (SHA-256)

## 📌 Áttekintés
Ez az eszköz fájlok sértetlenségének ellenőrzésére szolgál. A kiberbiztonságban kritikus fontosságú annak biztosítása, hogy egy fájl (pl. szoftvertelepítő) nem módosult-e szállítás közben vagy kártékony kód hatására.

## 🧠 Hogyan működik?
A program a **SHA-256 (Secure Hash Algorithm)** algoritmust használja, amely egy egyirányú kriptográfiai hash függvény. 
- Ha a fájl tartalma akár csak egyetlen bittel is megváltozik, az algoritmus teljesen más "ujjlenyomatot" (checksum) generál.
- A kód "chunk-based" olvasást alkalmaz, így extra nagy fájlok (több GB) esetén is stabilan működik a memóriahasználat túllépése nélkül.

## 🚀 Használat
A program bekéri a fájl útvonalát, és visszaadja annak hexadecimális hash értékét.