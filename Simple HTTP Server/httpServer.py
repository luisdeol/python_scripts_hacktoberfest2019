import socket
from HTMLParser import HTMLParser

indexFile = open('index.html','r')
index = indexFile.read()

page404File = open('page404.html','r')
page404 = page404File.read()

# server host and port definition
HOST = '' # server ip (empty)
PORT = 8080 # server port

# create a socket with IPv4 (AF_INET) using TCP (SOCK_STREAM)
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# allow addres and port reutilization
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# binds ip server and port
listen_socket.bind((HOST, PORT))

# "listen" requests
listen_socket.listen(1)

# print that the server is ready
print 'HTTP sever HTTP waiting connection on %s ...' % PORT

while True:
    # waits new connections
    client_connection, client_address = listen_socket.accept()
    # .recv receives the data sended by a client through the socket
    request = client_connection.recv(1024)
    # prints the message sended by the client
    print request
    print "GET / HTTP/1.1"
    print (request == "GET / HTTP/1.1")
    # server answer declaration
    if(request == "GET / HTTP/1.1"):
		http_response = index
    else:
		http_response = page404
	
   
    # server returns what was requested by the client (in this case, it's a generic response)
    client_connection.send(http_response)
    # close the connection
    client_connection.close()

# close the socket
listen_socket.close()
