from graphviz import Digraph
dot = Digraph(comment='OBDD')

print ("enter splitting order")
order=list(input())	
numbers = len(order)			      
file=open("input.txt","r")        #complements are represented with capital letters
input1=file.readlines()

for i in range(len(input1)) :
	input1[i]=list(input1[i][:-1])

input1 = np.array(input1,dtype='object')
print(len(input1))
print(int(numbers))
output = [[0 for y in range(int(numbers))] for x in range(len(input1))] 

print(input1)	
print(output)

for i in range(len(input1)) :
	for j in range(len(order)):
		for k in range(len(input1[i])):

			if	order[j] == input1[i][k]:
				output[i][j] = '01'
				print (output)

				if(k+1<len(input1[i])):
					if input1[i][k+1] == "'":
						output[i][j] = '10'

				break

			if k == len(input1[i])-1:
				output[i][j] = '11'	


print(len(output))
print(output[0])
print(output[1])

output = np.array(output,dtype='object')

dot.render('test-output/round-table.gv', view=True)