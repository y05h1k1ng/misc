from base64 import b64decode

with open("./6.txt") as f:
    data = f.read().strip().split("\n") # b64(repeat(key, plain))
