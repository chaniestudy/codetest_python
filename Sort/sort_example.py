array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


# 선택정렬
## 가장 작은 것을 선택한다 해서 선택 정렬
## 시간 복잡도 O(N^2)
for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프
    # python은 간단 구현 가능하나 C++에서는 스와프 변수가 있어야함
print(array)

# 삽입정렬
## 특정한 데이터를 적절한 위치에 삽입한다는 의미에서 삽입정렬
## 정렬이 이뤄진 원소는 항상 오름차순을 유지하고 있어서
## 삽입될 데이터보다 작은 데이터를 만나면 그 위치에서 멈추면됨
## 시간 복잡도 O(N^2), 최선의 경우 O(N)

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
# 거의 정렬 되어있을 경우 삽입 정렬을 사용
print(array)

# 퀵정렬
## 피벗을 선택하고, 피벗 값을 기준으로 정렬
## 가장 많이 쓰는 것은 첫번째 원소를 피벗으로 함
## 두 값이 엇갈리면 작은 데이터와 피벗위치를 변경
## 분할 이후 반복함
## 재귀함수로 작성을 많이하고, 종료 조건은 현재 리스트의 개수가 1일 때이다.
## 시간 복잡도 평균 O(NlogN) 최악 O(N^2)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start  # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while (left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while (left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while (right > start and array[right] >= array[pivot]):
            right -= 1
        if (left > right):  # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)

# 재귀함수를 활용해 직관적으로 짠 코드
def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# 이미 정렬 된 경우 매우 느리게 동작한다. 삽입정렬과 반대
print(quick_sort(array))


# 계수정렬
## 특정한 조건이 부합할 때 만 사용할 수 있지만 매우 빠른 정렬 알고리즘
### 데이터 크기가 한정되어있고, 데이터의 크기가 많이 중복되어 있을수록 유리함
## 최악의 경우에도 수행시간 O(N+K) 값을 보장 (모든 양의 정수로 된 데이터 개수 N, 최대값 K)
## 가장 작은 데이터에서 가장 큰 데이터 까지의 크기의 리스트를 만든다
## 출현 빈도를 그 리스트에 기록한다. 그 횟수만큼 인덱스 출력

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

# python 기본함수
## 병합정렬 기반임
## 시간 복잡도 O(NlogN) 보장
## 문제 유형 1) 정렬 라이브러리로 풀수 있는 문제 2) 정렬 알고리즘 원리를 물어봄 3) 더빠른 정렬이 필요함

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)

array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)