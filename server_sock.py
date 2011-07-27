import socket

HOST = 'localhost'   #The remote host
PORT = 1890          #The same port as used by server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connected By', addr
while 1:
 	data = conn.recv(1024)
	if not data : break
	conn.send(data)

conn.close()
