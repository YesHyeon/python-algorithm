# 예제문제
# 10 7
# 1 3 5 9 11 13 15 17 19 21
n, k = map(int, input().split())

array = list(map(int, input().split()))

# 재귀함수 이진탐색
def binary(arr, target, start, end) :
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if arr[mid] == target:
        return mid
    
    if arr[mid] > target :
        return binary(arr, target, start, mid-1)
        
    else :
        return binary(arr, target, mid+1, end)
    
result = binary(array, k, 0, n-1)

if result == None :
    print('숫자를 찾을 수 없습니다.')
else : 
    print(result+1)
