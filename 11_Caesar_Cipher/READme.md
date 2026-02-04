# Caesar Cipher Encryption & Decryption

## 📌 Áttekintés
A Caesar-rejtjel az egyik legegyszerűbb és legismertebb titkosítási technika. Ez a projekt egy funkcionális implementáció, amely képes szövegek titkosítására és visszafejtésére egy megadott kulcs (eltolás) segítségével.

## 🧠 Logikai felépítés
A program a **modulo aritmetikát** használja az ábécé karaktereinek eltolásához:
$E_n(x) = (x + n) \mod 26$
Ahol $x$ a karakter pozíciója, $n$ pedig az eltolás mértéke. A kódom kezeli a kis- és nagybetűket, miközben a speciális karaktereket és szóközöket változatlanul hagyja.

## 💻 Funkciók
- Szöveg titkosítása tetszőleges eltolással.
- Titkosított üzenet visszafejtése (Decryption).
- Automatikus karaktertartomány-kezelés (ASCII/Unicode).