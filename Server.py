import time, socket, sys
class connect:
    def __init__(self):
        self.new_socket = socket.socket()
        self.host_name = socket.gethostname()
        self.s_ip = socket.gethostbyname(self.host_name)
    def bind(self,name):
        port = 8080
        self.new_socket.bind((self.host_name, port))
        self.new_socket.listen(1) 
        self.conn, add = self.new_socket.accept()
        self.conn.send(name.encode())
        self.client = (self.conn.recv(1024)).decode()
        # set text to board
        # ' has joined...'
    def chat(self,message):
        self.conn.send(message.encode())
        message = self.conn.recv(1024)
        message = message.decode()
        print(self.client, ':', message)