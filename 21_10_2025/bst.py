from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

# 9
# 10 12 13 14 15 21 22 23 24
# 10 12 L
# 10 13 R
# 13 14 L
# 13 15 R
# 14 21 L
# 14 22 R
# 15 23 L
# 15 24 R
# 14

n = int(input())
eles = input().split()
vals = list(map(int,eles))
print(vals)
nodes = {}
root = None
for v in vals:
    nodes[v] = Node(v)
    
parents = {}

for _ in range(n-1):
    p,c,d = input().split()
    p = int(p)
    c = int(c)
    
    parents[c] = p
    
    if(d=="L"):
        nodes[p].left = nodes[c]
    else:
        nodes[p].right = nodes[c]
start = int(input())


childs = set()
for node in nodes.values():
    if node.left:
        childs.add(node.left.val)
    if node.right:
        childs.add(node.right.val)
for node in nodes:
    if node not in childs:
        root = nodes[node]
print(childs)
print(root.val)


# BFS
# result = []
# dq = deque()
# dq.append(root)

# while dq:
#     popedNode = dq[0]
#     print("popedNode : ",popedNode.val)
#     if popedNode.left:
#         dq.append(popedNode.left)
#         print("popedNode left : ",popedNode.left.val)
#     if popedNode.right:
#         dq.append(popedNode.right)
#         print("popedNode right : ",popedNode.right.val)
#     print(dq)
#     po = dq.popleft()
#     print("poped : ",po)
#     print(dq)
#     result.append(po)
#     print("result : ",result)
# print(result)


# PROBLEM

tar = []
result = []
watched = []
sec = 0
dq = deque()
dq.append(start)
while dq:
    popedNode = dq[0]
    # get the parent node
    parent = parents[popedNode]
    if parent not in watched:
        dq.append(parent)
        watched.append(parent)
    # get children
    if popedNode.left:
        leftChild = popedNode.left
        if leftChild not in watched:
            dq.append(leftChild)
            watched.append(leftChild)
    if popedNode.right:
        rightChild = popedNode.right
        if rightChild not in watched:
            dq.append(rightChild)
            watched.append(rightChild)
    if rightChild not in tar:
        tar.append(rightChild)
    poped = dq.popleft()
    if poped in tar:
        sec += 1
print("sec : "+sec)
    
    
    
    

