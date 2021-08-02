s = 0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
s = bytes.fromhex(hex(s)[2:])

# for c in range(0x20, 0x7f):
#     print(bytes([c]), bytes([c^x for x in s]))
key = "X"
print(bytes([ord(key)^x for x in s]))
