import requests
import json
import socket

def get_ip_location(target_ip=""):
    print(f"\n--- 🌍 IP GEOLOCATION TRACKER (ip-api.com) ---")
    print(f"[*] Célpont vizsgálata: {target_ip if target_ip else 'Saját Hálózat'}")
    
    try:
        # Az ip-api.com nagyon rugalmas. 
        # Ha a végére nem írunk semmit (üres string), a saját adatainkat adja vissza.
        url = f"http://ip-api.com/json/{target_ip}"
        
        response = requests.get(url)
        data = json.loads(response.text)
        
        if data['status'] == 'fail':
            print("❌ HIBA: Nem sikerült lekérni az adatokat.")
            print(f"Ok: {data.get('message', 'Ismeretlen')}")
            return

        # Eredmények kiírása
        print("\n✅ SIKERES TALÁLAT!")
        print(f"----------------------------------------")
        print(f"📍 IP Cím:     {data.get('query')}")
        print(f"🏳️  Ország:    {data.get('country')} ({data.get('countryCode')})")
        print(f"🏙️  Város:     {data.get('city')}")
        print(f"📮 Ir.szám:    {data.get('zip')}")
        print(f"🏢 Szolgáltató: {data.get('isp')}")
        print(f"🗺️  Koordináták: {data.get('lat')}, {data.get('lon')}")
        print(f"----------------------------------------")
        
        # Google Maps Link
        print(f"🔗 Térkép: http://maps.google.com/?q={data.get('lat')},{data.get('lon')}")
        
    except Exception as e:
        print(f"\n❌ Hálózati hiba: {e}")

if __name__ == "__main__":
    user_input = input("Adj meg egy IP címet vagy Weboldalt (Enter = Saját IP): ").strip()
    
    # Ha a felhasználó weboldalt írt be (pl. google.com), először IP-re fordítjuk
    if user_input and not user_input[0].isdigit():
        try:
            resolved_ip = socket.gethostbyname(user_input)
            print(f"[*] DNS Feloldás: {user_input} -> {resolved_ip}")
            get_ip_location(resolved_ip)
        except:
            print("❌ Érvénytelen weboldal cím!")
    else:
        # Ha IP címet írt, vagy üresen hagyta
        get_ip_location(user_input)
        
    input("\nNyomj Entert a kilépéshez...")
