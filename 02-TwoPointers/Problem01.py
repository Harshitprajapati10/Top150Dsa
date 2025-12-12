# 125 valid palindrome

def isValidPalindrome(st):
    s,e = 0, len(st)-1
    print(st[e])
    while(s<e):
        if not st[s].isalnum():s+=1
        elif not st[e].isalnum():e-=1
        elif st[s].lower() != st[e].lower(): return False
        else:
            s += 1
            e -= 1
    return True
        


print(isValidPalindrome("A man, a plan, a canal: Panama"))
