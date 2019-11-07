def buildTree(tree,a,n):
	
	for i in range(n):
		tree[n+i]=a[i]

	for i in range(n-1,0,-1):
		tree[i]=min(tree[2*i],tree[2*i+1])




def query(tree,left,right,n):
	left+=n
	right+=n
	mi=1e9
	if left==right:
		return tree[left]
	#print(left,right,left-n,right-n)
	while left<right:

		if left&1:
			mi=min(mi,tree[left])
			left+=1
		if right&1:
			right-=1
			mi=min(mi,tree[right])
			

		left//=2
		right//=2

	return mi



def update(tree,n,pos,value):
	#no overlap
	pos+=n
	tree[pos]=value
	while pos>1:
		pos>>=1
		tree[pos]=min(tree[2*pos],tree[2*pos+1])






a=[i for i in range(10)]
n=len(a)
#print(a)
tree=[0]*(2*n)

buildTree(tree,a,n)
#print(tree)

qs=1
qe=9
r=query(tree,qs,qe+1,n)
print("minimum from",qs,"to",qe,"is=",r, "And array is-->",tree[n+1:])

update(tree,n,9,0)
#print(tree)

qs=1
qe=9
r=query(tree,qs,qe+1,n)
print("minimum from",qs,"to",qe,"is=",r, "And array is-->",tree[n+1:])


