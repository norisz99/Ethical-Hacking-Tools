# Kernel-Level Input Monitor (Keylogger) ⌨️

## 📌 Áttekintés
Ez a projekt az operációs rendszer beviteli eseményeinek "elkapását" (Input Hooking) demonstrálja. A program egy háttérfolyamatot indít, amely figyeli a billentyűzet hardveres megszakításait és azokat olvasható formátumban naplózza.

## ⚠️ Biztonsági megjegyzés
A kód futtatását a legtöbb vírusirtó (pl. Windows Defender) gyanúsnak találhatja, mivel a viselkedése megegyezik a kémprogramokéval. Ez a viselkedés alapú detektálás (Heuristic Analysis) kiváló példája.