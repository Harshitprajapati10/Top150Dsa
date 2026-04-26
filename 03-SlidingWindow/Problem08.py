# longest unique substring
 
# longest substring with unique charcters

from collections import Counter

s = 'abcabcqbb'
#out :4 , abcq

def longest_unique_substring(s):
    start, longest = 0,0
    window_counter = Counter()
    for end in range(0, len(s)):
        leading_char = s[end]
        window_counter[leading_char] += 1
    
        while window_counter[leading_char] > 1:
            trailing_char = s[start]
            window_counter[trailing_char] -= 1
            start += 1
        longest = max(end-start+1, longest)
    return longest

print(longest_unique_substring(s))