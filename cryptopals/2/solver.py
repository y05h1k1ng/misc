def xor(a, b):
    return bytes([i^j for i, j in zip(a, b)])

s = 0x1c0111001f010100061a024b53535009181c
a = bytes.fromhex(hex(s)[2:])
t = 0x686974207468652062756c6c277320657965
b = bytes.fromhex(hex(t)[2:])

ans = "746865206b696420646f6e277420706c6179"

if xor(a, b).hex() == ans:
    print("ok")
else:
    print("ng")
