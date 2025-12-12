# container with most water

height = [1,8,6,2,5,4,8,3,7]

def mostwatercontaier(height):
    s,e = 0, len(height)-1
    water = 0
    while(s<e):
        water = max(water, (e-s)*min(height[s],height[e]))
        if height[s] <= height[e]: s+=1
        else: e-=1
    return water


print(mostwatercontaier(height))