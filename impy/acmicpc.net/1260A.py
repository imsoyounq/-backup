import Queue

n, m, v = [int(item) for item in raw_input().split()]
graph = []
visited = [False] * n

for _ in range(n):
    graph.append([0] * n)

for _ in range(m):
    a, b = [int(item) for item in raw_input().split()]
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1


def dfs(a):
    print a+1,
    global visited, graph
    visited[a] = True
    for idx, item in enumerate(graph[a]):
        if item > 0 and not visited[idx]:
            dfs(idx)

dfs(v-1)
print ''

visited = [False] * n
q = Queue.Queue()
q.put(v-1)
visited[v-1] = True
while not q.empty():
    t = q.get()
    print t+1,
    for idx, item in enumerate(graph[t]):
        if item > 0 and not visited[idx]:
            q.put(idx)
            visited[idx] = True
