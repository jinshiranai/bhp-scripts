import socket

target_host = "localhost"
target_port = 9998

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host,target_port))

# Send some data
client.send(b"Sup?")#b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")

# Recieve data
response = client.recv(4096)

print(response.decode())
client.close()