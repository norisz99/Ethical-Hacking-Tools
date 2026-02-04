# Heuristic Phishing URL Detector (v3.0) 🛡️

## 📌 Áttekintés
Ez a projekt egy **heurisztikus alapú** adathalász-link felismerő eszköz. A korábbi (statikus listákat használó) verziókkal ellentétben ez a program nem konkrét márkaneveket keres, hanem **URL-szerkezeti mintákat** és anomáliákat elemez.

A program egy **Kockázati Pontszámot (Risk Score)** számol ki minden URL-hez. Ha a pontszám átlép egy küszöbértéket, a rendszer riaszt.

## 🧠 Algoritmus és Logika
A detektor a következő "Red Flag" (gyanús) jeleket pontozza:

1.  **Trash TLD Detection:** Gyanús, olcsó domain végződések felismerése (pl. `.cfd`, `.xyz`, `.top`), amelyeket gyakran használnak eldobható csaló oldalakhoz.
2.  **Strukturális Anomáliák:**
    * **Túl sok aldomain:** (pl. `login.secure.update.bank.com`) -> A valódi cégek ritkán mennek 3 szintnél mélyebbre.
    * **Kötőjel-elárasztás:** (pl. `secure-login-facebook-account.com`) -> A "Typosquatting" tipikus jele.
3.  **IP-cím alapú URL-ek:** Ha a domain név helyett nyers IP cím szerepel (pl. `http://192.168.1.5/login`), az azonnali kritikus riasztást jelent.
4.  **Hosszúság és Obfuszkáció:** A gyanúsan hosszú vagy `@` jelet tartalmazó URL-ek büntetése.

## 🚀 Használat
A program Python környezetben futtatható. Nem igényel külső API kulcsot, mivel a mintafelismerés lokálisan történik.

```bash
python phishing_detector.py