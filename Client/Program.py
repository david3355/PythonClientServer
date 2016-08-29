__author__ = 'Jager'
from client import Client

def eventprinter(event):
    print(event)

def msghandler(msg):
    print(msg)

host = 'localhost'
port = 3100
inp = input('Remote address of server (default: {}): '.format(host))
if(inp != ""): host = inp
inp = input('Remote port of server (default: {}): '.format(port))
if(inp != ""): port = int(port)
client = Client(host, port, eventprinter, msghandler)
client.connect_to_server()
reading = True
while (reading):
    try:
        read = input('User: ')
        if(read != 'exit'): client.send(read)
        else:
            client.disconnect_from_server()
            reading = False
    except:
        print('Failed to send message!')

print('Client stopped!')