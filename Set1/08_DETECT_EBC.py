# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# f = open('files/output.txt','r')
# KEY = "YELLOW SUBMARINE".encode("utf-8")
# put_list = []
# counter = 16
# match_counter = 0
# #so what i am tryna do is convert the hex into bytes and then break them into 16 bytes meaning a block (cause aes operated on block of 16 ) 
# for i in f:
#     c = bytes.fromhex(i.strip())    #so what i have to do is make the ten splits of each and compare them with everyother.
#     for k in range(0,10):
#         first_end = counter*k
#         first = c[first_end:(k+1)*16]
#         put_list.append(first)
#     # print(put_list)
#     for j in put_list:
#         try:
#             for m in range(0, len(put_list)):
#                 if put_list[m] == j:
#                     # print(f"Checking with {j}")
#                     match_counter = match_counter + 1
#                     # print(match_counter)
#                 if match_counter >=2:
#                         print("Match Found")
#                         print(f"{put_list[m]}")
#             match_counter = 0 
#         except IndexError as e:
#             pass
 
#now what i need to do is compare each other form same line first i guess then move towards different if i cant find the same line ones.

#this works but needs some improvements la.





f = open('files/output.txt')

for i in f:
    c = bytes.fromhex(i)
    print(c)
    print(" ")
print(len(c))
