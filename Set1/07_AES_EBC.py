from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


import base64
file = open('./files/7.txt','r')
c = ""
for i in file:
    c += i.strip()

base64_decoded = base64.b64decode(c)
# cprint(base64_decoded)


def fdecrypter():
    KEY = "YELLOW SUBMARINE".encode("utf-8")
    cipher = Cipher(algorithms.AES(KEY), modes.ECB())
    print(type(cipher))
    decryptor = cipher.decryptor()
    print(type(decryptor))
    dec_text = decryptor.update(base64_decoded) + decryptor.finalize()
    print(dec_text)

fdecrypter()