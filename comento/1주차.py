import time


# 삽입정렬
def insertion_sort(arr):
    for i in range(1,len(sortArr)):
        for j in range(i,0,-1):
            if sortArr[j] < sortArr[j-1]:
                sortArr[j], sortArr[j-1] = sortArr[j-1], sortArr[j]
            else:
                break

# 머지정렬
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복 
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

sortArr = list(range(1, 1000001))
reverseSortArr = list(range(1000000, 0, -1))
data3 = [i for i in range(1, 10000001, 100)]

# 시간 측정
start_time = time.time()
insertion_sort(sortArr)
print("삽입 정렬 sortArr:", time.time() - start_time)

start_time = time.time()
insertion_sort(reverseSortArr)
print("삽입 정렬 reverseSortArr:", time.time() - start_time)

start_time = time.time()
insertion_sort(data3)
print("삽입 정렬 data3:", time.time() - start_time)

sortArr = list(range(1, 1000001))
reverseSortArr = list(range(1000000, 0, -1))
data3 = [i for i in range(1, 10000001, 100)]

# 시간 측정
start_time = time.time()
merge_sort(sortArr)
print("머지 정렬 sortArr:", time.time() - start_time)

start_time = time.time()
merge_sort(reverseSortArr)
print("머지 정렬 reverseSortArr:", time.time() - start_time)

start_time = time.time()
merge_sort(data3)
print("머지 정렬 data3:", time.time() - start_time)

# sortArr = list(range(1, 1000001))
# reverseSortArr = list(range(1000000, 0, -1))
# data3 = [i for i in range(1, 10000001, 100)]

# # 시간 측정
# start_time = time.time()
# quick_sort(sortArr, 0, len(sortArr))
# print("삽입 정렬 1:", time.time() - start_time)

# start_time = time.time()
# quick_sort(reverseSortArr, 0, len(sortArr))
# print("삽입 정렬 2:", time.time() - start_time)

# start_time = time.time()
# quick_sort(data3, 0, len(sortArr))
# print("삽입 정렬 3:", time.time() - start_time)


print(insertion_sort(reverseSortArr))

    