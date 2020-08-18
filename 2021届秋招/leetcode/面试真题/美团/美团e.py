n = int(input())
child_graph = {}
for _ in range(n):
    a, b = input().split()
    if a==b:
        continue
    if a not in child_graph:
        child_graph[a] = b
    else:
        child_graph[a] += "#" + b
visited = []
trace = []
has_circle = False
res = []
temp=0
def dfs(node_index):
    global has_circle
    global res
    global temp
    if (node_index in visited):
        if (node_index in trace):
            has_circle = True
            temp += 1
            return
        return
    visited.append(node_index)
    trace.append(node_index)
    if (node_index != ''):
        children = child_graph[node_index].split('#')
        for child in children:
            dfs(child)
    trace.pop()

for k,v in child_graph.items():
    dfs(k)
    res.append(temp)
if (has_circle == False):
    print(0)
else:
    print(max(res))

"""
8
beijing beijing
beijing nanjing
nanjing guangzhou
guangzhou shanghai
shanghai beijing
beijing fuzhou
fuzhou beijing
beijing wuhan
"""
