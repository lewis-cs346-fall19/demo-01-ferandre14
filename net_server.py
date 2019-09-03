import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #initialize socket
addr = ("localhost", 15556) #declare address and port
sock.bind(addr) #server binds to address and port (client does not bind to address)

sock.listen(5) #buffer in case connection fails--> number indicates # of failed connections allowed

msg = ''

(connectedSock, clientAddress) = sock.accept() #accepts connection, returns new socket (new socket= connectedSock)

while (True):
    try:
        msg = connectedSock.recv(1024).decode() #decode msg from client 
        print('Received message: '+msg)
    except(ConnectionAbortedError): #if socket hits end of data stream
        print('End of received message, closing socket.')
        connectedSock.close()
    reply = 'I got the mesage: '+msg
    connectedSock.sendall(reply.encode()) #send message back to client 
