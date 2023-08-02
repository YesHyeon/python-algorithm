n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(n,k,a,b)

a.sort()
b.sort(reverse=True)
count = 0

for i in range(n):
    if count == k :
        break

    if a[i] < b[i] :
        a[i], b[i] = b[i], a[i]
        count += 1
    else :
        break


