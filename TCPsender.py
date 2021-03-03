# UDP sender
# Olle Bergkvist & August M Rosenqvist

from socket import *
import time

serverName = 'localhost'
serverPort = 12000
sequenceNumber = 10000
sequenceNumberEnd = ";"
streamingData = 'A'*1400
endCharacters = "####"
compiledMessage = ""

# create TCP socket on client to use for connecting to remote server
clientSocket = socket(AF_INET, SOCK_STREAM)

# open the TCP connection
clientSocket.connect((serverName, serverPort))

print("Sending TCP packages to:", serverName, "\nPress Ctrl+C to stop.\n")

# Loop until keyboard interrupt (Ctrl+C)
try:
    while True:
        # Increment sequence number
        sequenceNumber += 1

        # Concatenate message
        compiledMessage = str(sequenceNumber) + sequenceNumberEnd + streamingData + endCharacters

        # Send sentence to socket; server and port number required
        # Need to convert message from string to bytes for Python 3
        clientSocket.send(compiledMessage.encode(), (serverName, serverPort))

        # Display current package ID
        print("\rCurrent package:", sequenceNumber, end='', flush=True)

        # Wait one second before sending next package
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped.")
    # Close socket
    clientSocket.close()
    time.sleep(1)