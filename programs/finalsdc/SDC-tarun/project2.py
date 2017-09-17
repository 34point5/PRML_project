import collections

x=0 
print(x)
file=open("table.txt","r")       #Input
input1=file.readlines()
countOnes={}

flaggedRows={k: 0 for k in range(len(input1))}


for i in range(len(input1)) :
    input1[i]=list(input1[i][:-1])  #parsing data
    size=len(input1[i])
print (input1)


flaggedColumns={k: 0 for k in range(len(input1[0]))}


print (flaggedColumns)
print(flaggedRows)

output = [0 for y in range(size)]
# for i in range(len(input1)):
# 	if (flaggedRows[i] !=1):
# 		counter=0
# 		for j in range (len(input1[i])):
# 			if(flaggedColumns[j] != 1):
# 				if input1[i][j] == '1':
# 					counter +=1
# 					index=j
# 		countOnes[i] = counter
# 		if counter==1:
# 			flaggedRows[i]=1
# 			x+=1
# 			flaggedColumns[index]=1
# 			output[index]=1

# 			for j in range(len(input1)):
# 				if(input1[j][index]== '1'):
# 					flaggedRows[j] = 1	
# 					x+=1

# 		print ("iteration-" + str(i))		

print("flaggedRows ", end = '')
print (flaggedRows)
print(flaggedColumns)
print(output)	
columnOnes={}

print("x " + str(x) + "len" + str(len(input1)))
while (sum(flaggedRows.values())!=len(input1)):
	for i in range(len(input1[0])):
		if (flaggedColumns[i] != 1):
			counter=0
			for j in range(len(input1)):
				if (flaggedRows[j]!=1):
					if(input1[j][i]=='1'):
						counter +=1
			columnOnes[i]=counter

	print("cl")
	print(columnOnes)

	sortedC = collections.OrderedDict(sorted(columnOnes.items(), key=lambda x:x[1], reverse=True))
	print(sortedC)
	value = list(sortedC.values())[0]
	print("value" + str(value))

	inv_map = {v: k for k, v in sortedC.items()}

	print (inv_map)
	print (inv_map[value])

	flaggedColumns[inv_map[value]]=1
	print(flaggedColumns)
	output[inv_map[value]]=1
	columnOnes[inv_map[value]]=0
	print (output)
	
	for f in range(len(input1)):
		if (input1[f][inv_map[value]]=='1'):
			flaggedRows[f]=1
			x+=1

	print("flagRows  " + str(flaggedRows))
	print("\n")

print("knksnsdn")			
print(flaggedRows)
print(sum(flaggedRows))
print("output" + str(output))
# answer={}
# for i in range(len(input1)):
# 	sum=0
# 	for j in range (len(input1[i])):
# 		sum += int(input1[i][j])*output[j]
# 	if sum<1:
# 		break
# 	answer[tuple(output)]='valid'	


# print (answer)
