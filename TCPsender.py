# TCP sender
# Olle Bergkvist & August M Rosenqvist

from socket import *
import time

serverName = "192.168.1.70"
serverPort = 12000
sequenceNumber = 10000
sequenceNumberEnd = ";"
streamingData = 'A'*1400
endCharacters = "####"
compiledMessage = ""

print("Sending TCP packages to:", serverName, "\nPress Ctrl+C to stop.\n")

# Loop until keyboard interrupt (Ctrl+C)
try:
    while True:
        # Create TCP socket on client to use for connecting to remote server
        clientSocket = socket(AF_INET, SOCK_STREAM)

        # Open the TCP connection
        clientSocket.connect((serverName, serverPort))

        # Increment sequence number
        sequenceNumber += 1

        # Concatenate message
        compiledMessage = str(sequenceNumber) + sequenceNumberEnd + streamingData + endCharacters

        # Send sentence to socket; server and port number required
        # Need to convert message from string to bytes for Python 3
        clientSocket.send(compiledMessage.encode())

        # Display current package ID
        print("\rCurrent package:", sequenceNumber, end='', flush=True)

        # Close TCP connection
        clientSocket.close()

        # Wait one second before sending next package
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped.")
    time.sleep(1)