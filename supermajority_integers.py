from collections import defaultdict


iters = int(input().strip())

d = defaultdict(lambda: 0)

for iter in range(iters):
    i = int(input())
    d[i] += 1

# print(d)

max_num = 0

for key, value in d.items():
    if value > max_num:
        max_num = value

# print(max_num)
# print(float(max_num / iters))
# print(float(2/3))
if float(max_num / iters) > float(2/3):
    print("True")
else:
    print("False")