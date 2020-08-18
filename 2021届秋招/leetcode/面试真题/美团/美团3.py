def union_find(nodes, edges):
    father = [0] * len(nodes)  # 记录父节点
    for node in nodes:  # 初始化为本身
        father[node] = node

    for edge in edges:  # 标记父节点
        head = edge[0]
        tail = edge[1]
        father[tail] = head

    for node in nodes:
        while True:  # 循环，直到找到根节点
            father_of_node = father[node]
            if father_of_node != father[father_of_node]:
                father[node] = father[father_of_node]
            else:  # 如果该节点的父节点与其爷爷节点相同，
                break  # 则说明找到了根节点

    L = {}
    for i, f in enumerate(father):
        L[f] = []
    for i, f in enumerate(father):
        L[f].append(i)

    return L
import sys

n, m = map(int, sys.stdin.readline().split())
data=[]
node=set()
for _ in range(m):
    a,b=map(int, sys.stdin.readline().split())
    data.append([a,b])
    node.add(a)
    node.add(b)
res=union_find(node,data)
print(len(res))
print(res)