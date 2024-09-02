def pkcs_padding(cipher):
    if len(cipher) != 16:
        cipher_byte = cipher.encode("utf-8")
        padding_number= 16- len(cipher) 
        padding_byte = padding_number.to_bytes(1, byteorder="big",signed=False)
        padded_byte = (cipher_byte+padding_byte*(16-len(cipher)))
        final_str = str(padded_byte)
    
    else:
        print(cipher)
        
    return padded_byte

Cipher_txt = "YELLOW SUBMAR"

pkcs_padding(Cipher_txt)


