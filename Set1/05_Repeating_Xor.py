line1 = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
print(len(line1))
line1_byte = line1.encode("utf-8")
key = "ICE".encode("utf-8")
print(f"key len: {len(key)}")
print(f"text1len: {len(line1_byte)}")
match_key = b''
while len(match_key)  <= len(line1_byte):
    for i in key:
        match_key = match_key + chr(i).encode("utf-8")
        
cipher1 = bytes(b1 ^ b2 for b1,b2 in zip(line1_byte,match_key))
print(cipher1.hex())
