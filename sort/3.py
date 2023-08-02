a = int(input())

array = []

for i in range(a):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))
    
print(array)

def sortScore(data) :
    return data[1]

array.sort(key = sortScore)

for i in array :
    print(i[0], end = ' ')