import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    print(sorted(list(map(int, sys.stdin.readline().rstrip().split())), reverse=True)[2])