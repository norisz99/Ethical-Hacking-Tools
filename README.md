# Cybersecurity & Python Portfolio - Level 1
A collection of Python scripts demonstrating cybersecurity concepts (Network Scanning, Cryptography, 2FA, Malware Analysis).
# 🛡️ Cybersecurity & Python Portfolio

**Author:** [Paczok Norisz]  
**Focus:** Ethical Hacking, Network Security, Cryptography, Python Development

---

## 📌 Overview
This repository contains a comprehensive collection of **14 Python-based security tools** developed to demonstrate fundamental concepts in cybersecurity. Each project focuses on a specific domain, ranging from network reconnaissance to cryptographic algorithms and defensive mechanisms.

## 📂 Project Catalog

### 🌐 Network Reconnaissance & Analysis
| Project | Description | Key Skills |
| :--- | :--- | :--- |
| **[03_Port_Scanner](./03_Port_Scanner)** | TCP scanner to identify open ports and services. | `socket`, TCP Handshake |
| **[04_IP_Scanner](./04_IP_Scanner)** | Network discovery tool (Ping Sweep) with hostname resolution. | ICMP, ARP, LAN Mapping |
| **[08_IP_Lookup_Geo](./08_IP_Lookup_Geo)** | Geolocation tracker using public APIs. | API Integration, JSON |
| **[07_Phishing_Detector](./07_Phishing_Detector)** | Heuristic URL analysis to detect potential threats. | Regex, Threat Intelligence |

### ⚔️ Offensive Security (Simulation)
| Project | Description | Key Skills |
| :--- | :--- | :--- |
| **[05_Brute_Force_Tool](./05_Brute_Force_Tool)** | Login simulation to test credential strength against attacks. | Authentication, Iteration |
| **[06_Hash_Cracker](./06_Hash_Cracker)** | Dictionary attack tool for cracking SHA-256 hashes. | Hashing, Wordlists |
| **[09_Keylogger_Educational](./09_Keylogger_Educational)** | Keyboard hooking demonstration for malware analysis. | `pynput`, System Hooking |

### 🔐 Cryptography & Identity
| Project | Description | Key Skills |
| :--- | :--- | :--- |
| **[10_Two_Factor_Auth](./10_Two_Factor_Auth)** | TOTP-based 2FA system implementation (Google Auth). | `pyotp`, MFA, QR Codes |
| **[01_Password_Generator](./01_Password_Generator)** | Cryptographically strong random password creator. | `secrets`, Entropy |
| **[11_Caesar_Cipher](./11_Caesar_Cipher)** | Classical encryption algorithm implementation. | Cipher logic, ASCII |
| **[13_Login_System_Hashing](./13_Login_System_Hashing)** | Secure login system using salted hashes. | `bcrypt`, Salting |

### 🛡️ Defensive Tools & Utilities
| Project | Description | Key Skills |
| :--- | :--- | :--- |
| **[02_Simple_Firewall](./02_Simple_Firewall)** | Automation script for generating iptables rules. | Linux, Firewall Config |
| **[12_File_Integrity_Checker](./12_File_Integrity_Checker)** | Tool to detect unauthorized file modifications. | Hashing, Integrity |
| **[14_Password_Strength_Checker](./14_Password_Strength_Checker)** | Tool to evaluate password complexity policies. | Validation Logic |

---

## 🛠️ Technologies Used
* **Language:** Python 3.10+
* **Libraries:** `socket`, `requests`, `pyotp`, `qrcode`, `pynput`, `hashlib`, `bcrypt`
* **Tools:** VS Code, Git, Wireshark (for traffic analysis)

## ⚠️ Disclaimer
*These tools were created for **educational purposes** and portfolio demonstration only. Usage for attacking targets without prior mutual consent is illegal. I assume no liability and am not responsible for any misuse or damage caused by this program.*
