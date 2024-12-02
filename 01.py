import heapq

class Day01:
    _hleft = []
    _hright = []
    
    def __init__(self, f):
        self._hleft = []
        self._hright = []
        with open(f) as file:
            for line in file:
                a, b = line.rstrip().split("   ")
                heapq.heappush(self._hleft, int(a))
                heapq.heappush(self._hright, int(b))

    def part_1(self):
        hleft, hright = self._hleft.copy(), self._hright.copy()
        accum = 0
        while hleft:
            a = heapq.heappop(hleft)
            b = heapq.heappop(hright)
            accum += abs(a - b)

        return accum
    
    def part_2(self):
        hleft, hright = self._hleft.copy(), self._hright.copy()
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

print(Day01("01_input.txt").part_1())
print(Day01("01_input.txt").part_2())