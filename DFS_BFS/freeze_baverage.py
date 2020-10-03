# Input1: 얼음틀의 세로 가로 길이, N * M 주어짐
# Input2 ~ N+1: 얼음틀의 형태 주어짐 (구멍 0 비 구멍 1)

# Condition: 상하좌우로 붙어있는 경우 서로 연결되어있다고 판단. 가능한 총 아이스크림 갯수 만들기

# Output: 한번에 만들 수 있는 아이스크림 개수

# Key Approach: 특정 지점에서 상하좌우를 살피고 주변 지점중에 값이 0이면서 아직 방문하지 않았다면 해당지점 방문
# 방문 지점에서 다시 상,하,좌,우를 살피며 다시 방문을 진행하면 모든 지점 방문가능
# 방문하지 않은 지점의 수를 세야

# 최대한 멀리있는 노드까지 우선적으로 탐색하는 방

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >=n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 아래 케이스중 에러는 위 조건문에서 걸러줌
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

count = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1

print(count)

