import socket

#Example TCP Client

HOST = '127.0.0.1' 
PORT = 65432 


#AF_NET -> para IPv4 estandar
#SOCK_STREAM -> para indicar que es un cliente TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    output = "Correcto"
    s.sendall(b'Correcto')
    data = s.recv(1024)

print('Received', repr(data))
