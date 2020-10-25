import socket
import threading

HEADER = 5
FORMAT = "utf-8"
HOST = '127.0.0.1'
PORT = 42069
WORKER_LIST = [
    {

    }
]
DISCONNECT_MESSAGE = "!DISCONNECT"

def main():

    def send(msg, conn):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        conn.send(send_length)
        conn.send(message)

    def start():
        master.listen()
        print(f"Server is listening on {HOST}")
        while True:
            conn, addr = master.accept()
            thread = threading.Thread(target=handle_client, args=(conn,addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

    def handle_client(conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")

        connected = True
        while connected:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                    send("Disconnected", conn)
                    
                print(f"[{addr}] {msg}")


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as master:
        master.bind((HOST, PORT))
        print("Starting server...")
        start()

if __name__ == "__main__":
    main()




#if prompt == "short":
#    short_job()
#else if prompt == "medium":
#    medium_job()
#else if prompt == "long":
#    long job()