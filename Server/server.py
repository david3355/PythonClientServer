__author__ = 'Jager'
import socket
from connection import Connection
from threading import Thread

class Server:
    def __init__(self, eventprinter, host='localhost', port=3100):
        self.socket = socket.socket()
        self.host = host
        self.port = port
        self.eventprinter = eventprinter
        self.connections = []


    def start_server(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        self.waiter = Thread(None, self.wait_for_clients)
        self.serverruns = True
        self.waiter.start()
        self.eventprinter('Server is listening on port {} ({}) - machine: {}'.format(self.port, self.host, socket.gethostname()))


    def stop_server(self):
        self.serverruns = False
        self.socket.close()
        self.stop_connections()


    def wait_for_clients(self):
        while (self.serverruns):
            try:
                c, addr = self.socket.accept()
                self.add_connection(c, addr)
                self.eventprinter('Connection established: {}'.format(addr))
            except:
                if(self.serverruns): self.eventprinter('Failed to add new connection')

    def add_connection(self, connection, addr):
        c = Connection(connection, addr, self.conn_msghandler, self.connection_closed)
        self.connections.append(c)
        c.start_reader()

    def connection_closed(self, connection):
        if (connection in  self.connections):
            self.connections.remove(connection)
            self.eventprinter('Connection {} closed'.format(connection.address))


    def conn_msghandler(self, connection, msg):
        print('{}: {}'.format(connection.address, msg))

    def stop_connections(self):
        for conn in self.connections:
            conn.close()
        self.connections.clear()