import socket
import threading

BIND_PORT = 7773
BIND_IP = "127.0.0.1"

def handle_client(client_socket):
   request = client_socket.recv(1024)
 
   print(f"[*] Received: {request}")
 
   client_socket.send("<html><title>python simple server</title><body></body></html>".encode())
   client_socket.close()

def tcp_server():
   server = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
   server.bind((BIND_IP, BIND_PORT))
   server.listen(5)
 
   print(f'[*] Listening on {BIND_IP}, {BIND_PORT}')
   while 1:
       client, addr = server.accept()
       print(f'[*] Accepted connection: {addr[0]}:{addr[1]}')
      
       client_handler = threading.Thread(target=handle_client, args=(client,))
       client_handler.start()

tcp_server()