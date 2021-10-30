n_balloons = int(input())
balls = []
for i in range(n_balloons):
    x, y, z, r = map(int, input().split())
    balls.append((x, y, z, r))


# Inclusive in range!!
def in_range(x, y, b_x, b_y, b_r):
    return (x - b_x) ** 2 + (y - b_y) ** 2 < b_r ** 2


x = 0
y = 0
for h in range(1500, -1, -1):

    for b_x, b_y, b_z, b_r in balls:
        if b_z == h:
            if in_range(x, y, b_x, b_y, b_r):

                # now move the guy!
                # print(b_x, b_y, b_z, b_r)

                dx = x - b_x
                dy = y - b_y
                mag = 1 / (dx ** 2 + dy ** 2) ** 0.5
                # print(dx, dy, mag)
                
                x = dx * mag * b_r + b_x
                y = dy * mag * b_r + b_y

                # print("bounced to", x, y)

def rd(num):
    return int(num * -1 // 1 * -1)


print(rd(x), rd(y))
                
    

