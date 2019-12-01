#Problem link:
https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/distinct-integers-in-range-66eca44b/

def buildTree(tree1,tree2,a,b,n):
	for i in range(n):
		tree1[i+n]=1<<(a[i]-1)
		tree2[n+i]=1<<(b[i]-1)

	for i in range(n-1,0,-1):
		tree1[i]=tree1[2*i]|tree1[2*i+1]
		tree2[i]=tree2[2*i]|tree2[2*i+1]



def query1(tree1,left,right,n):
	left+=n
	right+=n
	ans=0
	while left<right:
		if left&1:
			ans=ans|tree1[left]
			left+=1
		if right&1:
			right-=1
			ans|=tree1[right]

		left//=2
		right//=2

	return ans


def query2(tree2,left,right,n):
	left+=n
	right+=n
	ans=0
	while left<right:
		if left&1:
			ans=ans|tree2[left]
			left+=1
		if right&1:
			right-=1
			ans|=tree2[right]
		left//=2
		right//=2

	return ans





n=int(input())

a=list(map(int,input().split()))
b=list(map(int,input().split()))
q=int(input())
tree1=[0]*(2*n)
tree2=[0]*(2*n)
#print(tree1,tree2)
buildTree(tree1,tree2,a,b,n)
#print(tree1,tree2)

for _ in range(q):
	l1,r1,l2,r2=map(int,input().split())
	r=query1(tree1,l1-1,r1,n)
	rr=query2(tree2,l2-1,r2,n)
# 	print(r,rr,r|rr)
# 	r|=rr
	print(bin(r|rr).count('1'))



