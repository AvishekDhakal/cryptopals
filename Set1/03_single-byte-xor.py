import base64

hexstr = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
hex_to_byte = bytes.fromhex(hexstr)
print((hex_to_byte))
byte_list = []
for i in range(0,256):
    c = chr(i)
    encoded_i = c.encode("utf-8")
    encoded_i = encoded_i * len(hex_to_byte)
    byte_list.append(encoded_i)
    for x in byte_list:
        xoring = bytes(b1^ b2 for b1, b2 in zip(hex_to_byte ,x))
    print((f"{i} {chr(i)}---->{xoring}"))





