# UDP receiver
# Olle Bergkvist

from socket import *
serverPort = 12000
counter = 10000

# create UDP socket and bind to specified port
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print ("The UDP receiver is ready to recieve")

while True:
    # read client's message and remember client's address (IP and port)
    counter + 1
    message, clientAddress = serverSocket.recvfrom(2048)
    message.decode()
    messageArray = message.split(",")
    sequenceNumber = messageArray[0]
    extractedMessage = messageArray[1]

    if counter != sequenceNumber:
        print ("Wrong package order detected!")
        print ("Correct sequence number: " + counter)
        print ("Received sequence number: " + sequenceNumber)
        print ("Data stream: " + extractedMessage)