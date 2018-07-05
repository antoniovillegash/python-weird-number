n = int(input())
m =n%2
if m==0 and(2<=n<=5 or n>20):
	print("Not Weird")
elif m!=0 or 6<=n<=20 :
	print("Weird")
	
