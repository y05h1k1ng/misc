from base64 import b64encode

# hex to base64
s = 0x49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
ans =  b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

x = b64encode(bytes.fromhex(hex(s)[2:]))
if x == ans:
    print("ok")
else:
    print("ng")
