#!/usr/bin/python3

num=int(input("Total no. of inputs: "))
j=0

while(j<num) :
	input("Please enter the elements of matrix: ")
	j=j+1

def fun(num):
	i=2
	flag=0

	while(i<num) :
		if (num%i==0) :
			print("matrix possible: ")
			print ((i, int(num/i)))
			flag=1
		i=i+1

	if (flag==0):
		print("No matrix can be formed!")
		input("Please enter one more number: ")
		print("Possible dimensions of matrix with your no. of inputs:")
		fun(num+1)
	return;
fun(num)
	

