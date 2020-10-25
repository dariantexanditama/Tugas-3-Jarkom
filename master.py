import socket
import sys

if __name__ == "__main__":

    try:
        host = sys.argv[1]
        port = int(sys.argv[2])

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sock.connect((host, port))

            login_notification = sock.recv(
                65535).decode("utf-8").replace('\r\n', '')
            print(login_notification)
            authentication = input()
            sock.sendall(authentication.encode("utf-8"))

            while True:
                cmd = input("enter command: ")
                command = cmd + "/r/n"
                sock.sendall(cmd.encode())
                reply = sock.recv(65535).decode(
                    "utf-8").replace('\r\n', '')
                print(reply)
        except socket.error as e:
            print(e)
            sock.close()

    except socket.error:
        sock.close()
        print("dead")

