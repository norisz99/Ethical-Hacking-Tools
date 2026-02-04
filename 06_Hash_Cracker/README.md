# Offline Dictionary Hash Cracker 🔨

## 📌 Áttekintés
Ez az eszköz demonstrálja, hogyan működnek a modern jelszófeltörő szoftverek (pl. Hashcat). Nem online próbálgatással (ami lassú), hanem offline hash-összehasonlítással dolgozik.

## 🚀 Teljesítmény
A kód **Memory Efficient** (memóriatakarékos): nem tölti be az egész fájlt a RAM-ba, hanem soronként ("Lazy Loading") dolgozza fel. Ez lehetővé teszi akár 10-20 GB-os wordlistek feldolgozását is egy átlagos laptopon.