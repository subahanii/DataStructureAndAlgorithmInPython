

from collections import defaultdict

class Graph:
	def __init__(self,v):
		self.graph= defaultdict(list)
		self.V=v


	def addEdge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def show(self):
		print(self.graph)


	#DisJoint Set union() and findP()

	def union(self,pt,x,y):

		xx=self.findP(pt,x)
		yy=self.findP(pt,y)

		s=pt[yy]
		pt[yy]=xx
		pt[xx]+=s


	def findP(self,pt,i):
		if pt[i]<0:
			return i
		k=i
		while 1:
			if pt[i]<0:
				pt[k]=i
				break
			i=pt[i]

		return i


	def isCycle(self):
		visit={i:False for i in range(self.V)}
		pt=[-1]*(self.V)

		for i in self.graph:
			for j in self.graph[i]:
				if visit[j]==False:
					x=self.findP(pt,i)
					y=self.findP(pt,j)
					#print(i,j,x,y,pt)
					if x==y:
						return 1

					self.union(pt,i,j)
				#print(i,j,x,y,pt)
			visit[i]=True
			#print(visit)
		return 0


g=Graph(9)


g.addEdge(1,2)

g.addEdge(3,4)

g.addEdge(5,6)
g.addEdge(7,8)
g.addEdge(2,4)
g.addEdge(2,5)
g.addEdge(1,3)
g.addEdge(6,8)
g.addEdge(5,7)

r=g.isCycle()
if r:print("Yeap! There is a cycle.")
else:print("Nope! There is no any cycle.")

#g.show()

