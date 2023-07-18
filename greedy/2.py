import math
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    if min(data) < min_value :
        min_value = min(data)

result = min_value
print(result)