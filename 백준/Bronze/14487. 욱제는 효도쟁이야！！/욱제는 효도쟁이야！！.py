import sys

input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))

print(sum(array) - max(array))