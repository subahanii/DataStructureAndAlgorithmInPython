
#Problem Link: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/tutorial/




from collections import defaultdict as dfd

class Graph:
    def __init__(self,v):
        self.graph=dfd(list)
        self.V=v
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def show(self):
        print(self.graph)
        
    
    def dfs(self,s):
        visited={i: False for i in range(1,self.V+1)}
        
        stack=[s]
        visited[s]=True
        
        while stack:
            node=stack[-1]
            del stack[-1]
            
            for i in self.graph[node]:
                if visited[i]==False:
                    visited[i]=True
                    stack.append(i)
                    
        c=0
        for i in visited:
            if visited[i]==False:
                c+=1
        return c
        
        
        
n,m=map(int,input().split())
g=Graph(n)

for _ in range(m):
    u,v=map(int,input().split())
    
    g.addEdge(u,v)
    
s=int(input())
print(g.dfs(s))
************************INPUT*********************
10 10
8 1
8 3
7 4
7 5
2 6
10 7
2 8
10 9
2 10
5 10
2

**********OUTPUT***********
0

    
    
        
