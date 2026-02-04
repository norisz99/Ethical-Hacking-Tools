#!/bin/bash

# 1. TISZTA LAP (Flush)
# Törlünk minden korábbi szabályt, hogy ne akadjanak össze
iptables -F
iptables -X

# 2. DEFAULT POLICY (Alapértelmezett házirend)
# Ez a legfontosabb: MINDENT eldobunk, amit nem engedélyezünk külön!
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# 3. STATEFUL INSPECTION (Állapotvizsgálat)
# Engedélyezzük a válaszcsomagokat (pl. ha mi nyitunk meg egy weboldalt, a válasz jöhessen be)
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# 4. LOCALHOST (Loopback)
# A gép saját magával tudjon kommunikálni (pl. adatbázis és backend között)
iptables -A INPUT -i lo -j ACCEPT

# 5. SSH (Távoli elérés) - Port 22
# Csak így tudjuk távolról menedzselni a szervert
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# 6. WEBSZERVER (HTTP/HTTPS) - Port 80, 443
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# 7. PING (ICMP)
# Engedélyezzük a pinget hibakereséshez (opcionális, de hasznos)
iptables -A INPUT -p icmp -j ACCEPT

# Naplózás (Logging) - Hogy lássuk, ki próbálkozott sikertelenül
iptables -A INPUT -j LOG --log-prefix "IPTables-Dropped: "

echo "✅ Tűzfal szabályok élesítve: Default Deny Policy aktív."