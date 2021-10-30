"""
NOTE: This problem is not solved due to TLE (1 second).

"""


import collections

sequence = input()
n = int(input())

stack = collections.deque()
for c in sequence:
    stack.append(c)

for i in range(n):
    count, op = input().split()
    count = int(count)
    if op.isalpha():
        i = 0
        for c in op:
            stack.insert(count + i, c)
            i += 1
    else:
        idx = count
        remove_n = int(op)
        for i in range(remove_n):
            if len(stack) > 0 and idx < len(stack) and idx >= 0:
                del stack[idx]

print(''.join(stack))




"""
Using List:
sequence = input()
n = int(input())

stack = []
for c in sequence:
    stack.append(c)

for i in range(n):
    count, op = input().split()
    count = int(count)
    if op.isalpha():
        i = 0
        for c in op:
            stack.insert(count + i, c)
            i += 1
    else:
        remove_n = int(op)
        del stack[count]

print(''.join(stack))"""