# This page contains all the functions in this project

import pandas as pd
import math
import operator

# This function is used to create the training datasets and test datasets.
def loadDataset(filename):
    data = pd.read_csv(filename,
                       usecols=['AST/TOV', 'STL/TOV', 'Height', 'Weight', 'PTSPM', 'DREBPM', 'ASTPM', 'STLPM', 'BLKPM',
                                'OREBPM', 'Pos'])
    data = data.dropna()
    data.to_csv('Result.csv')

    try:
        file = open('Result.csv', 'r', encoding="gbk")
        next(file)
        context = file.read()
        list_result = context.split("\n")
        length = len(list_result)
        for i in range(length):
            list_result[i] = list_result[i].split(",")
        list_result.pop()
        test_data = []
        training_data = []
        for i in range(len(list_result)):
            if i % 5 == 0:
                test_data.append(list_result[i])
            else:
                training_data.append(list_result[i])
        return test_data, training_data
    except Exception :
        print("Could not read file, please check the file path.")
    finally:
        file.close()


# This function is to get the Euclidean Distance of two data
def getDistance(instance1, instance2, length):
    distance = 0
    for x in range(1, length):
        distance += pow((float(instance1[x]) - float(instance2[x])), 2)
    return math.sqrt(distance)

# This function is to get the k nearest neighbors of the test data.
def getNeighbors(training_data, test, k):
    distances = []
    length = len(test) - 1
    for x in range(len(training_data)):
        dist = getDistance(test, training_data[x], length)
        distances.append((training_data[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

# This function is to predict which position is the test data pointing to.
def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

# This function is used to get the accuracy.
def getAccuracy(test_data, predictions):
    correct = 0
    for x in range(len(test_data)):
        if test_data[x][-1] == predictions[x]:
            correct += 1
    return (correct / float(len(test_data))) * 100.0
