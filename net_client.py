import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("localhost", 15555)
sock.connect(addr)
msg =''
#for i in range(100):
#    msg += str(i)+'\n'
while (True):
    msg = input('Enter message to send to server: ')
    sock.sendall(msg.encode())
    print('Sent message to server, waiting for reply')
    newMsg = sock.recv(1024).decode()
    print(newMsg)

