import math

n = int(input())

x, y = 0, 0
dir = 0
for i in range(n):
    ch_dir, ch_deg, ch_dist = input().split()
    ch_deg, ch_dist = round(float(ch_deg)), round(float(ch_dist))
    
    if ch_dir == 'Right':
        dir -= ch_deg
    else:
        dir += ch_deg
    dir %= 360
    
    # print(dir)
    dir = math.radians(dir)
    dx = math.cos(dir) * ch_dist
    dy = math.sin(dir) * ch_dist
    x += dx
    y += dy
    a, b = round(x), round(y)
    # print(dx, dy)
    # print(x, y)
    dir = math.degrees(dir)

# now output in proper format:
mag = int(round(math.sqrt(x**2 + y**2)))

rads = math.atan2(y, x)
degs = math.degrees(rads)
degs = round(degs)

if degs < 0:
    print('Right', degs * -1, mag)
else:
    print('Left', degs, mag)

    
