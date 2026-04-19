# Multi source flood fill


n = 3
m = 3
sources = [[0,0,1],[2,2,2]]

def construct_graph(r,c,sources):
    grid = [[0 for _ in range(r)] for _ in range(c)]
    for i in range(len(sources)):
        grid[sources[i][0]][sources[i][1]] = sources[i][2]
    return grid

def dfs(grid):
    r,c = len(grid), len(grid[0])
    print(r,c)



def colorGrid(n, m, sources):
    sources.sort(key=lambda x: -x[2])
    A = [[0] * m for i in range(n)]
    for i,j,v in sources:
        A[i][j] = v
    for i,j,v in sources:
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            x = i + di
            y = j + dj
            if 0 <= x < n and 0 <= y < m and A[x][y] == 0:
                A[x][y] = v
                sources.append([x,y,v])
    return A

grid = colorGrid(n,m,sources)
print(grid)