import heapq

def p1():
    hleft = []
    hright = []
    with open("01_input.txt") as file:
        for line in file:
            a, b = line.rstrip().split("   ")
            heapq.heappush(hleft, int(a))
            heapq.heappush(hright, int(b))
    accum = 0
    while hleft:
        a = heapq.heappop(hleft)
        b = heapq.heappop(hright)
        accum += abs(a - b)

    return accum

def p2():
    hleft = []
    hright = []
    with open("01_input.txt") as file:
        for line in file:
            a, b = line.rstrip().split("   ")
            heapq.heappush(hleft, int(a))
            heapq.heappush(hright, int(b))
    accum = 0
    while hleft:
        if not hright:
            return accum

        curr_left = heapq.heappop(hleft)
        curr_right = hright[0]
        simularity = 0
        while curr_right and curr_right <= curr_left:
            if curr_right == curr_left:
                simularity += 1
            heapq.heappop(hright)
            curr_right = hright[0]
        accum += curr_left * simularity
    
    return accum

print(p1())
print(p2())