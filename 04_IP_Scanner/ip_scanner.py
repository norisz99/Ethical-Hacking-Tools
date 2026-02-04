import os
import platform
import socket

def ping_sweep(network_prefix):
    print(f"\n--- 📡 IP SCANNER (Full Network Scan) ---")
    print(f"[*] Hálózat vizsgálata: {network_prefix}.1 - {network_prefix}.254")
    print("(Ez eltarthat egy darabig, kérlek várj...)\n")
    
    # Windows vagy Linux? (Más a ping parancs paramétere)
    # -n 1 = 1 db ping küldése
    # -w 50 = 50ms várakozás (hogy gyorsabb legyen a scan)
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    wait_param = '-w' if platform.system().lower() == 'windows' else '-W'
    
    found_hosts = 0
    
    # MOST MÁR AZ EGÉSZ HÁLÓZATOT NÉZZÜK (1-254)
    for host in range(1, 255): 
        ip = f"{network_prefix}.{host}"
        
        # A parancs összeállítása
        # Gyorsítunk rajta: csak 50ms-t várunk válaszra
        command = f"ping {param} 1 {wait_param} 50 {ip} > nul"
        
        response = os.system(command)
        
        if response == 0:
            # Ha találtunk valamit, próbáljuk meg a nevét is lekérni
            try:
                hostname = socket.gethostbyaddr(ip)[0]
                print(f"[+] 🟢 TALÁLAT: {ip} ({hostname})")
            except:
                print(f"[+] 🟢 TALÁLAT: {ip} (Név nem elérhető)")
                
            found_hosts += 1
        else:
            # Kiírjuk, hol tartunk, hogy ne tűnjön lefagyottnak
            # Az 'end=\r' miatt egy sorban frissül a számláló
            print(f"[*] Keresés... {ip}", end="\r")
            
    print(f"\n\n✅ Kész! Összesen {found_hosts} aktív eszközt találtam.")

if __name__ == "__main__":
    print("Példa hálózat: 192.168.0")
    net = input("Add meg a hálózat elejét (pl. 192.168.0): ").strip()
    
    if not net:
        net = "192.168.0" # Alapértelmezett, ha lusta vagy beírni
    
    ping_sweep(net)
    input("\nNyomj Entert a kilépéshez...")