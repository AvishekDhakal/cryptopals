import base64

base_64_enc = ""
file_enc_text = open('./files/6.txt', 'r')
for  c in file_enc_text:
    base_64_enc = base_64_enc + c.strip()
dec_base64 = base64.b64decode(base_64_enc)


def key_size_find():
    i = 2
    first_str = ""
    second_str = ""
    while i <42:
        value_list = [k for k in dec_base64]
        required_list = [j for j in value_list[0:i*2]]
        first_split, second_split = [p for p in required_list[0:len(required_list)//2]], [q for q in required_list[len(required_list)//2::]]
        for m in first_split:
            first_str = first_str + format(m, "b").zfill(8)
        for n in second_split:
            second_str = second_str + format(n, "b").zfill(8)
        resulting_xor = bytes(int(b1) ^ int(b2) for b1,b2 in zip(first_str, second_str))
        # f = [x for x in second_str if x == '1' ]  #you can len if you want to use this 
        # f = [x for x in second_str if x == '1' ].count('1')
        f = sum(bin(byte).count("1") for byte in resulting_xor) 
        normalized_dist = f / (i)
        # print(f"The length is: {(f)}")
        # print(f"This is for keysize:{i}")
        # print(f"noramlized distanccce {normalized_dist}")
        i = i + 1      


# so the key size is 2 



first_elem = []
secon_elem = []

for i in range(0,len(dec_base64)+1,2):
    try:
        c,d = dec_base64[i], dec_base64[i+1]
        first_elem.append(c)
        secon_elem.append(d)
    except IndexError as e:
        pass
# print(first_elem)
# print(secon_elem)
xoring = b''
for y in first_elem:
    ll = format(y, '0x')
    for i in range(256):
        try:
            xoring = bytes(b1 ^ b2 for b1, b2 in zip(ll.encode("utf-8") , chr(i).encode("utf-8"))).decode("utf-8")

        except UnicodeDecodeError:
            pass




# print([i for i in dec_base64])


# what i need to do is brute the byte i got with key lenght from 2 to 40 and check the hammidng distance. and if you found the lower hamming distance you would now then know that is the key lenght.





# Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.

# Write a function to compute the edit distance/Hamming distance between two strings. The Hamming distance is just the number of differing bits. The distance between:

# this is a test    /done shit
# and
# wokka wokka!!!

# is 37. Make sure your code agrees before you proceed.  /verified

# For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.

# The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.

# Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.

# Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.
# Solve each block as if it was single-character XOR. You already have code to do this.

# For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.








