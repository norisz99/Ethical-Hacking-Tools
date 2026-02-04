import requests
import sys

def lookup_ip(ip_address=""):
    print(f"\n--- 🛡️ IP LOOKUP TOOL (HTTPS) ---")
    
    # Ha nincs megadva IP, a sajátunkat kérdezzük le
    target = ip_address if ip_address else "json"
    
    # 1. A legstabilabb ingyenes HTTPS API
    url = f"https://ipapi.co/{target}/json/"
    
    # 2. Fejléc beállítása (Böngészőnek álcázzuk magunkat)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        print(f"Kapcsolódás a szerverhez ({url})...")
        response = requests.get(url, headers=headers, timeout=10)
        
        # SIKERES VÁLASZ (200 OK)
        if response.status_code == 200:
            data = response.json()
            
            # Ellenőrizzük, hogy nem hibaüzenetet kaptunk-e JSON-ben
            if "error" in data:
                 print(f"❌ API Hiba: {data.get('reason')}")
            else:
                print("\n✅ TALÁLAT:")
                print(f"📍 IP Cím:      {data.get('ip')}")
                print(f"🌍 Ország:      {data.get('country_name')}")
                print(f"🏙️ Város:       {data.get('city')}")
                print(f"🏢 Szolgáltató: {data.get('org')}")
                print(f"🗺️ Koordináták: {data.get('latitude')}, {data.get('longitude')}")

        # TILTOTT VÁLASZ (403 Forbidden) - Túl sok kérés
        elif response.status_code == 403:
            print("❌ HIBA 403: A szerver átmenetileg letiltotta a kérést (Rate Limit).")
            print("💡 Tipp: Próbáld meg később, vagy használj VPN-t/Mobilnetet.")
            
        else:
            print(f"❌ Szerver hiba: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("❌ HÁLÓZATI HIBA: Nincs internet, vagy a tűzfal blokkolja a Python-t.")
    except requests.exceptions.Timeout:
        print("❌ IDŐTÚLLÉPÉS: A szerver nem válaszolt 10 másodpercen belül.")
    except Exception as e:
        print(f"❌ Váratlan hiba: {e}")

if __name__ == "__main__":
    target = input("Adj meg egy IP címet (vagy Enter a sajátodhoz): ").strip()
    lookup_ip(target)
    input("\nNyomj Enter-t a kilépéshez...")