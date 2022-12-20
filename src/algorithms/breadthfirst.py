def bfs(graph, startNode):
    visited = []
    queue = []
    
    visited.append(startNode)
    queue.append(startNode)
    
    while queue:
        s = queue.pop(0)
        print(s, end = " ")
        
        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)