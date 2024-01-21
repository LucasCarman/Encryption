import socket
import sys
import rsa

def get_constants(prefix):
    """Create a dictionary mapping socket module constants to their names."""
    return dict( (getattr(socket, n), n)
                 for n in dir(socket)
                 if n.startswith(prefix)
                 )

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')
with open('public.pem', mode='rb') as publicfile:
    keydata = publicfile.read()
pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(b"""-----BEGIN PUBLIC KEY-----
MIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEAmpin9oZqtVIZ9v4165GY
2SfYULardpkFXR7XLTtuub37IC1BYtL7PrX5mSjBwtxpi45KK3uYwjzcmUoGTqLC
scgSqvWN3/ZUsrNN2ObpG3UKXvHsCOGvAXA1Dll+1+CCLiopdciMaLgmLY3rhoEV
JO8O1al0QRlZu1mrzcY54cXaYF7OSf8BrIl8d2u4kKd+Hc9I1ZljGmbKgR2MCxvj
SBYRHbwGYDN4rBkwNLiqxQrg1CT0yC3F21oGB9o2MMEh9GoHMCFqjTBk0wnzge6a
ZYf7hTygdLU6v6B5chwGFx/Yotz6gxr+PEBR0eG7RIIC4VP5ORqg2KN+mfYTlZ0i
u4oe5ekj/0GfYog16E6OeWb8LzP5dARJIkPndQu3MYH/XZtzxxWm7gvbvUZLXUaZ
G+5re1SjxbTmco0cJ2kgg5dOExxw8H0UBP2Kqg87lLhOx2CUudsTgVpsB673P7sw
JEO//phlRUy/v0x8ugboFiZgag0HR7V1G5+ISSkK2zy9AgMBAAE=
-----END PUBLIC KEY-----""")

# Create a TCP/IP socket
sock = socket.create_connection(('localhost', 10000))

print('Family  :', families[sock.family], file=sys.stderr)
print('Type    :', types[sock.type], file=sys.stderr)
print('Protocol:', protocols[sock.proto], file=sys.stderr)
print(file=sys.stderr)
message = input("What's the message?\n").encode("ascii").strip()

encrypted_message = rsa.encrypt(message, pubkey)
try:
    
    # Send data
    print('sending "%s"' % encrypted_message, file=sys.stderr)
    sock.sendall(encrypted_message)

    amount_received = 0
    amount_expected = len(encrypted_message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received "%s"' % data.decode("ascii"), file=sys.stderr)

finally:
    print('closing socket', file=sys.stderr)
    sock.close()