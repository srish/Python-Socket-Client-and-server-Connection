import socket

HOST = 'localhost'   #The remote host
PORT = 1890          #The same port as used by server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('Hello World')

data = s.recv(1024)
s.close()

print 'Received ', repr(data)