from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import socket
import sys
import rsa


#key = b'Sixteen byte key'
#data = b'secret data'


#data = input("What would you like to send?").encode('latin1')

#print(key)








def connectSend(key, data):
    sock = socket.create_connection(('localhost', 10001))
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('latin1'))
    nonce = cipher.nonce
    stored_text = bytearray(b"nonce" + nonce + b"tag" + tag + b"ciphertext" + ciphertext)
    try:

        # Send data
        print('sending "%s"' % stored_text, file=sys.stderr)
        sock.sendall(stored_text)

        amount_received = 0
        amount_expected = len(stored_text)

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print('received "%s"' % data, file=sys.stderr)

    finally:
        print('closing socket', file=sys.stderr)
        sock.close()