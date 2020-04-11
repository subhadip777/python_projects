#thought is everything
def jump(x):
	if x==0:
		return 1
	else:
		k=pow(10,x)+jump(x-1)
		return k

n=int(input())
for i in range(n):
	print(pow(jump(i),2))