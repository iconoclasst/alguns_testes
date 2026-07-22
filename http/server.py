import socket
import json
import os
import sys

def verify(filename):
    try:
        with open (filename, 'r') as f:
            return True
    except:
        return False
    
def handle(message):
    req_line = message['Req-line'].split(' ')
    filename = req_line[1]

    status = '404'
    if verify(filename):
        filesize = str(os.path.getsize(filename))
        status = '200'

    response = {
        'Status': status,
        'Filesize': filesize
    }

    response_size = str(sys.getsizeof(response))

    return response, response_size

def send_file(message, conn):
    req_line = message['Req-line'].split(' ')
    filename = req_line[1]

    file = open(filename, 'rb')
    data = file.read()
    conn.send(data)


IP, PORT = 'localhost', 55000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(1)

print('Listening')
while 1:
    conn, addr = server.accept()
    print(f'Conn with {addr}')

    message = json.loads(conn.recv(1024).decode())

    response, response_size = handle(message)
    conn.send(response_size.encode())

    conn.send(json.dumps(response).encode())

    send_file(message, conn)
    

    conn.close()
server.close()