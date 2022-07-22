from collections import deque
import queue


n,m=map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
    
    
def bfs(x,y):
    result =0
    queue = deque()
    queue.append(x,y)
    for i in range(4):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    
    
    

