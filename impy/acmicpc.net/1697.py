import Queue

n, k = [int(item) for item in raw_input().split()]
q = Queue.Queue()
visited = [False]*100001

q.put((n, 0))
visited[n] = True
while True:
    t = q.get()
    if t[0] == k:
        print t[1]
        break
    if not visited[t[0]-1]:
        q.put((t[0]-1, t[1]+1))
        visited[t[0]-1] = True
    if not visited[t[0]+1]:
        q.put((t[0]+1, t[1]+1))
        visited[t[0]+1] = True
    if 2*t[0] <=100000 and not visited[2*t[0]]:
        q.put((2*t[0], t[1]+1))
        visited[2*t[0]] = True


