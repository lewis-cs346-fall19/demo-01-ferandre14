import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 15556)
sock.bind(addr)

sock.listen(5)

msg = ''

(connectedSock, clientAddress) = sock.accept()

while (True):
    try:
        msg = connectedSock.recv(1024).decode()
        print('Received message: '+msg)
    except(ConnectionAbortedError):
        print('End of received message, closing socket.')
        connectedSock.close()
    reply = 'I got the mesage: '+msg
    connectedSock.sendall(reply.encode())
