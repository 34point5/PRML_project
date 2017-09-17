import numpy as np
class Node:
    def __init__(self,initvalue,initlvl,initdata):
        self.data = initdata
        self.value= initvalue
        self.level = initlvl
        self.lchild = None
        self.rchild = None
        self.logic = None
        self.id = None
    def getData(self):
        return self.data
    def getValue(self):
        return self.value
    def getlChild(self):
        return self.lchild
    def getrChild(self):
        return self.rchild
    def getlogic(self):
        return self.logic
    def getId(self):
        return self.id
    def getlvl(self):
        return self.level




    def setData(self,newdata):
        self.data = newdata
    def setlChild(self,newdata):
        self.lchild = newdata
    def setrChild(self,newdata):
        self.rchild = newdata
    def setValue(self,newdata):
        self.value = newdata
    def setLogic(self,newdata):
        self.logic = newdata
    def setId(self,newdata):
        self.id = newdata
    def setlvl(self,newdata):
        self.level = newdata
    
class tree:

    def __init__(self):
        self.head = None
       
    
    def gethead(self):
        return self.head
    def isEmpty(self):
        return self.head == None
    def split(self,node,value,level,array,counter):
        if(node.getlChild()!=None):
            self.split(node.getlChild(),value,level,array,counter)
            self.split(node.getrChild(),value,level,array,counter)
        else:
            
            newNode = Node(value+str(counter[0]),level,array.copy())
            node.setlChild(newNode)
            counter[0] = counter[0] + 1
        
            newNode2 = Node(value+str(counter[0]),level,array.copy())
            node.setrChild(newNode2)
            counter[0] = counter[0] + 1



    def add(self,value,level,array):
        counter = [0]
        if (self.head == None):
            newNode = Node(value + str(counter[0]),level,array)
            self.head = newNode
        else:

            self.split(self.head,value,level,array,counter)

    def callshow(self,dot):
        if(self.head!=None):
            self.show(self.head,dot)
    def show(self,node,dot):
        if(node != None):
            if(node.getlogic() != None ):
                dot.node(node.getValue(),str(node.getlogic()), shape = 'box')
            else:
                dot.node(node.getValue(),node.getValue()[:-1])
            if(node.getlChild() != None):
                dot.edge(node.getValue(),node.getlChild().getValue(),'0')
                dot.edge(node.getValue(),node.getrChild().getValue(),'1')
            print("Value: %s"%node.getValue())
            print("Data: %s"%node.getData())
            if(node.getId() != None):
                print("Id: %s"%node.getId())
            if(node.getValue() == 'final'):
                print("Logic: %s"%node.getlogic())
            print("\n")
            
            self.show(node.getlChild(),dot)
            self.show(node.getrChild(),dot)
    def callshow_robdd(self, dot):
        if(self.head!=None):
            self.show_robdd(self.head, dot)
    def show_robdd(self,node,dot):
        if(node != None):
            if(node.getlogic() != None ):
                dot.node(str(node.getId()),str(node.getlogic()), shape = 'box')
            else:
                dot.node(str(node.getId()),node.getValue()[:-1])

            if(node.getlChild() != None):
                dot.edge(str(node.getId()),str(node.getlChild().getId()),'0')
                dot.edge(str(node.getId()),str(node.getrChild().getId()),'1')
                        
            self.show_robdd(node.getlChild(),dot)
            self.show_robdd(node.getrChild(),dot)

    def apply(self):
        if(self.head != None):
            self.appl(self.head.getlChild(),0)
            self.appr(self.head.getrChild(),0)
        else:
            print("tree is empty")
    def childdatachangel(self,node,index):
        if(node!=None):
            temp = node.getData()
            for x in range(0, len(temp)):
                if(temp[x][index]=='01'):
                    temp[x][index] = '00'
                if(temp[x][index]=='10'):
                    temp[x][index] = '11'
            node.setData(temp)
            self.childdatachangel(node.getlChild(),index)
            self.childdatachangel(node.getrChild(),index)

    def childdatachanger(self,node,index):
        if(node!=None):
            temp = node.getData()
            for x in range(0, len(temp)):
                if(temp[x][index]=='01'):
                    temp[x][index] = '11'
                if(temp[x][index]=='10'):
                    temp[x][index] = '00'
            node.setData(temp)
            self.childdatachanger(node.getlChild(),index)
            self.childdatachanger(node.getrChild(),index)


    def appl(self,node,index):
        if(node!= None):

            temp = node.getData()

            for x in range(0, len(temp)):
                if(temp[x][index]=='01'):
                    temp[x][index] = '00'
                if(temp[x][index]=='10'):
                    temp[x][index] = '11'
            node.setData(temp)
            self.childdatachangel(node.getlChild(),index)
            self.childdatachangel(node.getrChild(),index)

            
            self.appl(node.getlChild(),index+1)
            self.appr(node.getrChild(),index+1)

    def appr(self,node,index):
        if(node!= None):
            temp = node.getData()
            
            #print(temp)
            for x in range(0, len(temp)):
                if(temp[x][index]=='01'):
                    temp[x][index] = '11'
                if(temp[x][index]=='10'):
                    temp[x][index] = '00'
            node.setData(temp)
            self.childdatachanger(node.getlChild(),index)
            self.childdatachanger(node.getrChild(),index)

            #print(temp)

            #self.callshow()
            self.appl(node.getlChild(),index+1)
            self.appr(node.getrChild(),index+1)
    def setfinal(self,node):
        if(node != None):
            if 'final' in node.getValue():
                finalcheck = 0
                for x in node.getData():
                    check = 1
                    for y in x:
                        if y == '00':
                            check = 0
                            break
                    if(check == 1):
                        finalcheck = 1
                if(finalcheck == 1):
                    node.setLogic(1)
                    node.setId(2)
                else:
                    node.setLogic(0)
                    node.setId(1)

            self.setfinal(node.getlChild())
            self.setfinal(node.getrChild())
    
    def firstloop(self,height):
        checkarray = []
        for i in reversed(range(height)):
        
            self.idsetting(self.head,i,checkarray)
        #print(checkarray)
    def idsetting(self,node,level,checkarray):
        if(node != None):
            self.idsetting(node.getlChild(),level,checkarray)
            self.idsetting(node.getrChild(),level,checkarray)

            if(node.getlvl() == level):
                    left = node.getlChild().getId()
                    right = node.getrChild().getId()
                    if(left == right):
                        sum = left
                        node.setLogic(node.getlChild().getlogic())
                        node.setValue(node.getlChild().getValue())
                        node.setlChild(None)
                        node.setrChild(None)
                    else:
                        sum = left + right
                        sum = self.checkarr(checkarray,sum,left,right)
                    node.setId(sum)
                    checkarray.append([sum, left, right])
    def checkarr(self, checkarray,sum,left,right):
        for x in checkarray:
            if (sum == x[0]):
                if (left != x[1] or right != x[2]):
                    final = self.checkarr(checkarray,sum+1,left,right)
                    return final
        return sum
        return sum

    def ite(self, node):

        
        if(node.getlogic() == 1 or node.getlogic() == 0):
            print ( str(node.getlogic()) + ',' , end = '')
            flag=1;
            return 
            

        print ("ite ( " + str(node.getValue()[:-1]) + ',', end = '')

        self.ite(node.getrChild())
        self.ite(node.getlChild())

        print (')', end = '')

