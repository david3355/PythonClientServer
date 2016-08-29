__author__ = 'Jager'
from client import Client

def eventprinter(event):
    print(event)

def msghandler(msg):
    print(msg)

client = Client('localhost', 3100, eventprinter, msghandler)
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