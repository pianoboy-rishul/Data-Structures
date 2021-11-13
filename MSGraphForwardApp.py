##...RISHUL GHOSH...##
##...N230...##

def shortestPath(graph):
    global INF
    dist = [0] * N
    dist[N - 1] = 0
    for i in range(N - 2, -1, -1):
        dist[i] = INF
        for j in range(N):
            if graph[i][j] == INF:
                continue
            dist[i] = min(dist[i],graph[i][j] + dist[j])
    return dist[0]

N = 12
INF = 999999999999
graph = [[INF, 9, 7, 3, 2, INF, INF, INF, INF, INF, INF, INF],
         [INF, INF, INF, INF, INF, 4, 2, 1, INF, INF, INF, INF],
         [INF, INF, INF, INF, INF, 2, 7, INF, INF, INF, INF, INF],
         [INF, INF, INF, INF, INF, INF, INF, 11, INF, INF, INF, INF],
         [INF, INF, INF, INF, INF, INF, 11, 8, INF, INF, INF, INF],
         [INF, INF, INF, INF, INF, INF, INF, INF, 6, 5, INF, INF],
         [INF, INF, INF, INF, INF, INF, INF, INF, 4, 3, INF, INF],
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, 5, 6, INF],
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 4],
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 2],
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 5]]

print("=== As per given graph, the minimum distance is calculated as ===")
print("MIN DIST =",shortestPath(graph))



