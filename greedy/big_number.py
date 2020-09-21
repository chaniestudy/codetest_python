# 가장 큰 수 만들기

# 주어진 다양한 수의 배열에서 특정 인덱스가 K번을 초과해 더할 수 없고 M번 더해 가장 큰 수를 만드는 것

# input: 배열의 크기 N, 숫자 더해지는 횟수 M, 연속 한계 K
# input2: N개의 자연수가 주어짐. 공백으로 구분
# 조건: K는 항상 M 보다 작거나 같다.

# Output: 큰 수의 법칙의 답

# Key Approach:
# 큰 수가 유일할 경우: 받은 수 중에 가장 큰 수를 K번 더하고, 한번은 다음으로 큰수 한번 더하고 다시 K번 더함
# 큰 수가 2개 이상일 경우: 받은 수를 M번 더함
# 가장 큰 수 얼마나 더했는지 체크하고 총 얼마나 더했는지 체크해야함

# Input 받기
n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

big_num = 0

num_list.sort(reverse=True)
num_1, num_2 = num_list[0:2]

cnt_m = 0
cnt_k = 0
# if num_1 != num_2:
#     while cnt_m < m:
#         if cnt_k < k:
#             big_num += num_1
#             cnt_k += 1
#         else:
#             big_num += num_2
#             cnt_k = 0
#         cnt_m += 1
#
# else:
#     big_num = num_1 * m
#
#
# print(big_num)

# Key Approach 2:
# 반복되는 수열에 대한 파악
# M 을 K+1 로 나눈 몫만큼 반복되고 나머지 만큼 최대 수를 더해주면됨

cnt_array = int(m / (k+1))
big_num = (num_1 * k + num_2) * cnt_array
big_num += (num_1) * (m % (k+1))

print(big_num)