from collections import deque

# 필요한 변수는 graph, visited, V(시작값))

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

# 정점으로 해결
# graph2 = [[] for _ in range(N + 1)]

# for _ in range(M):
#     a, b = map(int, input().split())
#     graph2[a].append(b)
#     graph2[b].append(a)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
    
visited1 = [False] * (N + 1) # 방문기록 남기기

def dfs(V) :
    visited1[V] = True
    print(V, end=" ")
    for i in range(1, N + 1) :
        # 방문 안했고 graph[V][i]이 True이면
        if not visited1[i] and graph[V][i]:
            dfs(i)

dfs(V)

        

