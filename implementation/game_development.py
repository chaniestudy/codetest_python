# input: 맵 세로크기 N 가로크기 M
# input2: 캐릭터가 있는 칸의 좌표, 바라보는 방향 d
# input3: 맵이 육지인지 바다인지 알려줌
# input 조건: 게임캐릭터가 위치한 칸의 상태는 항상육지

# simulation:

# key approach:
#   왼쪽 방향의 정의: 방향값에 있어서 움직이는 path를 정의할 필요가 있음
#   이미 가본칸은 1으로 봐도 무방

# 첫째줄에 이동을 마친후 캐릭터가 방문한 칸의 수를 출력

path_list = [(0, -1), (1, 0), (0, 1), (-1, 0)]
back_list = [(-1, 0), (0, -1), (1, 0), (0, 1)]

map_list = []
rotation_count = 0
cnt = 0

n, m = map(int, input().split())
x, y, d = map(int, input().split())

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3


# map을 준비함
for k in range(n):
    map_list.append(input().split())

while True:
    print(cnt)
    if rotation_count == 4:
        nx = x + back_list[d][0]
        ny = y + back_list[d][1]
        if map_list[nx][ny] == "1":
            break
        rotation_count = 0
    else:
        nx = x + path_list[d][0]
        ny = y + path_list[d][1]
        if map_list[nx][ny] == "1":
            turn_left()
            rotation_count += 1
        else:
            map_list[nx][ny] = "1"
            x, y = nx, ny
            cnt += 1

print(cnt)