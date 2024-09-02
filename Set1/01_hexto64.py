import base64
hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
raw_bytes = bytes.fromhex(hex)
print(raw_bytes)
encoded = base64.b64encode(raw_bytes)
print(encoded)

# never ever do operation on hex or base64 you need to convert it in raw bytes and then do anythiny you like any operation of crypto.


# Base64: Not a Number System

# Base64 is not a numerical system in the traditional sense like binary or decimal. It's a binary-to-text encoding scheme.
# It's designed to represent binary data (which could be anything from images to text to executable code) using a limited set of 64 printable characters.
# How Base64 Works:

# Chunking: The input binary data is divided into groups of 6 bits.
# Mapping: Each 6-bit group is mapped to a specific character from the Base64 alphabet. This alphabet includes:
# Uppercase letters (A-Z)
# Lowercase letters (a-z)
# Digits (0-9)
# Two special characters (+ and /)
# Padding: If the input data length isn't divisible by 3 bytes (24 bits), padding characters (=) are added to the end to make the encoded length a multiple of 4