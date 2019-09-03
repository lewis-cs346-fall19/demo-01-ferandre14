import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #initialize socket
addr = ("localhost", 15556) #declare address and port of connection 
sock.connect(addr) #connect to address and port
msg =''


while (True): #continue to accept replies with while loop 
    msg = input('Enter message to send to server: ')
    sock.sendall(msg.encode()) #send message to server
    print('Sent message to server, waiting for reply')
    newMsg = sock.recv(1024).decode() #decode reply
    print(newMsg) #output reply from server 


