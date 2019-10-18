import random
a=random.randrange(1,10)
aa=3
while aa>0:
	guess=int(input())
	if guess==a:
		print("you win")
	else:
		aa-=1
		if aa==0:
			print('you lose')
		else:
			print("now you have only "+str(aa)+' chances')
		

		print("you have chances")
	
i=1
while i<10:
	a=input("enter the no.")
	if i%2==0:
		print(i,"you are riyaz khan")
	elif i%3==0:
		print(i,"you are deepak")
	i=i+1

else:
	print("bye bye")
i
	
		

