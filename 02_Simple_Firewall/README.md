# Stateful Firewall Script (iptables) 🛡️

## 📌 Áttekintés
Ez a Bash szkript egy "Stateful Packet Inspection" (SPI) tűzfalat konfigurál Linux szerverekhez. A szkript a kiberbiztonságban aranyszabálynak számító **"Default Deny"** elvet követi: alapértelmezetten minden bejövő kapcsolat tiltott, kivéve a kifejezetten engedélyezett szolgáltatásokat.

## 🛠 Konfiguráció
- **Policy:** DROP (Minden bejövő csomag eldobása).
- **Exceptions:**
  - SSH (22): Rendszeradminisztráció.
  - HTTP/HTTPS (80/443): Webszolgáltatás.
  - Loopback: Belső folyamatok kommunikációja.
  - Established: Már felépült kapcsolatok fenntartása.