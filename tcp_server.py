import socket
import threading 

bind_ip = "127.0.0.1"
bind_port = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#datos del hosts del cual estaremos a la escucha
server.bind((bind_ip,bind_port))
#backlog conecction de 5
server.listen(5)

print("[*] A la escucha en", bind_ip,":",bind_port)


#thread para conectar con el cliente
def handle_client(client_socket):

	request = client_socket.recv(1024)
	print("[*] Se recibio -> ",request," como request")

	client_socket.sendall(b"ACK!")
	client_socket.close()


while True:
	client,addr = server.accept()

	print("[*] CONEXION ACEPTADA de ", addr[0], addr[1])

	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()