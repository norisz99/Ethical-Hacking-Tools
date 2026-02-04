
# 📡 Network IP Scanner (Ping Sweep)

## 📌 Áttekintés
Ez a script feltérképezi a helyi hálózatot (LAN), hogy megtalálja az összes aktív, csatlakoztatott eszközt. Nemcsak az IP címeket detektálja, hanem megpróbálja feloldani az eszközök hálózati nevét (Hostname) is.

## 🛠️ Funkciók
* **ICMP Ping Sweep:** ICMP csomagokat küld a hálózat minden tagjának (1-től 254-ig).
* **Multi-OS Támogatás:** Automatikusan felismeri, hogy Windowson vagy Linuxon fut, és ahhoz igazítja a ping parancsot.
* **Hostname Resolution:** A `socket` könyvtár segítségével megpróbálja lekérdezni az eszköz nevét (pl. `DESKTOP-XY`, `Samsung-TV`).
* **Sebesség:** Optimalizált időzítéssel (50ms timeout) gyorsan átvizsgálja a /24-es alhálózatot.

## 🚀 Használat
```bash
python ip_scanner.py