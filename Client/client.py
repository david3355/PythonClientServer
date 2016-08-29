__author__ = 'Jager'
import socket
from threading import Thread

class Client:
    def __init__(self, serveraddress, port, eventprinter,msghandler):
        self.socket = socket.socket()
        self.host = serveraddress
        self.port = port
        self.eventprinter = eventprinter
        self.msghandler = msghandler
        self.connected = False
        self.connopen = False



    def connect_to_server(self):
        try:
            self.socket.connect((self.host, self.port))
            self.connected = True
            self.start_reader()
            self.eventprinter('Connected to server!')
        except:
            self.eventprinter('Connection failed!')

    def disconnect_from_server(self):
        self.connopen = False
        self.socket.close()
        self.connected = False
        self.eventprinter('Disconnected from server')


    def isconnected(self):
        return self.connected


    def reader(self):
       while (self.connopen):
           try:
               data = self.socket.recv(2048).decode('utf-8')
               self.msghandler(data)
           except:
               self.eventprinter('Read error!')
               self.disconnect_from_server()


    def start_reader(self):
        self.connopen = True
        self.t_reader = Thread(None, self.reader)
        self.t_reader.start()


    def send(self, message):
        try:
            self.socket.sendall(str.encode(message))
        except:
            self.eventprinter('Failed to send message!')
