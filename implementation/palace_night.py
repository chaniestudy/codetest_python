# input1: 8*8에서 나이트가 현재 위치한 곳의 좌표
# output: 나이트가 이동할 수 있는 경우의 수
# 조건: 1) 수평 두칸 이동 수직 한칸 이동 2) 수직 두칸 이동 수평 한칸 이동

# Key Approach
#   - 가능한 경우의 수에 대한 리스트업
#   - 두스텝의 이동 중 하나라도 안되면 안됨
#   - 수평 두칸 가능? -> 수직 한칸 가능?
#   - 수직 두칸 가능? -> 수직 한칸 가능?

loc = input()
x, y = int(loc[1]), int(ord(loc[0])) - int(ord('a'))+ 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

cnt = 0

for step in steps:
    nx = x + step[0]
    ny = y + step[1]

    if nx >= 1 and ny <= 8 and ny >= 1 and nx <= 8:
        cnt +=1

print(cnt)






