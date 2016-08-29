__author__ = 'Jager'
from threading import Thread


class Connection:
    def __init__(self, conn, address, msghandler, disconnect_callback):
        self.conn = conn
        self.address = address
        self.msghandler = msghandler
        self.disconnect_callback = disconnect_callback


    def send(self, message):
        self.conn.sendall(str.encode(message))


    def close(self):
        self.connopen = False
        self.conn.close()
        self.disconnect_callback(self)


    def reader(self):
        while (self.connopen):
            try:
                data = self.conn.recv(2048).decode('utf-8')
                self.processmsg(data)
            except:
                self.close()

    def send(self, message):
        try:
            self.conn.sendall(str.encode(message))
        except:
            self.eventprinter('Failed to send message!')

    def start_reader(self):
        self.connopen = True
        self.t_reader = Thread(None, self.reader)
        self.t_reader.start()

    def processmsg(self, data):
        self.msghandler(self, data)
        self.send('Reply: ' + data)


    def __eq__(self, other):
        return self.conn == other.conn

