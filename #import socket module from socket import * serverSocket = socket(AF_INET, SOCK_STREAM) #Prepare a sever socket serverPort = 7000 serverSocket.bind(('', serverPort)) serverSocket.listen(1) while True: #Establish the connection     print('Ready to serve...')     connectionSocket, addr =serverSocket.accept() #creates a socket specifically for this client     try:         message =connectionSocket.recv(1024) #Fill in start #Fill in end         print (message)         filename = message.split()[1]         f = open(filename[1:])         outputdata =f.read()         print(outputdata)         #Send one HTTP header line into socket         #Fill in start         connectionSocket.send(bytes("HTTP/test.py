#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverPort = 7000
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while True:
#Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =serverSocket.accept() #creates a socket specifically for this client
    try:
        message =connectionSocket.recv(1024) #Fill in start #Fill in end
        print (message)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata =f.read()
        print(outputdata)
        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n", "utf-8"))
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(bytes(outputdata[i], "utf-8"))
        connectionSocket.close()
        print("file received")
    except IOError:
    
        #Send response message for file not found
        #Fill in start
        connectionSocket.send(bytes("\n404 File Not Found\n", "utf-8")) #sends an error message to be printed on the page
        #Fill in end
        #Close client socket
        connectionSocket.close()
        #Fill in start
        #Fill in end
    serverSocket.close()
