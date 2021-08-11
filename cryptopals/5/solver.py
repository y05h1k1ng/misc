data = b"""Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""

key = b"ICE"

ans = """0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"""


def enc(s, key):
    res = b""
    for i in range(len(s)):
        res += bytes([s[i] ^ key[i%len(key)]])
    return res

ans = bytes.fromhex("".join(ans.split("\n")))

c = enc(data, key)
print(c == ans)
print(c)
print(ans)
