import os 
import math
import csv 
from numpy import matrix
from numpy import linalg
import numpy

trainingSet = []
testSet = []

data1 = []
data0 = []

K = 5
mean = [[0 for x in range(10)] for y in range(K) ]  # K x 10
mean1 = [[0 for x in range(10)] for y in range(K)]  # K x 10

covariance = [[[0 for x in range(10)]for y in range(10)] for z in range(K)] # K x 10 x 10
covariance1 = [[[0 for x in range(10)]for y in range(10)]for z in range(K)]  # K x 10 x 10
cov_inv = [[[0 for x in range(10)]for y in range(10)]for z in range(K)]  # K x 10 x 10
cov_inv1 = [[[0 for x in range(10)]for y in range(10)]for z in range(K)]  # K x 10 x 10

alpha = [float(1/float(K)) for x in range(K)]   # array of K values 
alpha1 = [float(1/float(K)) for x in range(K)]   # array of K values

initial_min = [0 for x in range(10)]
initial_max = [0 for x in range(10)]
initial_min1 = [0 for x in range(10)]
initial_max1 = [0 for x in range(10)]


def gaussian_pdf(J , I):
    
    temp = covariance[J]
    #print temp 
    #print('covariance' + '\n')

    temp_inv = cov_inv[J] #numpy.linalg.inv(temp)
   # print temp_inv 
    temp_x = [0.0 for x in range(10)]
    final = 0.0

    for i in range(10):
        for j in range(1 , 11):
            temp_x[i] = float(temp_x[i] + float((I[j] - mean[J][j-1])*(temp_inv[j-1][i])))
    
    for i in range(10):
        final = float(final + float(temp_x[i]*(I[i+1] - mean[J][i]) ) )

    dett = numpy.linalg.det(temp)
    dett = float(math.sqrt(dett))
    dett = float(dett*(pow(2*math.pi , 5)))  # d/2 = 10/2 = 5
    exp_value = math.exp(-final/2) 
    answer = exp_value/dett  
    return answer 

def gaussian_pdf1(J ,I):
    temp = covariance1[J]
    temp_inv = cov_inv1[J] #numpy.linalg.inv(temp)
   # print temp_inv
    temp_x = [0.0 for x in range(10)]
    final = 0.0

    for i in range(10):
        for j in range(1, 11):
            temp_x[i] = float(temp_x[i] + float((I[j] - mean1[J][j-1])*(temp_inv[j-1][i])))

    for i in range(10):
        final = float(final + float(temp_x[i]*(I[i+1] - mean1[J][i])))

    dett = numpy.linalg.det(temp)
    dett = float(math.sqrt(dett))
    dett = float(dett*(pow(2*math.pi, 5)))  # d/2 = 10/2 = 5
    exp_value = math.exp(-final/2)
    answer = exp_value/dett
    return answer

def bayes(X):
    sum1 = 0.0 
    for i in range(K):
        sum1 = float(sum1 + alpha[i]*gaussian_pdf(i , X))
    
    sum2 = 0.0 
    for i in range(K):
        sum2 = float(sum2 + alpha1[i]*gaussian_pdf1(i , X))
    
    if(sum1 > sum2):
        return '1'
    else:
        return '0' 

#Borrowed from Rohan's Knn :p 

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

# Borrowed from Rohan's Knn :p
def main():

    trainingSet = loadDataset('act_train1.csv')
    testSet = loadDataset('act_test.csv')
# Some Processing of data for Training Set 

    for i in range(len(trainingSet)):
        if(trainingSet[i][3] == 'type 1'):
            trainingSet[i][13] = 'type 0'
        else:
            for k in range(4, 13):
                trainingSet[i][k] = 'type 0'
        del(trainingSet[i][0])
        del(trainingSet[i][1])
        del(trainingSet[i][1])
        
        for h in range(1, 11):
            if trainingSet[i][h].split(' ')[0] == 'type':
                trainingSet[i][h] = float(trainingSet[i][h].split(' ')[1])
        
        if(i != 0):
            if(int(trainingSet[i][-1]) == 1):
                data1.append(trainingSet[i])
                del(data1[-1][-1])
                
                for h in range(1 ,11):
                    if(i == 1):
                        initial_max[h-1] = trainingSet[i][h]
                        initial_min[h-1] = trainingSet[i][h]
                    else:
                        initial_max[h-1] = max(initial_max[h-1] , trainingSet[i][h])
                        initial_min[h-1] = min(initial_min[h-1] , trainingSet[i][h])
            else:
                data0.append(trainingSet[i])
                del(data0[-1][-1])

                for h in range(1 ,11):
                    if(i == 1):
                        initial_max1[h-1] = trainingSet[i][h]
                        initial_min1[h-1] = trainingSet[i][h]
                    else:
                        initial_max1[h-1] = max(initial_max1[h-1] , trainingSet[i][h])
                        initial_min1[h-1] = min(initial_min1[h-1] , trainingSet[i][h])
    del(trainingSet[0])

    for i in range(len(testSet)):

        if (testSet[i][3] == 'type 1'):
            testSet[i][13] = 'type 0'
        else:
            for k in range(4, 13):
                testSet[i][k] = 'type 0'
        del(testSet[i][0])
        del(testSet[i][1])
        del(testSet[i][1])

        for h in range(1, 11):
            if testSet[i][h].split(' ')[0] == 'type':
                testSet[i][h] = float(testSet[i][h].split(' ')[1])
    del(testSet[0])

