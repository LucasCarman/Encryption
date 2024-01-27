import socket
import sys
import rsa
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import re

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10001)
print('starting up on %s port %s' % server_address, file=sys.stderr) 
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print('waiting for a connection', file=sys.stderr) 
    connection, client_address = sock.accept()
    try:
        fullMessage = bytearray(b'')
        print('connection from', client_address, file=sys.stderr)
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received "%s"' % data, file=sys.stderr)
            fullMessage += data
            if data:
                print('sending data back to the client', file=sys.stderr)
                connection.sendall(data)
            else:
                print('no more data from', client_address, file=sys.stderr)
                break       
    finally:
    # Clean up the connection
        print(fullMessage)
        data = cipher.decrypt_and_verify(ciphertext, tag)
        print(decrypted_message)
        connection.close()