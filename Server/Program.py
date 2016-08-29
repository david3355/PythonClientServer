__author__ = 'Jager'
from server import Server

def eventprinter(event):
    print(event)

server = Server(eventprinter)
server.start_server()

print('Server is running...')
input('Press a key to stop server!\n')
server.stop_server()
print('Server is stopped!')

