#Please put your code for Step 2 and Step 3 in this file.


import numpy as np
import matplotlib.pyplot as plt
import random


# FUNCTIONS
def openckdfile():
#This takes in the data from the csv. It has no parameters, and returns glucose, hemoglobin, and classification.
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(glucose, hemoglobin, classification):
#This normalizes the data so everything is on a scale of 0-1. It takes in the parameters of the glucose and 
#hemoglobin data, and the classifications of each points. It returns the normalized versions of glucose and 
#hemoglobin, as well as their classifications.
    normal_glucose = (glucose - np.amin(glucose))/(np.amax(glucose)-np.amin(glucose))
    normal_hemoglobin = (hemoglobin - np.amin(hemoglobin)) / (np.amax(hemoglobin) - np.amin(hemoglobin))
    normal_classification = classification
    return normal_glucose, normal_hemoglobin, normal_classification

def graphData(glucose, hemoglobin, classification):
#This graphs the data. It takes in the parameters, glucose, hemoglobin, and classification, and has no return
#values.
   plt.figure()
   plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "CKD Cases")
   plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Normal Cases")
   plt.xlabel("Hemoglobin")
   plt.ylabel("Glucose")
   plt.title("Glucose vs. Hemoglobin")
   plt.legend()
   plt.show()

def createTestCase():
#This creates a random value to be used as the test case. It has no parameters, and returns new_hemoglobin
#and new_glucose, the coordinates of the test case.
    new_hemoglobin = np.random.random_sample()
    new_glucose = np.random.random_sample()
    return (new_hemoglobin, new_glucose)

def calculateDistanceArray(new_glucose, new_hemoglobin, normal_glucose, normal_hemoglobin):
#This calculates the distance of every point from the test case. It takes in the test case coordinates and
#the normalized data as parameters. It returns all of the distances from the test case as an array.
    distance_array = np.zeros((0,1))
    for i in range(158):
        distance = np.sqrt(((normal_glucose[i] - new_glucose)**2) + ((normal_hemoglobin[i] - new_hemoglobin)**2))
        distance_array = np.append(distance_array, distance)
    return distance_array

def nearestNeighborClassifier(new_glucose, new_hemoglobin, glucose, hemoglobin, classification, distance_array):
#This function finds the closest point to the test case, and makes a guess about the classification of the test
#case based on the classification of the nearest neighbor. It takes in the parameters of the test case coordinates,
#the glucose, hemoglobin, and classification data, as well as the distance array. It returns the classification of 
#the nearest neighbor.
    distance_array = calculateDistanceArray (new_glucose, new_hemoglobin, normal_glucose, normal_hemoglobin)
    min_index = np.argmin(distance_array)
    nearest_class = classification[min_index]
    print(nearest_class)
    return nearest_class

def graphTestCase(new_glucose, new_hemoglobin, glucose, hemoglobin, classification):
#This graphs the data and the test case. It takes in the parameters of the test case coordinates and the data points.
   plt.figure()
   plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "CKD Cases")
   plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Normal Cases")
   plt.plot(new_hemoglobin, new_glucose, "g.", label = "Test Case", markersize = 15)
   plt.xlabel("Hemoglobin")
   plt.ylabel("Glucose")
   plt.title("Glucose vs. Hemoglobin (Including Test Case)")
   plt.legend()
   plt.show()    

def kNearestNeighborClassifier(k, new_glucose, new_hemoglobin, normal_glucose, normal_hemoglobin, classification):
#This finds the k nearest number of neighbors, and determines the classification of the test case based on the 
#the average value of the classifications of the nearest neighbors. It takes the parameters k (the number of data
#points to test), the test case, the data points, and their classifications. It returns the prediction for the 
#classification of the test case.
    distance_array = calculateDistanceArray (new_glucose, new_hemoglobin, normal_glucose, normal_hemoglobin)
    sorted_array =  np.argsort(distance_array)  
    k = sorted_array[:k]
    class_of_k_values = classification[k]
    average_k = np.median(class_of_k_values)
    return average_k

# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()
normal_glucose, normal_hemoglobin, normal_classification = normalizeData(glucose, hemoglobin, classification)
new_hemoglobin, new_glucose = createTestCase()
distance_array = calculateDistanceArray(new_glucose, new_hemoglobin, normal_glucose, normal_hemoglobin)
nearest_class = nearestNeighborClassifier(new_glucose, new_hemoglobin, normal_glucose, normal_hemoglobin, classification, distance_array)
k_neighbor = kNearestNeighborClassifier(5, new_glucose, new_hemoglobin, normal_glucose, normal_hemoglobin, classification)
graphTestCase(new_glucose, new_hemoglobin, normal_glucose, normal_hemoglobin, normal_classification)


