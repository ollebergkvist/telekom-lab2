# TCP receiver
# Olle Bergkvist & August M Rosenqvist

from socket import *

serverPort = 12000
counter = 10000

# Create UDP socket and bind to specified port
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

# Activate listen on socket
serverSocket.listen(1)

print ("The TCP receiver is ready to receive.\n")

while True:
    # Read client's message and remember client's address (IP and port)
    counter += 1
    
    # server waits for incoming requests; new socket created on return
    connectionSocket, addr = serverSocket.accept() 

    # read sentence of bytes from socket sent by the client
    message = connectionSocket.recv(1024).decode()

    messageArray = message.split(";")
    sequenceNumber = int(messageArray[0])
    extractedMessage = messageArray[1]

    if counter != sequenceNumber:
        print("Wrong package order detected!")
        print("Expected ID:", counter, "Received ID:", sequenceNumber)
    else:
        print("Correct package received:", sequenceNumber)
