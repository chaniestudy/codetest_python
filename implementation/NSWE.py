# input: 첫째줄 공간 크기 N, 둘째줄 이동 계획서 내용
# output: 도착지
# Condition: 공간 밖의 움직임은 무시됨

# Key Approach
# 하나씩 받아오면서 무시할것은 무시하기

n = int(input())
dir_list = input().split()
# x= 1; y = 1
#
# for dir in dir_list:
#     if dir == "U":
#         if x > 1:
#             x -= 1
#     elif dir == "D":
#         if x < n:
#             x += 1
#     elif dir == "L":
#         if y > 1:
#             y -= 1
#     elif dir == "R":
#         if y < n:
#             y += 1
#
# print(("%d %d")%(x, y))

# Answer

x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dir_types = ['L', 'R', 'U', 'D']

for dir in dir_list:
    nx = x + dx[(dir_types.index(dir))]
    ny = y + dy[(dir_types.index(dir))]

    if nx < 1 or nx > n or ny < 1 or ny >n:
        continue

    x, y = nx, ny

print(x, y)
