import socket

HEADER = 5 # adjust as needed
FORMAT = "utf-8"
HOST = '127.0.0.1'
PORT = 42069
DISCONNECT_MESSAGE = "!DISCONNECT"
MANUAL = """
----------------------------------------------
exit        -   exit client
help        -   view manual
(pick a short job)       -   short job (experimental)
(pick a medium job)      -   medium job (experimental)
(pick a long job)        -   long job (experimental)
==============================================
"""

def main():

    def send(msg):
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)
        msg_length = client.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = client.recv(msg_length).decode(FORMAT)
            print(msg)


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print("Connected\n Type 'help' to view list of commands.")
        no_exit = True
        while no_exit:
            prompt = input(">>")
            if prompt == "help":
                print(MANUAL)
            elif prompt == "exit":
                no_exit = False
                send(DISCONNECT_MESSAGE)
            else:
                send(prompt)

if __name__ == "__main__":
    main()