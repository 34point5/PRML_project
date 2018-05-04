import numpy as np
import csv
import random
import math
import operator


# Load Data Set and Split Function
def loadDataset(filename):
    with open(filename, 'r') as f:
        lines = csv.reader(f)

        #for row in lines:
        #    print(lines)

        Set = []
        dataset = list(lines)

        for x in range(len(dataset) - 1):
           Set.append(dataset[x])

    #print (len(dataset), trainingSet, testSet)
    return Set

##calculate euclidean distance
def euclideanDistance(instance1, instance2, length):
     distance = 0
    # print("calculating")
     for x in range(1,length):        
         distance += pow((instance1[x] - instance2[x]), 2)
     return math.sqrt(distance)


def getAccuracy(testSet, predictions):
     correct = 0
     for x in range(len(testSet)):
         if testSet[x][-1] is predictions[x]:
             correct += 1
     return (correct/float(len(testSet))) * 100.0


def main():
    trainingSet = []
    testSet = []
    

    trainingSet= loadDataset('act_train2.csv')
    testSet=loadDataset('act_test.csv')


    for i in range(len(trainingSet)):
        if(trainingSet[i][3]=='type 1'):
            trainingSet[i][13]='type 0' 
        else: 
            for k in range(4,13): 
                trainingSet[i][k]='type 0' 
        del(trainingSet[i][0])
        del(trainingSet[i][1])
        
        for h in range(1,12):
            if trainingSet[i][h].split(' ')[0]=='type':
                trainingSet[i][h]=float(trainingSet[i][h].split(' ')[1])
    del(trainingSet[0])
    
    for i in range(len(testSet)):

        if (testSet[i][3]=='type 1'):
            testSet[i][13]='type 0'
        else:
            for k in range(4,13):
                testSet[i][k]='type 0'
        del(testSet[i][0])        
        del(testSet[i][1])

        for h in range(1,12):
            if testSet[i][h].split(' ')[0]=='type':
                testSet[i][h]=float(testSet[i][h].split(' ')[1])
    del(testSet[0])

    print('Train: ' + repr(len(trainingSet)))
    print('Test: ' + repr(len(testSet)))


    f=open('predictions.csv','w')
    f.write('activity_id' + ',' + 'outcome' + '\n')

    predictions=[]
    #density function
    h = 0.5
    n = len(trainingSet)
    count = 0
    for x in range(len(testSet)):

        func0 = func1 = 0

        for y in range(len(trainingSet)):

            dist1 = euclideanDistance(testSet[x],trainingSet[y],10)
            print(dist1)

            if(trainingSet[y][12] == '0'):

                func0 = func0 + ((math.pow(1/(1.25),10))*math.exp(-math.pow(dist1,2)/(2*(0.5*0.5))))/n
            else:
                func1 = func1 + ((math.pow(1/(1.25),10))*math.exp(-math.pow(dist1,2)/(2*(0.5*0.5))))/n

            print("couunt")
            print(count)

        if(func1>func0):
            c = '1';
        else:
            c = '0';

        f.write(list(testSet[x])[0] + ',' + c + '\n')
        count = count + 1

main()