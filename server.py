import socket
import sys
import rsa

with open('private.pem', mode='rb') as privatefile:
    keydata = privatefile.read()
    
privkey = rsa.PrivateKey.load_pkcs1(b"""-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----""")

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
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
            #decrypted_message = rsa.decrypt(data, privkey)
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
        decrypted_message = rsa.decrypt(fullMessage, privkey)
        print(decrypted_message)
        connection.close()