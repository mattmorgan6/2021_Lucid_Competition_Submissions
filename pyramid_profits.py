from collections import defaultdict

# dict from person to (boss, percentage)
d = {}

r = {'Jude':0}

n_salespeople = int(input())
for i in range(n_salespeople):
    person, boss, percentage = input().split()
    percentage = float(percentage)
    d[person] = (boss, percentage)
    r[person] = 0

n_sales = int(input())
for i in range(n_sales):
    person, sale = input().split()
    sale = float(sale)

    path = []
    temp = person
    while temp != 'Jude':
        boss, percentage = d[temp]
        path.append((boss, percentage))
        temp = boss

    for boss, percentage in reversed(path):
        profit = sale * ((100 - percentage) / 100)
        r[boss] += profit
        sale = sale - profit

    r[person] += sale

output = []
for k, v in r.items():
    output.append((k, int(round(v))))

output.sort()
for k, v in output:
    print(k, v)

    


# print(d)