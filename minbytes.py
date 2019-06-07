import math
s=int(input())
a=math.log10(s)/math.log10(2)
if math.ceil(a)==math.floor(a):
	print(0)
else:
	r=(s-1)//2
	u=r*2
	print(s-u)

