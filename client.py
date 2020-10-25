import socket

HEADER = 64
FORMAT = "utf-8"
HOST = socket.gethostbyname(socket.gethostname())
PORT = 42069
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(1024).decode(FORMAT))

send("Hello World!")
input()
send("2")
input()
send("1")

send(DISCONNECT_MESSAGE)