# 問4: 1行のコードを作成する
print(["FB" if i%15 == 0 else "B" if i%5 == 0 else "F" if i%3 == 0 else i for i in range(1, int(input("n : ")) + 1)])
