# count substring anagram

s = 'gattactat'
t = 'att'
# out = 3


def count_anagrams(s, t):
    target_length, n = len(t), len(s)
    s_s, s_t = set(), set(t)
    count = 0
    for i in range(target_length): s_s.add(s[i])
    if s_s == s_t: count += 1
    for j in range(target_length, n):
        s_s.discard(s[j-target_length])
        s_s.add(s[j])
        if s_s == s_t: count += 1
    return count

print(count_anagrams(s,t))