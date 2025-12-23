from collections import deque
n = int(input())
deq = deque()
deq.append("1")
for a in range(1,n+1):
    poped = deq.popleft()
    print(f"{a} => {poped}")
    deq.append(poped+"0")
    deq.append(poped+"1")
