# Time-based One-Time Password (TOTP) Implementation 🔐

## 📌 Áttekintés
Ez a projekt egy szabványos (RFC 6238) kétfaktoros hitelesítési rendszert valósít meg. A kód demonstrálja a "Shared Secret" megosztását QR kódon keresztül, és a HMAC-SHA1 algoritmus használatát az időalapú kódok generálásához.

## ⚙️ Technológia
- **Library:** `pyotp` (Python One-Time Password Library)
- **Szinkronizáció:** A szerver és a kliens (telefon) órájának szinkronban kell lennie.
- **Időablak:** A kódok 30 másodpercenként frissülnek.