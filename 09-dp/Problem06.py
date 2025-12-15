# 1899 merge triplets to form targets

triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]
target = [5,5,5]

def mergeTriplets(triplets, target):
    a = b = c = 0
    for x, y, z in triplets:
        if x > target[0] or y > target[1] or z > target[2]:
            continue
        a = max(a, x)
        b = max(b, y)
        c = max(c, z)
    return a == target[0] and b == target[1] and c == target[2]


print(mergeTriplets(triplets, target))