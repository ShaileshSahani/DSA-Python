n = [1, 2, 3, 4, 5]
visited = [False for i in n]
print(visited)
for i in range(len(n)):
    visited[i] = True
print(visited)