n, m = map(int, input().split())

graph = []
result = 0;

for a in range(n) :
    graph.append(list(map(int, input())))
    
def dfs(x,y) :
    if x < 0 or x>= n or y < 0 or y >= m :
        return False
    
    if graph[x][y] == 0 :
        graph[x][y] = 1 # 방문처리
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    
    return False

for i in range(n) :
    for z in range(m):
        if dfs(i, z) == True :
            result += 1

print(result)