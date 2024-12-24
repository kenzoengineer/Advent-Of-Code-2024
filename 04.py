def xmas(a,b,c,d):
    print(a,b,c,d)
    yes = a == "X" and b == "M" and c == "A" and d == "S"
    if yes:
        print("!")
    return yes
def task_1():
    grid = []
    res = 0
    with open("04_input.txt") as file:
        for line in file:
            grid.append(list(line.strip()))
    
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            row = grid[r]
            if grid[r][c] != "X":
                continue
            right = c+3 < len(row)
            left = c-3 >= 0
            down = r+3 < len(grid)
            up = r-3 >= 0
            if right:
                if xmas(grid[r][c],grid[r][c+1],grid[r][c+2],grid[r][c+3]):
                    res += 1
            if left:
                if xmas(grid[r][c],grid[r][c-1],grid[r][c-2],grid[r][c-3]):
                    res += 1
            if down:
                if xmas(grid[r][c],grid[r+1][c],grid[r+2][c],grid[r+3][c]):
                    res += 1
            if up:
                if xmas(grid[r][c],grid[r-1][c],grid[r-2][c],grid[r-3][c]):
                    res += 1
            if right and down:
                if xmas(grid[r][c], grid[r+1][c+1],grid[r+2][c+2], grid[r+3][c+3]):
                    res += 1
            if left and down:
                if xmas(grid[r][c],grid[r+1][c-1],grid[r+2][c-2],grid[r+3][c-3]):
                    res += 1
            if left and up:
                if xmas(grid[r][c],grid[r-1][c-1],grid[r-2][c-2],grid[r-3][c-3]):
                    res += 1
            if right and up:
                if xmas(grid[r][c],grid[r-1][c+1],grid[r-2][c+2],grid[r-3][c+3]):
                    res += 1
    return res

import re
def task_2():
    grid = []
    res = 0
    with open("04_input.txt") as file:
        for line in file:
            grid.append(list(line.strip()))
    for r in range(len(grid) - 2):
        for c in range(len(grid[r]) - 2):
            g = grid[r][c:c+3] + grid[r+1][c:c+3] + grid[r+2][c:c+3]
            if re.match("M.S.A.M.S","".join(g)):
                print(grid[r][c:c+3] , grid[r+1][c:c+3] , grid[r+2][c:c+3])
                res += 1
            if re.match("S.S.A.M.M","".join(g)):
                print(grid[r][c:c+3] , grid[r+1][c:c+3] , grid[r+2][c:c+3])
                res += 1
            if re.match("M.M.A.S.S","".join(g)):
                print(grid[r][c:c+3] , grid[r+1][c:c+3] , grid[r+2][c:c+3])
                res += 1
            if re.match("S.M.A.S.M","".join(g)):
                print(grid[r][c:c+3] , grid[r+1][c:c+3] , grid[r+2][c:c+3])
                res += 1
    return res
print(task_2())