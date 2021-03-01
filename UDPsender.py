# UDP sender
# Olle Bergkvist

from socket import *
import time

serverName = '192.168.2.4'
serverPort = 12000
sequenceNumber = 10000
sequenceNumberEnd = ";"
streamingData = 'A'*1400
endCharacters = "####"
compiledMessage = ""

# create UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    # Increment sequence number
    sequenceNumber += 1

    # Concatenate message
    compiledMessage = str(sequenceNumber) + sequenceNumberEnd + streamingData + endCharacters

    # send sentence to socket; server and port number required
    # need to convert message from string to bytes for Python 3
    clientSocket.sendto(compiledMessage.encode(),(serverName, serverPort))

    # Wait one second before sending next package
    time.sleep(1)

# close UDP socket
clientSocket.close()
