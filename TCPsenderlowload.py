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

# Set timeout after 20 seconds
end_time = time.time() + 20

print("Sending TCP packages to:", serverName, "\nPress Ctrl+C to stop.\n")

# Loop until timeout
while time.time() < end_time:
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

    # Calculate time left
    time_left = round(end_time - time.time(), 2)

    # Display current package ID
    print("\rCurrent package:", sequenceNumber, "| Time left:", time_left, end='', flush=True)

    # Close TCP connection
    clientSocket.close()

    # Wait x second(s) before next package
    time.sleep(0.05)
