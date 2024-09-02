import string
import base64
d = open("./files/4.txt","r")
counter = 1
j = 0
counter = 1
for i in d:

    f = i.strip()
    k = bytes.fromhex(f)    # you know what i mistook? it was something related to i took value from file but forget to use it in bytes.
    # print(counter,f)  #the encrypted ones are correctly printed
    for j in range(0,256):
        c = chr(j)
        # print(counter, c) #the loop sis also good all the ascii are getting looped
        encoded_j = c.encode("utf-8")
        encoded_j = encoded_j * len(i)
        try:
            xoring = bytes(b1 ^ b2 for b1,b2 in zip(k, encoded_j)).decode("utf-8")
            d = list(chr(i) for i in range(97,122)) + [' ']
            common_chars = set("".join(d))  
            common_count = sum(1 for char in xoring if char in common_chars)
            score = common_count / len(xoring)
            if score >= 0.8:
                print(f" {k} {chr(j)} {score} {xoring}")
        except UnicodeDecodeError:
            pass

