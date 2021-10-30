n_rows = int(input())
n_cols = int(input())
grid = []
output = grid.copy()
for r in range(n_rows):
    lst = list(map(int, input().split()))
    grid.append(lst)



def dfs(grid, output, r, c, count):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dy, dx in dirs:
        y, x = r + dy, c + dx
        if 0 <= y < n_rows and 0 <= x < n_cols:
            if count < grid[y][x]:
                grid[y][x] = count
                dfs(grid, output, y, x, count + 1)        
    

for r in range(n_rows):
    for c in range(n_cols):
        if grid[r][c] == 0:
            dfs(grid, output, r, c, 1)

# output
for r in range(n_rows):
    for c in range(n_cols):
        print(grid[r][c], end=" ")
    print()
            