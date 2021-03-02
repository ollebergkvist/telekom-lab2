# UDP sender
# Olle Bergkvist & August M Rosenqvist

from socket import *
import time
t_end = time.time() + 21

serverName = '192.168.2.4'
serverPort = 12000
sequenceNumber = 10000
sequenceNumberEnd = ";"
streamingData = 'A'*1400
endCharacters = "####"
compiledMessage = ""

# Create UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

print("Sending UDP packages to:", serverName)

# Loop over 20 seconds time
while time.time() < t_end:
    # Increment sequence number
    sequenceNumber += 1

    # Concatenate message
    compiledMessage = str(sequenceNumber) + sequenceNumberEnd + streamingData + endCharacters

    # Send sentence to socket; server and port number required
    # Need to convert message from string to bytes for Python 3
    clientSocket.sendto(compiledMessage.encode(), (serverName, serverPort))

    # Display current package ID
    print("\rCurrent package:", sequenceNumber, end='', flush=True)

    # Wait one second before sending next package
    time.sleep(0.025)
