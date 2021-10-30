n = int(input())

houses = list(map(int, input().split()))
# scares = []
# for i, s_i in enumerate(s):
#     scares.append((s_i, i))
# scares.sort()

output = 0

adj = []
for i in range(n):
    r = list(map(int, input().split()))
    adj.append(r)

visited = set()

a = 0
while a < n:
    possible = []
    for i in range(n):
        if i in visited:
            continue

        neighs = 0
        for j, z in enumerate(adj[i]):
            if z == 1 and j in visited:
                neighs += houses[j]

        possible.append((houses[i] + neighs, i))

    possible.sort()
    print(possible)
    # break
    temp_score, k = possible[-1]
    # print(temp_score, k)
    visited.add(k)
    output += temp_score
    a += 1



print(output)