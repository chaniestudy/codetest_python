# input: 자연수 N과 K가 주어짐
# Output: N이 1이될때 까지 수행해야하는 횟수의 최솟값

# Key Approach:
# N이 K의 제곱수로 표현하고 나머지 를 더하면됨

n, k = map(int, input().split())

number = 0
count = 0

while True:
    number = (n // k) * k
    count += n - number
    n  = number
    if n < k:
        break
    count += 1
    n //= k

count += n - 1

print(count)