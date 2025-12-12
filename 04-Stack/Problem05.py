#853 car fleet

class Solution:
    def carFleet(self, target, position, speed):
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        fleets = 1
        prevTime = (target - pair[0][0]) / pair[0][1]
        for i in range(1, len(pair)):
            currCar = pair[i]
            currTime = (target - currCar[0]) / currCar[1]
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime
        return fleets

o = Solution()
target = 100
position = [0,2,4]
speed = [4,2,1]
print(o.carFleet(target, position, speed))