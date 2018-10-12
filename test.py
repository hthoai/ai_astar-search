with open('input.txt') as f:
    N = int(next(f))
    start_x, start_y = [int(x)for x in next(f).split()]
    goal_x, goal_y = [int(x)for x in next(f).split()]
    grid = [[int(x)for x in line.split()]for line in f]

print(N)
print(start_x, start_y)
print(goal_x, goal_y)

for i in range(N):
    for j in range(N):
        print(grid[i][j], end='')
    print()
