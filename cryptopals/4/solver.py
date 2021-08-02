allow = set(range(0x20, 0x7f))

def score(s: bytes):
    res = 0
    for x in s:
        if x in allow:
            res += 1
    return res

with open("./4.txt") as f:
    data = f.read().strip().split("\n")
    data = [bytes.fromhex(d) for d in data]

# max_score = len(data[0])
# for c in range(0x20, 0x7f):
#     for i, d in enumerate(data):
#         m = bytes([x^c for x in d])
#         cnt = score(m)
#         if cnt >= max_score-1:
#             print(bytes([c]), i, m)
key = "5"
line = 170
print(bytes([ord(key) ^ x for x in data[line]]))
