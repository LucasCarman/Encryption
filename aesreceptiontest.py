from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import re
import socket
import sys

#nonce_regex = "/(?<=nonce).+(?=tag)/"
#tag_regex = "(?<=tag).+(?=ciphertext)"
#cipher_regex = "(?<=ciphertext).+"
#
#message = b'nonce\x7fCLi\x1dt\xef\xeco\x9c\x0c8.\xecNAtag\x85\x17\x19&\xee\x92}\x19\x10Y\x97\x9e\xc76m\xd8ciphertext\xf8c\xcaC\x88\x1c\xe5%F\x7f\xaf'
#
#nonce = re.findall(r'(?<=nonce).+(?=tag)', message.decode('latin1'))
#tag = re.findall(r'(?<=tag).+(?=ciphertext)', message.decode('latin1'))
#ciphertext = re.findall(r'(?<=ciphertext).+', message.decode('latin1'))
#
#nonce = nonce[0]
#tag = tag[0]
#ciphertext = ciphertext[0] 
#print(ciphertext)
##print(nonce[0].encode('latin1'))
##print(tag[0].encode('latin1'))
##print(ciphertext[0].encode('latin1'))


key = b'Sixteen byte key'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print('starting up on %s port %s' % server_address, file=sys.stderr) 
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print('waiting for a connection', file=sys.stderr) 
    connection, client_address = sock.accept()
    try:
        message = bytearray(b'')
        print('connection from', client_address, file=sys.stderr)
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received "%s"' % data, file=sys.stderr)
            message += data
            if data:
                print('sending data back to the client', file=sys.stderr)
                connection.sendall(data)
            else:
                print('no more data from', client_address, file=sys.stderr)
                break       
    finally:
        nonce = re.findall(r'(?<=nonce).+(?=tag)', message.decode('latin1'))
        tag = re.findall(r'(?<=tag).+(?=ciphertext)', message.decode('latin1'))
        ciphertext = re.findall(r'(?<=ciphertext).+', message.decode('latin1'))

        nonce = nonce[0]
        tag = tag[0]
        ciphertext = ciphertext[0] 
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce.encode('latin1'))
        try:    
            plaintext = cipher.decrypt_and_verify(ciphertext.encode('latin1'), tag.encode('latin1'))


            print("The message is authentic:", plaintext)

        except ValueError:

            print("Key incorrect or message corrupted")
            # Clean up the connection
        connection.close()




