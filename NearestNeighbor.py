'''CPSC-51100,[2nd Semester][2018-2019]
Name: [Boubacar Ide]
PROGRAMING ASSIGNMENT #3'''
# Import numpy
import numpy as np

# Loads and parses the training dataset files into separate NumPy ndarrays
fname_train = 'iris-training-data.csv'
train_attributes = np.loadtxt(fname_train, dtype='float', delimiter=',', usecols=(0,1,2,3))
train_classes = np.loadtxt(fname_train, dtype='str', delimiter=',', usecols=(4))

# Loads and parses the testing dataset files into separate NumPy ndarrays
fname_test = 'iris-testing-data.csv'
testing_attributes = np.loadtxt(fname_test, dtype='float', delimiter=',', usecols=(0,1,2,3))
testing_classes = np.loadtxt(fname_test, dtype='str', delimiter=',', usecols=(4))

# Print our output header as instructed
string1 = 'CPSC-51100,[2nd Semester][2018-2019]'
string2 = 'Name: [Boubacar Ide]'
string3 = 'PROGRAMING ASSIGNMENT #3'
print(string1 + '\n' + string2 + '\n' + string3+'\n')

# Calculate the distances between the testing and each training points
def euclideanDistance(instance1, instance2):
    distance = np.sqrt(np.sum((instance1 - instance2)**2,axis=1))
    return distance

# Get the nearest neighbor
def getNeighbors(trainingSet, testInstance, k):
    dist = euclideanDistance(testInstance, trainingSet)
    dist = np.argsort(dist)[:k]
#    neighbors = trainingClass[dist[:k]]
    return dist

# Choose the 31 nearest neighbor
neighbors = getNeighbors(train_attributes,testing_attributes[0,:],31)

# Classification of the plantes
def getResponse(neighbors,trainingClasses):
    classes = trainingClasses[neighbors]
    unique_elements, counts_elements = np.unique(classes, return_counts=True)
    index_max = np.argmax(counts_elements) #get the maximum count
    response = unique_elements[index_max]
    return response

getResponse(neighbors,train_classes)

# the output function of our prediction
def getAccuracy(trainingSet,trainingClass,testingSet,testingClass,k):
    response_vec = []  # Creating an empty list
    print("#,True,Predicted")
    count = 1
    for sample in testingSet:
        neighbors = getNeighbors(trainingSet,sample,k)
        response = getResponse(neighbors,trainingClass)
        response_vec.append(response)
        print("{},{},{}".format(count,testingClass[count-1],response))
        count += 1
    correct_labels = testingClass == response_vec  # Compare the testing and the response

    # Calculate the accuracy of our prediction
    accuracy = sum(correct_labels)/len(testingClass)*100
    print("Accuracy: {}%".format(accuracy))

getAccuracy(train_attributes,train_classes,testing_attributes,testing_classes,1)

