# input: 행 갯수 N, 열 갯수 M이 주어짐
# input2: 둘째 줄 부터 (N X M)의 행렬이 주어짐

# Output: 게임 규칙에 맞는 숫자 출력

# Key Approach:
# 입력 받을 때 동시에 최솟값 받기.
# 최솟값의 최대값 갱신

n, m = map(int, input().split())

num_max = 0

for k in range(n):
    num_list = list(map(int, input().split()))
    num_list.sort()
    if num_list[0] > num_max:
        num_max = num_list[0]

print(num_max)