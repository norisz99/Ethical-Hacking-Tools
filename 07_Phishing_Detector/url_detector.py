import re
from urllib.parse import urlparse

def analyze_url_heuristics(url):
    print(f"\n--- 🤖 Heurisztikus Elemzés: {url} ---")
    
    risk_score = 0
    reasons = []
    
    # 1. Előkészítés
    parsed = urlparse(url)
    domain = parsed.netloc
    path = parsed.path
    
    # --- ÁLTALÁNOS MINTÁK KERESÉSE (NEM márkafüggő!) ---

    # 1. SZABÁLY: Túl sok pont (.) a domainben
    # A valódi cégek (otp.hu) keveset használnak. A csalók (login.secure.update.bank.com) sokat.
    dot_count = domain.count('.')
    if dot_count > 3:
        risk_score += 3
        reasons.append(f"Túl mély aldomain szerkezet ({dot_count} db pont)")

    # 2. SZABÁLY: A kötőjel (-) trükk
    # A "facebook-login-secure.com" gyanús. A "facebook.com" nem.
    dash_count = domain.count('-')
    if dash_count > 2:
        risk_score += 3
        reasons.append(f"Túl sok kötőjel a domainben ({dash_count} db)")

    # 3. SZABÁLY: IP cím használata
    # Ha számok vannak a domain helyett, az 100% scam.
    if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', domain):
        risk_score += 10
        reasons.append("IP cím használata domain név helyett (Kritikus!)")

    # 4. SZABÁLY: Olcsó/Ingyenes TLD-k (Top Level Domains)
    # Ez nem "egy linkre" vonatkozik. A .cfd, .xyz, .top végződéseket 99%-ban csalók veszik, mert 1 dollárba kerülnek.
    # Egy bank sosem használ ilyet.
    trash_tlds = ['.cfd', '.xyz', '.top', '.club', '.work', '.gq', '.cn', '.ru', '.buzz']
    
    # Megnézzük, hogy a domain vége egyezik-e bármelyikkel a listából
    found_trash_tld = False
    for tld in trash_tlds:
        if domain.endswith(tld):
            risk_score += 5
            reasons.append(f"Gyanús/Olcsó domain végződés: {tld}")
            found_trash_tld = True
            break
            
    # 5. SZABÁLY: Hosszú, összevissza URL
    if len(url) > 70:
        risk_score += 2
        reasons.append("Gyanúsan hosszú URL")

    # 6. SZABÁLY: @ jel használata (Régi trükk)
    if "@" in url:
        risk_score += 5
        reasons.append("Tiltott '@' karakter a linkben")

    # --- KIÉRTÉKELÉS ---
    print(f"Kockázati pontszám: {risk_score}/10")
    
    if risk_score >= 5:
        print("🔴 VÉLEMÉNY: VESZÉLYES ADATHALÁSZ LINK!")
    elif risk_score >= 3:
        print("🟠 VÉLEMÉNY: GYANÚS (Fokozott óvatosság)")
    else:
        print("🟢 VÉLEMÉNY: A szerkezet alapján tisztának tűnik.")
        
    if reasons:
        print("\nTalált problémák:")
        for r in reasons:
            print(f"- {r}")

if __name__ == "__main__":
    # Teszteljük le a te példáddal és egy másikkal is!
    test_links = [
        "https://glsvs.cfd/hu",                  # A te példád
        "http://secure-login-apple-id.com",      # Általános kötőjel trükk
        "http://192.168.1.55/bank/login",        # IP címes trükk
        "https://otp.hu"                         # Legális oldal
    ]
    
    print("--- 🛡️ HEURISZTIKUS PHISHING DETECTOR (v3.0) ---")
    
    user_input = input("Adj meg egy URL-t (vagy Enter a teszt sorozathoz): ").strip()
    
    if user_input:
        analyze_url_heuristics(user_input)
    else:
        print("\n[Teszt üzemmód aktiválva 4 különböző linkre...]\n")
        for link in test_links:
            analyze_url_heuristics(link)