import socket, threading, sys, subprocess, os, time

class workerNode(threading.Thread):

    # Constructor
    def __init__(self, sock, ip):
        self.ip = ip
        self.sock = sock
        threading.Thread.__init__(self)

    # Overwrite method run di threading.Thread
    def run(self):
        # Setting timeout socketnya ( 30 detik )
        self.sock.settimeout(30)
        try:
            # Supaya client bisa kirim data terus2an, recv koneksinya terus2an
            while True:
                # Autentikasi dahulu
                print("running authentication")
                self.sock.sendall("[*] please enter your credential [username:password] : ".encode("utf-8"))
                login_data = self.sock.recv(65535).decode("utf-8").replace('\r\n', '')
                # Format autentikasinya username:password
                if login_data == "Tugas3:password123":
                    print("authentication succeeded")
                    self.sock.sendall("[+] Authentication succeed\r\n".encode("utf-8"))
                    # Supaya client bisa kirim data terus2an, recv koneksinya terus2an
                    while True:
                        # Denger perintah yang dikasih ( ukuran data yang diterima maks 65535 bytes )
                        # Ilangin \r\n , biasanya \r\n kekirim pas teken enter
                        cmd = self.sock.recv(65535).decode("ascii").replace('\r\n', '')
                        # Putty gatau kenapa kirim data empty, jadi yang di print hanya teks/command yang ada ascii-nya
                        if len(cmd) != 0:
                            print("running " + cmd)
                        cmd_timer = time.time()
                        total_timer = ""
                        # Taro command yang mau dilakukan disini ( Hanya bisa bentuk if statement aja)
                        if cmd == "Halo":
                            self.sock.sendall("Hola\r\n".encode("ascii"))
                            current_timer = time.time()
                            total_timer = "the command took " + str(current_timer - cmd_timer) + " s\r\n"
                            print(total_timer)
                            self.sock.sendall(total_timer.encode("ascii"))
                            print("finished")
                        if cmd == "Exit":
                            self.sock.close()
                            print("finished")
                            break
                        if (cmd!="Halo") and (cmd!="Exit") and (cmd!='\r\n') and (cmd!=''):
                            #
                            # Bikin childprocess, terus outputnya dikasih ke client
                            #
                            cmd_args = cmd.split(" ")
                            run_cmd = subprocess.Popen(cmd_args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                            stdout_ , stderr_ = run_cmd.communicate()
                            print("finished")
                            if stderr_ != None:
                               self.sock.sendall(str(str(stdout_)+str(stderr_)).encode("utf-8"))
                            if stderr_ == None:
                               self.sock.sendall(stdout_)
                            os.system(cmd)
                            current_timer = time.time()
                            self.sock.sendall(str("command " + cmd + " ran successfully\r\n").encode("ascii"))
                            total_timer = "the command took " + str(current_timer - cmd_timer) + " s\r\n"
                            self.sock.sendall(total_timer.encode("ascii"))
                            print(total_timer)
                            print("finished")
                else:
                    print("[-] Authentication failed")
                    self.sock.sendall("[-] authentication failed\r\n".encode("ascii"))
        except socket.error as e:
            print(e)

if __name__ == "__main__":

    # Cara run : python workerJarkom.py [alamat ip AWS/worker] [port]
    
    try:
        host = sys.argv[1]
        port = int(sys.argv[2])
        # Buat socketnya
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind address-nya
        sock.bind((host, port))
        print("active")
        while True:
            print("waiting")
            # Listen koneksinya => 5 adalah backlog-nya
            sock.listen(5)
            # Terima koneksi ( conn -> socket descriptor , addr -> set dari (ip,port) )
            conn, addr = sock.accept()
            ip, port = addr
            print("connected client " + str(ip))
            print("busy")
            # Bikin thread baru
            worker = workerNode(conn, ip)
            # Run kelas thread-nya dan join thread-nya (non-daemon thread)
            worker.start()
            worker.join()
    except socket.error:
        sock.close()
        print("dead")
    except KeyboardInterrupt:
        sock.close()
        print("dead")
