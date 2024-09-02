# Write a function that takes two equal-length buffers and produces their XOR combination.

# If your function works properly, then when you feed it the string:

# 1c0111001f010100061a024b53535009181c
# ... after hex decoding, and when XOR'd against:

# 686974207468652062756c6c277320657965
# ... should produce:

# 746865206b696420646f6e277420706c6179
import base64


def fixdxor():
    hex1 = "1c0111001f010100061a024b53535009181c"
    hex2 = "686974207468652062756c6c277320657965"
    xoring = bytes(b1 ^ b2 for b1, b2 in zip(bytes.fromhex(hex1), bytes.fromhex(hex2)))
    print(xoring)
    final_ouptut = base64.b16encode((xoring))    #this encoding schemes here only supports bytes like object.
    print(final_ouptut)

fixdxor()