# IP Geolocation & Network Lookup

## 📌 Áttekintés
Ez egy hálózati diagnosztikai eszköz, amely külső REST API segítségével gyűjt információkat egy adott IP-címről. Hasznos lehet incidenskezeléskor vagy gyanús forgalom elemzésekor.

## ⚙️ Funkciók
- **IP Információk:** Ország, város, régió és irányítószám lekérése.
- **ISP Adatok:** Az internetszolgáltató (Internet Service Provider) beazonosítása.
- **Geolokáció:** Pontos szélességi és hosszúsági koordináták megjelenítése.

## 🛠 Stack
- **Requests modul:** A HTTP kérések kezeléséhez.
- **JSON:** Az API-tól kapott strukturált adatok feldolgozásához.
## ⚠️ Ismert korlátozások és hibaelhárítás
A projekt fejlesztése során **HTTP 403 (Forbidden)** és **Timeout** hibák léphetnek fel a nyilvános API-k (ip-api.com, ipapi.co) használatakor.

### Miért történik ez?
1. **Rate Limiting:** Az ingyenes szolgáltatók korlátozzák az egy IP-címről érkező kérések számát.
2. **Bot védelem:** Bizonyos hálózatok (tűzfalak) blokkolják a Python kéréseket.

### Megoldás portfólió felhasználóknak:
A kód fel van készítve **API Key** fogadására. Stabil, éles használathoz javasolt regisztrálni egy ingyenes kulcsot az [ipapi.com](https://ipapi.com/) vagy hasonló oldalakon, és beilleszteni a `api_key` változóba.