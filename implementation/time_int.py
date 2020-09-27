# input: 정수 입력 n (0<= n <= 23)
# output: 00시 00분 00초 부터 n시 59분 59초까지 모든 시각중에서 3이 하나라도 포함되는 모든 경우의 수

# Key Approach:
# 시간에 3이 없는 경우 -> 60*60 - (0~59 까지 3이 안들어가는 횟수) * (0~59 까지 3이 안들어가는 횟수)
# 시간에 3이 있는 경우 -> 60*60

# n까지의 숫자에 3이 몇개 들어가는 지 체크해서 계산

n = int(input())

time_not_three = 0
n_three = 0

# for k in range(60):
#     if list(str(k)).count("3") == 0:
#         time_not_three += 1
#
# for k in range(n + 1):
#     if list(str(k)).count("3") != 0:
#         n_three += 1
#
# ans = (n+1) * (60 ** 2) - (n + 1 - n_three) * (time_not_three ** 2)
#
#
# print(ans)

# ANSWER

for k in range(60):
    if list(str(k)).count("3") == 0:
        time_not_three += 1
    else:
        if k < n:
            n_three += 1

ans = (n+1) * (60 ** 2) - (n + 1 - n_three) * (time_not_three ** 2)



print(ans)