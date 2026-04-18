class Solution:
    def absl(self,x):
        if x>=0:return x
        else:return -x

    def reverseInt(self,n):
        if n == 0: return n
        rev = ''
        while n != 0:
            last = n%10
            n = n//10
            rev += f'{last}'
        return int(rev)
    
    def mirrorDistance(self, n):
        return self.absl(n-self.reverseInt(n))


o = Solution()


print(o.mirrorDistance(25))
print(o.mirrorDistance(10))
print(o.mirrorDistance(7))

