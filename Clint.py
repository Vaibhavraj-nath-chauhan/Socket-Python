import time, socket, sys
#clint Side
class connect:
    def __init__(self):
        self.socket_server = socket.socket()
        self.server_host = socket.gethostname()
        self.ip = socket.gethostbyname(self.server_host)
    def bind(self,name):
        sport = 8080
        self.server_host = "192.168.43.7" # Enter host IP Adress
        self.socket_server.connect((self.server_host, sport))
        self.socket_server.send(name.encode())
        
        self.server_name = self.socket_server.recv(1024)
        self.server_name = self.server_name.decode()
         #Pint message 
        print(self.server_name,"has joined...")

    def chat(self,message):
        while True:
            sMessage = (self.socket_server.recv(1024)).decode()
            if sMessage =="exit":
                break
            print(self.server_name, ":", sMessage)
            self.socket_server.send(message.encode()) 
            if message =="exit":
                break