# YOUR JOB ABOVE THIS IS TO CREATE THE DATA MATRIX  , done only test data left

#THE EM ALGORITHM 
 
  # INITIAL PARAMETERS
    N = len(data1)
    weight = [[1/float(K) for y in range(K)] for x in range(N)]   # N x K 
    
    for i in range(10):
        r = float(initial_max[i] - initial_min[i])/float(K + 1 ) 
        for j in range(K):
            mean[j][i] = float((j+1)*r) 


    for i in range(len(data1)):
        for j in range(1 , 11):
            for k in range(1 , 11):
                for l in range(K):
                    covariance[l][j-1][k-1] = float(covariance[l][j-1][k-1] + float((data1[i][j] - mean[l][j-1])*(data1[i][k] - mean[l][k-1]))/float(len(data1)))

    # INITIAL PARAMETERS for data0

    N = len(data0)
    weight1 = [[1/float(K) for y in range(K)] for x in range(N)]   # N x K

    for i in range(10):
        r = float(initial_max1[i] - initial_min1[i])/float(K + 1)
        for j in range(K):
            mean1[j][i] = float((j+1)*r)

    for i in range(len(data0)):
        for j in range(1, 11):
            for k in range(1, 11):
                for l in range(K):
                    covariance1[l][j-1][k-1] = float(covariance1[l][j-1][k-1] + float(float((data0[i][j] - mean1[l][j-1])*(data0[i][k] - mean1[l][k-1])))/float(len(data0)))


    
    count = 10
  
    while count >= 0:
        print ('iteration no. ')
        print count
        count = count - 1

        for i in range(K):
            cov_inv = numpy.linalg.inv(covariance[i]) 
    # THE E STEP - involves calculation of all weight factors 

        for i in range(len(data1)):
            temp = [0.0 for x in range(K)] 
            sum1 = 0.0
        
            for j in range(K):
                prob = float(gaussian_pdf(j , data1[i]))
                temp[j] = float(alpha[j]*prob)
                sum1 = float(sum1 + float(temp[j])) 
        
            for j in range(K):
                weight[i][j] = float(temp[j]/sum1) 


    #VALIDATION OF THIS STEP YET TO BE DONE , FOR VALIDATION REFER THE MATERIAL

    # THE M STEP - involves update on all the parameters 

        for i in range(K):
            sum1 = 0.0
            arr_mean = [0.0 for x in range(10)]

            for j in range(len(data1)):
                sum1 = float(sum1 + weight[j][i]) 
                for k in range(1 ,11): 
                    arr_mean[k-1] = float(weight[j][i]*data1[j][k])
        
            alpha[i] = float(sum1/float(len(data1)))         #modification of alpha

            for j in range(10):
                mean[i][j] = float(arr_mean[j]/sum1)         #modification of mean

            cov = [[0.0 for x in range(10)] for y in range(10) ]

            for j in range(len(data1)):
                for k in range(1 , 11):
                    for l in range(1 , 11):
                        cov[k-1][l-1] = float(float(cov[k-1][l-1] + weight[j][i]*(data1[j][k] - mean[i][k-1])*(data1[j][l] - mean[i][l-1]))/sum1)
        
            for j in range(10):
                for k in range(10):
                    covariance[i][j][k] = cov[j][k]           #modification of covariance matrix 




    # for data from data0 
    
    # THE E STEP - involves calculation of all weight factors

        for i in range(K):
            cov_inv1[i] = numpy.linalg.inv(covariance1[i])

        for i in range(len(data0)):
            temp = [0.0 for x in range(K)]
            sum1     = 0.0

            for j in range(K):
                prob = float(gaussian_pdf1(j, data0[i]))
                temp[j] = float(alpha1[j]*prob)
                sum1 = sum1 + float(temp[j])

            for j in range(K):
                weight1[i][j] = float(temp[j]/sum1)

    #VALIDATION OF THIS STEP YET TO BE DONE , FOR VALIDATION REFER THE MATERIAL

    # THE M STEP - involves update on all the parameters

        for i in range(K):
            sum1 = 0.0
            arr_mean = [0.0 for x in range(10)]

            for j in range(len(data0)):
                sum1 = float(sum1 + weight1[j][i])
                for k in range(1, 11):
                    arr_mean[k-1] = float(weight1[j][i]*data0[j][k])

            alpha1[i] = float(sum1/float(len(data0)))  # modification of alpha

            for j in range(10):
                mean1[i][j] = float(arr_mean[j]/sum1)  # modification of mean

            cov = [[0.0 for x in range(10)] for y in range(10)]

            for j in range(len(data0)):
                for k in range(1, 11):
                    for l in range(1, 11):
                        cov[k-1][l-1] = float(float(cov[k-1][l-1] + weight1[j][i]*(data0[j][k] - mean1[i][k-1])*(data0[j][l] - mean1[i][l-1]))/sum1)

            for j in range(10):
                for k in range(10):
                # modification of covariance matrix
                    covariance1[i][j][k] = cov[j][k]

    print covariance
    print 'covariance'
    print covariance1
    print 'covariance1'
    f = open('predictions.csv', 'w')
    f.write('activity_id' + ',' + 'outcome' + '\n')

    predictions = []

    print('final')
    for x in range(len(testSet)):
        result = bayes(testSet[x])
        f.write(list(testSet[x])[0] + ',' + result + '\n')

main()
