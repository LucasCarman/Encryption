from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii


with open('public.pem', mode='rb') as publicfile:
    keydata = publicfile.read()

msg = b'A message for encryption'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
print("Encrypted:", binascii.hexlify(encrypted))

decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted)

