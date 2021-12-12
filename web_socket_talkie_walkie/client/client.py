




import socket
import time 
MAX_DATA_VALUE = 1027

HOST_IP = "127.0.0.1"
HOST_PORT = 32000

while  True : 
    try :
        s = socket.socket()
        s.connect((HOST_IP,HOST_PORT))
    except ConnectionRefusedError:
        print("Aucun connextion , Reconnexion")
        time.sleep(4)
    else:
        print("connection etablie")
        break ; 
    
while True : 
    msg_received = s.recv(MAX_DATA_VALUE)
    print("Message:", msg_received.decode("utf-8"))
    msg_envoye = input("Vous : ")
    s.sendall(msg_envoye.encode())
    
    
s.close()