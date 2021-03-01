# UDP sender
# Olle Bergkvist & August M Rosenqvist

from socket import *
import time

serverName = '192.168.2.4'
serverPort = 12000
sequenceNumber = 10000
sequenceNumberEnd = ";"
streamingData = 'A'*1400
endCharacters = "####"
compiledMessage = ""

# Create UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

print("Sending UDP packages to:", serverName, "\nPress Ctrl+C to stop.\n")

# Loop until keyboard interrupt (Ctrl+C)
try:
    while True:
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
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped.")
    # Close socket
    clientSocket.close()
    time.sleep(1)
