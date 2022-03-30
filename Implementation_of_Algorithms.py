star_galactica = { "Ajan Kloss": {"Bahu": 15, "Bothawui": 11, "Bespin and Hoth": 20},
                   "Bahu": {"Ach-To" : 6, "Endor and Kef Bir": 4},
                   "Bothawui": {"Cantanice": 12, "Kessel": 5},
                   "Bespin and Hoth": {"Crait": 5, "D'Qar": 6},
                   "Ach-To": {"Cantanica": 22},
                   "Endor and Kef Bir": {"Sullust": 10, "Ring of Kafrene": 5},
                   "D'Qar": {"Sullust": 2, "Naboo": 2}}


def dfs(visited, graph, node):
    visited = set() # Set to keep track of visited nodes.
    if node not in visited:
        print ("dfs",node)
        if node == target:
            print("Found:",node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)