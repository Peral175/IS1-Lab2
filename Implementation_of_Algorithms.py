def dfs(visited, graph, node):
    visited = set() # Set to keep track of visited nodes.
    if node not in visited:
        print ("dfs",node)
        if node == target:
            print("Found:",node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)