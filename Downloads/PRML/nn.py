import numpy as np
import pandas as pd
import csv

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

def sigmoid(x, deriv=False):
    if deriv == True:
        return x * (1 - x)

    return 1 / (1 + np.exp(-x))



# This is the forward propagation function
def forward_prop(model,a0):
    
    # Load parameters from model
    W1, b1, W2, b2, W3, b3 = model['W1'], model['b1'], model['W2'], model['b2'], model['W3'],model['b3']
    
    # Do the first Linear step 
    z1 = a0.dot(W1) + b1
    
    # Put it through the first activation function
    a1 = np.tanh(z1)
    
    # Second linear step
    z2 = a1.dot(W2) + b2
    
    # Put through second activation function
    a2 = np.tanh(z2)
    
    #Third linear step
    z3 = a2.dot(W3) + b3
    
    #For the Third linear activation function we use the softmax function
    a3 = softmax(z3)
    
    #Store all results in these values
    cache = {'a0':a0,'z1':z1,'a1':a1,'z2':z2,'a2':a2,'a3':a3,'z3':z3}
    return cache

# This is the backward propagation function
def backward_prop(model,cache,y):

# Load parameters from model
    W1, b1, W2, b2, W3, b3 = model['W1'], model['b1'], model['W2'], model['b2'],model['W3'],model['b3']
    
    # Load forward propagation results
    a0,a1, a2,a3 = cache['a0'],cache['a1'],cache['a2'],cache['a3']
    
    # Get number of samples
    m = y.shape[0]
    
    # Calculate loss derivative with respect to output
    dz3 = loss_derivative(y=y,y_hat=a3)

# Calculate loss derivative with respect to second layer weights
    dW3 = 1/m*(a2.T).dot(dz3) #dW2 = 1/m*(a1.T).dot(dz2) 
    
    # Calculate loss derivative with respect to second layer bias
    db3 = 1/m*np.sum(dz3, axis=0)
    
    # Calculate loss derivative with respect to first layer
    dz2 = np.multiply(dz3.dot(W3.T) ,tanh_derivative(a2))
    
    # Calculate loss derivative with respect to first layer weights
    dW2 = 1/m*np.dot(a1.T, dz2)
    
    # Calculate loss derivative with respect to first layer bias
    db2 = 1/m*np.sum(dz2, axis=0)
    
    dz1 = np.multiply(dz2.dot(W2.T),tanh_derivative(a1))
    
    dW1 = 1/m*np.dot(a0.T,dz1)
    
    db1 = 1/m*np.sum(dz1,axis=0)
    
    # Store gradients
    grads = {'dW3':dW3, 'db3':db3, 'dW2':dW2,'db2':db2,'dW1':dW1,'db1':db1}
    return grads



# Data

trainingSet= loadDataset('act_train.csv')
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
print(trainingSet[1])
print(testSet[1])
print(trainingSet[1][1:11])
Xin=[]
Yin=[]
Zin=[]
for i in range (len(trainingSet)):
    print(i)
    Xin.append(trainingSet[i][1:12])
    Zin.append(trainingSet[i][0])
    Yin.append(trainingSet[i][12])
print(Xin)
print (Yin)
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(28,8), random_state=1)
clf.fit(Xin, Yin)                         
print(clf)
MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto',beta_1=0.9, beta_2=0.999, early_stopping=False,epsilon=1e-08, hidden_layer_sizes=(5, 2), learning_rate='constant',learning_rate_init=0.001, max_iter=200, momentum=0.9,
nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
solver='lbfgs', tol=0.0001, validation_fraction=0.1, verbose=False,
warm_start=False)
f=open('neuralnet.csv',"w")
clf.predict([[4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 76.0]])
f.write('activity_id' + ',' + 'outcome' + '\n')
for i in range(len(testSet)):
    print(testSet[i][0])
    print(clf.predict([testSet[i][1:]]))
    f.write( testSet[i][0]+ ',' + clf.predict([testSet[i][1:]])[0]+'\n')

