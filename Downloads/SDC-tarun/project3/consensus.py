import numpy as np
import collections
def logical_and (A,B):
	
	if A=='00' or B=='00':
			output1='00'
	elif A=='01' and B=='01':
			output1='01'
	elif A=='01' and B=='10':
			output1='00'
	elif A=='10' and B=='10':
			output1='10'
	elif A=='10' and B=='01':
			output1='00'
	elif A=='01' and B=='11':
			output1='01'
	elif A=='11' and B=='01':
			output1='01'
	elif A=='10' and B=='11':
			output1='10'
	elif A=='11' and B=='10':
			output1='10'
	elif A=='11' and B=='11':
			output1='11'

	return output1

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    def contents(self):
    	return self.items

def logical_or (A,B):
	if A=='01' and B=='01':
			output2='01'
	elif A=='01' and B=='10':
			output2='11'
	elif A=='10' and B=='10':
			output2='10'
	elif A=='10' and B=='01':
			output2='11'
	elif A=='01' and B=='11':
			output2='11'
	elif A=='11' and B=='01':
			output2='11'
	elif A=='10' and B=='11':
			output2='11'
	elif A=='11' and B=='10':
			output2='11'
	elif A=='11' and B=='11':
			output2='11'
	elif A=='00' :
			output2=B
	elif B=='00':
			output2=A


	return output2

def logical_not (A):
	if A=='00':
			output2='11'
	elif A=='01' :
			output2='10'
	elif A=='10':
			output2='01'
	elif A=='11' :
			output2='00'
	return output2


def consensus (list1,list2):

	if len(list1) == len(list2):

		output = [[0 for y in range(len(list1))] for x in range(len(list1))]
		for i in range(len(list1)):
			for j in range(len(list2)):
				if i==j:

					output[i][j]=logical_or(list1[j],list2[j])
				else:
					output[i][j]=logical_and(list1[j],list2[j])
		return output

	else:
		return


def cofactor (list1,list2):
	flag=0
	
	#print (result)
	if(list1 is None or list2 is None):
		return None
	else:
		result=[0 for x in range(len(list1))]	
		for i in range(len(list1)):
			if logical_and(list1[i],list2[i])=='00':
				flag=1
				#print(flag)
				break
		if flag==1:
			return
		else:
			for i in range(len(list1)):
			
				result[i]=logical_or(list1[i],logical_not(list2[i]))
			return list(result)


def sharp (list1,list2):
	if len(list1) == len(list2):

		output = [[0 for y in range(len(list1))] for x in range(len(list1))]

		for i in range(len(list1)):
			for j in range(len(list1)):
				if i == j:
					output[i][j] = logical_and(list1[j],logical_not(list2[i]))
				else:
					output[i][j] = list1[j]

		return output

	else:
		return

def disjoint_sharp(list1,list2):
	if len(list1) == len(list2):

		output = [[0 for y in range(len(list1))] for x in range(len(list1))]

		for i in range(len(list1)):
			for j in range(len(list1)):
				if i == j:
					output[i][j] = logical_and(list1[j],logical_not(list2[i]))
				elif i>j:
					output[i][j] = logical_and(list1[j],list2[j])
				else:
					output[i][j] = list1[j]

		return output

	else:
		return




def select_tautology(filepath):
	file=open(filepath,"r")
	data=file.readlines()
	dict={}
	q=Queue()
	for i in range(len(data)):
		data[i]=data[i][:-1]
	input1 = [[0 for y in range(int(len(data[0])/2))] for x in range(len(data))]		
	for i in range(len(data)):	
		input1[i]=[data[i][j:j+2] for j in range(0, len(data[i]), 2)]	
	
	for j in range(len(input1[0])):
		count=0
		for i in range(len(input1)):
			if input1[i][j]!='11':
				count+=1
		dict[j]=count	
	#print(dict)	
	sortedC = collections.OrderedDict(sorted(dict.items(), key=lambda x:x[1], reverse=True))
	#print(sortedC)
	order=list(sortedC.keys())
	#print(order)
	list2=list(input1)
	list3=list(input1)
	q.enqueue(input1)
	for j in range(len(order)):
		list1=list(q.dequeue())
		
		print(list1)
		k1 =['11' for y in range(len(input1[j]))]
		k2 =['11' for y in range(len(input1[j]))]
		k1[order[j]]='01'
		k2[order[j]]='10'
		
		print(k1)
		print(k2)
		for i in range(len(input1)):
			list2[i]=(cofactor(list1[i],k1))
			
			#	flag1=1
			#	break
			list3[i]=(cofactor(list1[i],k2))
			#if list3[i]==['11','11','11']:
			#	flag2=1
			#	break

		#if flag1==0:	
		k3 =['11' for y in range(len(input1[j]))]

		if not(k3 in list(list2)):
			q.enqueue(list(list2))
		if not(k3 in list(list3)):
			q.enqueue(list(list3))


		print(q.contents())
	if(q.isEmpty()):
		return 1
	else :
		return 0




list1=['11','11']
list2=['01','01']

ans=select_tautology("input.txt")
print(ans)
#consensus=disjoint_sharp(list1,list2)

#print (consensus)
#print(cofactor(list1,list2))