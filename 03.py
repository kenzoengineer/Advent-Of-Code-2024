import re
def p1():
    with open("03_input.txt") as file:
        acc = 0
        for line in file:
            level = line.rstrip()
            # mul(NUMBER, NUMBER)
            matches = re.findall(r"mul\((\d+),(\d+)\)",level)
            for m in matches:
                acc += int(m[0]) * int(m[1])
    return acc

def p2():
    with open("03_input.txt") as file:
        acc = 0
        do = True
        for line in file:
            level = line.rstrip()
            # mul(NUMBER, NUMBER) or do() or don't()
            matches = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))",level)
            for m in matches:
                if m[2]:
                    do = True
                elif m[3]:
                    do = False
                else:
                    if do:
                        acc += int(m[0]) * int(m[1])

    return acc

print(p1())
print(p2())