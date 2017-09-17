import numpy as np

print ("Enter number of variabes") #number of variables the function is dependent on
numbers = input()
print ("enter splitting order")
order=list(input())	
print (order)			  
print("Enter the expression")      
file=open("input.txt","r")        #complements are represented with capital letters
input1=file.readlines()


for i in range(len(input1)):
	input1[i]=list(input1[i][:-1])
print(input1)
input1 = np.array(input1,dtype='object')
print(input1)	
input2=input1.copy()
print(input2)

for i in range(len(input1)):
	for j in range(len(order)):
		
		if order[j] in input1[i]:     	
			input2[i][j]='01'
		print (ord(order[j]))	
		if chr(ord(order[j]) - 32) in input1[i]:
			input2[i][j]='10'
		 
			
print(input1)
print (input2)	