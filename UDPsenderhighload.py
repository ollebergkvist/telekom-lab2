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

# Set timeout after 20 seconds
end_time = time.time() + 20

print("Sending UDP packages to:", serverName)

# Loop until timeout
while time.time() < end_time:
    # Increment sequence number
    sequenceNumber += 1

    # Concatenate message
    compiledMessage = str(sequenceNumber) + sequenceNumberEnd + streamingData + endCharacters

    # Send sentence to socket; server and port number required
    # Need to convert message from string to bytes for Python 3
    clientSocket.sendto(compiledMessage.encode(), (serverName, serverPort))

    # Calculate time left
    time_left = round(end_time - time.time(), 2)

    # Display current package ID
    print("\rCurrent package:", sequenceNumber, "| Time left:", time_left, end='', flush=True)

    # Wait x second(s) before next package
    time.sleep(0.019)