N = int(input())

d = [0] * (N + 1)

for i in range(2, N + 1):
    d[i] = d[i - 1] + 1  # 현재 수에서 1을 빼는 경우
    if i % 2 == 0:  # 현재 수가 2로 나누어 떨어지는 경우
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:  # 현재 수가 3으로 나누어 떨어지는 경우
        d[i] = min(d[i], d[i // 3] + 1)

print(d[N])