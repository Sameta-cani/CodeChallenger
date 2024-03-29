import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(X)

result = [i for i in range(1, N + 1) if distance[i] == K]

if result:
    print(*result, end='\n')
else:
    print(-1)