# has substing anagram

s = 'greyhounds'
# t = 'gre'
# t = 'hoy'
t = "avs"
# out: True , yho is in s

def has_substr_anagram(s, t):
    target_length, n = len(t), len(s)
    s_s, s_t = set(), set(t)
    for i in range(target_length): s_s.add(s[i])
    if s_s == s_t: return True
    for j in range(target_length, n):
        s_s.add(s[j])
        s_s.discard(s[j-target_length])
        if s_s == s_t: return True
    return False

print(has_substr_anagram(s,t))