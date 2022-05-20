

# FAIL~
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        n = len(stations)
        stations.sort()
        curr_pos = 0
        curr_fuel = startFuel
        fl = 0
        cnt = 0
        i = 0

        while target - curr_pos > curr_fuel:
            fl = 0
            for j in range(n-1, i-1, -1):
                st_pos = stations[j][0]
                st_fuel = stations[j][1]

                if curr_fuel - st_pos >= 0:
                    curr_fuel -= (st_pos - curr_pos)
                    curr_fuel += st_fuel
                    curr_pos = st_pos
                    i = j
                    fl = 1
                    cnt += 1
                    #print(i, st_pos, st_fuel, curr_fuel)
                    break

            if fl == 0:
                return -1
        return cnt


target = 100
startFuel = 10
stations = [[10, 60], [20, 30], [30, 30], [60, 40]]
s = Solution()
res = s.minRefuelStops(target, startFuel, stations)

print(res)


