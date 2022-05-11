# Server-side

import socket

HOST = "127.0.0.1"; # "0.0.0.0"
PORT = 7000; 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
s.bind((HOST, PORT))
s.listen(5)

print("server start at: %s:%s" %(HOST, PORT))
print("wait for connection...")

while True: 
    conn, addr = s.accept()
    print("connected by" + str(addr))

    while True:
        indata = conn.recv(1024)                 ## receiveData = s.recv(self.recv_parameter)
        if len(indata) == 0: # connection closed ## if not receiveData: break 
            conn.close()
            print("client closed connection.")
            break 
        print("recv: " + indata.decode())

        outdata = "echo " + indata.decode()
        conn.send(outdata.encode())  ## s.sendall(cMESG.encode(encoding='utf8'))
