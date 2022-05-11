# Client-side heartbeat
import socket
import time 

HOST = "127.0.0.1"; 
PORT = 7000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True: 
    outdata = "heartbeat"
    print("send: " + outdata)
    s.send(outdata.encode())

    indata = s.recv(1024)
    if len(indata) == 0: # connection closed
        s.close()
        print("Server closed connection.")
        break 
    print("recv: " + indata.decode())

    time.sleep(1)
    