import socket

class Connection:
    def __init__(self):
        self.host="127.0.0.1"
        self.port = 6500
        self.sock=socket

    def create_connection(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.host, self.port))
        s.listen(1)
        self.sock, addr = s.accept()
        print("client connected with address " + addr[0])

    def recover(self):
        buf=self.sock.recv(1024)
        buf=buf.decode('utf8').rstrip()
        print("Message recovered good")
        return buf

    def sending(self,buf):
        self.sock.send(buf.encode('utf8'))
        print("Message sended succesfull")




connection=Connection()
connection.create_connection()
connection.recover()
connection.sending("Server answer")
