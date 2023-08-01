graph = {"n1": [0, 2, 0, 1, 0, 0, 0],
         "n2": [2, 0, 0, 0, 5, 0, 0],
         "n3": [0, 0, 0, 2, 4, 0, 0],
         "n4": [1, 0, 2, 0, 0, 0, 0],
         "n5": [0, 0, 0, 0, 0, 7, 5],
         "n6": [0, 0, 0, 0, 7, 0, 8],
         "n7": [0, 0, 0, 0, 5, 8, 0]}


All_nodes = graph.keys()
All_nodes = list(All_nodes)
print(All_nodes)
visitedNodes = []
unVisitedNodes = All_nodes
path = []
node_sat = input("Enter Starting node: ")
node_end = input("Enter End node: ")
while node_sat != node_end:
    min_val = []
    if (node_sat and node_end) in All_nodes:
        master = graph[node_sat]
        for i in master:
            if i > 0:
                min_val.append(i)
            visitedNodes[0] = (All_nodes[master.index(min(min_val))])
        master = visitedNodes[0]
        print(master)
    else:
        print("path not found")
        break

