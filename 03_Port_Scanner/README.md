
# 🔍 Simple Port Scanner (TCP)

## 📌 Áttekintés
Ez az eszköz egy alapvető hálózati felderítő (Reconnaissance) script. Célja, hogy megvizsgáljon egy adott szervert vagy IP címet, és megtalálja a nyitott szolgáltatásokat (Portokat). A kiberbiztonságban ez az első lépés egy rendszer sérülékenységének vizsgálatakor.

## 🧠 Működési Elv
A program a Python `socket` könyvtárát használja, hogy TCP kapcsolatot kezdeményezzen a leggyakoribb portokon:
* **21 (FTP):** Fájlátvitel (Gyakran titkosítatlan!)
* **22 (SSH):** Biztonságos távoli vezérlés
* **80 (HTTP) / 443 (HTTPS):** Webszerverek
* **3389 (RDP):** Távoli asztal

Ha a szerver válaszol a "kopogtatásra" (TCP Handshake), a port NYITOTT-nak minősül.

## 💻 Használat
```bash
python port_scanner.py