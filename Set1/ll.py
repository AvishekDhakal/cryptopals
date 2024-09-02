# a = ord('b')
# z = ord('y')
# ab = b'01111010'
# az = b'01100001'

# # ab = bin(a)
# # az = bin(z)
# # print(ab,az)
# # bin1 = b'01100010'
# # bin2 = b'01111001'
# c = bytes(b1 ^ b2 for b1, b2 in zip(ab,az))
# # c = bytes(b1 ^ b2 for b1,b2 in zip(bin1,bin2))
# print(c)
# print ()
# # d = 00011011

# hexstr = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
# key = b'\x00\x00\x00\x01\x01\x00\x01\x01'
# hex_to_byte = bytes.fromhex(hexstr)

# c = bytes(b1 ^ b2 for b1, b2 in zip(hex_to_byte,key))
# print(c)

# hexstr = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

# hex_to_byte = b'{ZB\x15A]TA\x15A]P\x15ETGAL\x15\\F\x15_@XE\\[R?'
# key1 = b"5"
# key2 = b"x"
# # while len(key1) % len(hex_to_byte) != 0:
# key1 = key1 * len(hex_to_byte)
# print(key1)
# c = bytes(b1 ^ b2 for b1, b2 in zip(hex_to_byte,key1)).decode("utf-8")
# print(c)



#str to hex:

# c = "Now that the party is jumping"
# hexv = c.encode("utf-8").hex()
# print(len(hexv))
# print(type(hexv))
# dex = bytes.fromhex(hexv)
# print(dex)





c = "this is a test".encode("utf-8")
d = "wokka wokka!!!".encode("utf-8")
f = ""
c = bytes(b1 ^ b2 for b1, b2 in zip(c,d))
for i in c:
    f = f + format(i,'b')
print(f)
# f = str(format(i, 'b'))
counter = 0
for i in f:
    if i == '1':
        counter = counter + 1

print(counter)