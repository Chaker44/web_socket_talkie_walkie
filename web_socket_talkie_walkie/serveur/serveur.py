import socket 

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_VALUE = 1027
s = socket.socket()
s.bind((HOST_IP,HOST_PORT))
s.listen()
connection_socket, client_ip = s.accept()
print(f"connection etablie avec address {client_ip}")
        
while True:
    
    msg = input("Message :")  
    connection_socket.sendall(msg.encode())
    msg_received = connection_socket.recv(MAX_DATA_VALUE)
    print("vous:", msg_received.decode("utf-8"))
    
s.close()