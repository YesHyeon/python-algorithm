n = input()

arr = []
for i in range(int(n)) :
    arr.append(int(input()))
    
answer = sorted(arr, reverse=True)

for i in answer:
    print(i, end=' ')
