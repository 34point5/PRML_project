import numpy as np
import sdctree
from graphviz import Digraph


#print ("Enter number of variabes") #number of variables the function is dependent on
#numbers = input()
print ("enter splitting order")
order=list(input()) 
numbers = len(order)                  
file=open("input.txt","r")        #complements are represented with capital letters
input1=file.readlines()

for i in range(len(input1)) :
    input1[i]=list(input1[i][:-1])
#print(input1)
input1 = np.array(input1,dtype='object')
print(len(input1))
#out_i = [None]*int(numbers)
#output = [out_i]*len(input1)
print(int(numbers))
output = [[0 for y in range(int(numbers))] for x in range(len(input1))] 

print(input1)   
print(output)

for i in range(len(input1)) :
    for j in range(len(order)):
        
        for k in range(len(input1[i])):

            if  order[j] == input1[i][k]:
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

dot = Digraph(comment='OBDD')
dot_robdd = Digraph(comment='ROBDD')
mytree = sdctree.tree()
for counter,x in enumerate(order):
    
    mytree.add(x,counter, output)  #add all the individual nodes
height = counter +1

mytree.add('final',height, output) #add final nodes


mytree.apply()                     #change the cover values 


mytree.setfinal(mytree.gethead())  #sets a 1 or 0 to the final nodes
mytree.callshow(dot)               #display the tree
print ('\n\nITE: \n')
mytree.ite(mytree.gethead())
print ('\n')
mytree.firstloop(height)            #call for reduction
#mytree.callshow(dot)            
#print(dot.source)
mytree.callshow_robdd(dot_robdd)   #display the tree
print(dot_robdd.source)
dot.render('test-output/OBDD', view=True)       #render full
dot_robdd.render('ROBDD', view=True) #render reduced







