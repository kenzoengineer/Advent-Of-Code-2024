def safe_level(level):
    prev = None
    inc = None
    for _curr in level:
        curr = int(_curr)
        # set up first number
        if not prev:
            prev = curr
            continue
        # set up delta with second number
        if inc == None:
            inc = curr - prev > 0
        # check if direction has changed
        else:
            if (curr - prev > 0 )!= inc:
                return False
            
        # failure cases
        if abs(curr - prev) > 3:
            return False
        if curr == prev:
            return False

        prev = curr
    return True

def p1():
    with open("02_input.txt") as file:
        res = 0
        for line in file:
            level = line.rstrip().split(" ")
            if safe_level(level):
                res += 1

        return res
    
def p2():
    with open("02_input.txt") as file:
        res = 0
        for line in file:
            level = line.rstrip().split(" ")
            if safe_level(level):
                res += 1
            # see if we can remove an element to make it safe
            else:
                for i in range(len(level)):
                    x = level.copy()
                    x.pop(i)
                    if safe_level(x):
                        res += 1
                        break
        return res
    
print(p1())
print(p2())