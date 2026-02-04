# Password Strength Checker (Python)

## 📌 Áttekintés
Ez egy Python-alapú eszköz, amely a jelszavak biztonsági szintjét elemzi meghatározott kritériumok alapján. Nemcsak a hosszt ellenőrzi, hanem az entrópia növeléséhez szükséges karaktertípusokat is.

## 🛠 Technikai részletek
A szkript **Reguláris Kifejezéseket (Regex)** használ a következő minták azonosítására:
- Minimum 8 karakteres hossz.
- Kis- és nagybetűk jelenléte.
- Numerikus karakterek.
- Speciális karakterek (pl. @, #, $).

## 🚀 Használat
1. Futtasd a `password_check.py` fájlt.
2. Add meg a tesztelni kívánt jelszót.
3. A program egy 0-4 skálán értékeli az erősséget és tippeket ad a javításhoz.