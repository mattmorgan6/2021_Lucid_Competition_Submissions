cols = int(input())
order = list(map(int, input().split()))
message = input()

arr = [[] for i in range(cols)]
for i, c in enumerate(message):
    arr[i % cols].append(c)
    

for o in order:
    print(''.join(arr[o-1]), end='')