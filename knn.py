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

     for x in range(1,length):        
         distance += pow((instance1[x] - instance2[x]), 2)
     return math.sqrt(distance)


# locate most similar neighbors
def getNeighbors(trainingSet, testInstance, k):
     distances = []
     length = len(testInstance)
     for x in range(len(trainingSet)):
         dist = euclideanDistance(testInstance, trainingSet[x], length)
         distances.append((trainingSet[x], dist))
         
         distances.sort(key=operator.itemgetter(1))
         
         neighbors = []
     for x in range(k):
         neighbors.append(distances[x][0])
     #print(neighbors)
     return neighbors


def getResponse(neighbors):
     classVotes = {}
     print('hola')
     for x in range(len(neighbors)):
         response = neighbors[x][-1]
         print(response)
         if response in classVotes:
             classVotes[response] += 1
         else:
             classVotes[response] = 1
         sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
     return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
     correct = 0
     for x in range(len(testSet)):
         if testSet[x][-1] is predictions[x]:
             correct += 1
     return (correct/float(len(testSet))) * 100.0


def main():
    trainingSet = []
    testSet = []
    

    trainingSet= loadDataset('act_train1.csv')
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
#    print(trainingSet)
#    print(testSet)


    f=open('predictions.csv','w')
    f.write('activity_id' + ',' + 'outcome' + '\n')

    predictions=[]
    k = 3
    for x in range(len(testSet)):
        line=[1,2]
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        print(list(testSet[x])[0],result)
        f.write(list(testSet[x])[0] + ',' + result + '\n')
        #print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
        #accuracy = getAccuracy(testSet, predictions)
        #print('Accuracy: ' + repr(accuracy) + '%')

main()