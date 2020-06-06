import socket

DATA = "PING"
def tcp_client():
   client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   client.connect(("127.0.0.1", 7772))
   client.send(str.encode(DATA, "utf-8"))
   response = client.recv(4096)
   print(response)
if __name__ == "__main__":
   tcp_client()