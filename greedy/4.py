n, m = map(int, input().split())

"""
n을 m으로 나눈 나머지가 0이면 나누기
만약 안나눠진다면 -1을 계속해서 빼나가기
"""

count = 0

while True :
    if n == 1 :
        break;
    
    if n % m == 0 :
        n = n // m
        count += 1
        
    else :
        n -= 1
        count += 1
        
    
    
print(count)