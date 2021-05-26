# 問5: 2~4全部満たすコードを作成する
print(list(map(lambda i:"FB" if i/15 == i//15 else "B" if i/5 == i//5 else "F" if i/3 == i//3 else i,  range(1, int(input("n : ")) + 1))))
