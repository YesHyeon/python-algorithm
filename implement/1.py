n = int(input())
# m = list(map(str, input().split(' ')))
m = input().split(' ')

x,y = 1, 1

# L R U D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# types = ['L', 'R', 'U', 'D']

for a in m :
    if a == 'L' :
        nx = x + dx[0]
        ny = y + dy[0]
    elif a == 'R' :
        nx = x + dx[1]
        ny = y + dy[1]
    elif a == 'U' :
        nx = x + dx[2]
        ny = y + dy[2]
    elif a == 'D' :
        nx = x + dx[3]
        ny = y + dy[3]
    
    if nx > 0 and ny > 0 and nx < n+1 and ny < n+1 :
        x, y = nx, ny
        
print(x,y)



