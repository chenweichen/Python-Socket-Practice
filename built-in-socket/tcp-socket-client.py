# Client-side

import socket 

HOST = "127.0.0.1"; # "0.0.0.0" 
PORT = 7000 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True: 
    outdata = input("please input message: ")
    print("send: " + outdata)
    s.send(outdata.encode()) ## s.sendall(cMESG.encode(encoding='utf8'))

    indata = s.recv(1024)
    if len(indata) == 0: # 
        s.close()
        print("server closed connection.")
        break 
    print("recv " + indata.decode())
