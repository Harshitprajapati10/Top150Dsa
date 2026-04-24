# furthest point from origin

moves = "L_RL__R"


def furthestdistance(moves):
    cR, cL = 0,0
    selected = 'L'
    # count max char
    for move in moves:
        if move == 'L': cL += 1
        elif move == 'R': cR += 1
    if cR > cL: selected = 'R'

    # put max char in place of _
    s = list(moves)
    for i in range(len(s)):
        if s[i] == '_': s[i] = selected
    moves = ''.join(s)
    
    dist = 0
    for move in moves:
        if move == 'L': dist -= 1
        else: dist += 1
    return abs(dist)

        

print(furthestdistance(moves))
print(furthestdistance('_R__LL_'))
print(furthestdistance('_______'))
