# Trapping rain water

class Solution:
    def trap(self, height):
        l = 0
        r = len(height) - 1
        maxL = maxR = ans = 0    
        while l < r:
            if height[l] < height[r]: 
                if height[l] >= maxL: maxL = height[l]
                else: ans += maxL - height[l]
                l += 1
            else: 
                if height[r] >= maxR: maxR = height[r]
                else:
                    ans += maxR - height[r]
                r -= 1          
        return ans
    

height = [0,1,0,2,1,0,1,3,2,1,2,1]
o = Solution()
print(o.trap(height))