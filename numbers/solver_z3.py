from z3 import *

with open("sample1/input1.txt") as f:
    data = f.read().strip()

with open("sample1/output1.txt") as f:
    answers = list(map(eval, f.read().strip().split("\n")))

idxs = [Int("x%d") for i in range(1, 100)]
nums = String("nums")

s = Solver()

for i in range(len(idxs)):
    s.add(1 <= idxs[i], idxs[i] <= 2)

s.add(Length(nums) == len(data))
s.add(simplify(Contains(nums, data)))
dist = []
for i in range(len(idxs)):
    dist.append(Extract(nums, sum(idxs[:i]), idxs[i]))
s.add(simplify(Distinct(dist)))

r = s.check()
if r != sat:
    print(r)
    exit()

m = s.model()
res = []
for i in range(len(xs)):
    res.append(m[xs[i]].as_long())
print("[+] found a solution")
print(res)

print("[*] compare the answer")
print(res == answers[0])
