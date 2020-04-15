#Please place your FUNCTION code for step 4 here.

import numpy as np
import matplotlib.pyplot as plt
import random

#CITE STARTER CODE!

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
    return normal_glucose, normal_hemoglobin, classification 

def createCentroid(K):
#This creates random centroids to start the k means clustering process with. It takes the parameter k, the 
#number of centroids to make, and returns the values of the centroids.
    the_centroids = np.random.random((K, 2))
    print("The centroids are:", the_centroids)
    return the_centroids

def assign(centroids, normal_glucose, normal_hemoglobin):
#This assigns every data point to the centroid that it is closest to. It takes in the centroids and the 
#normalized data as parameters. It returns the assignment of every data point as an array.
    K = centroids.shape[0]
    distances = np.zeros((K, len(hemoglobin)))
    for i in range(K):
        g = centroids[i,1]
        h = centroids[i,0]
        distances[i] = np.sqrt((normal_hemoglobin-h)**2+(normal_glucose-g)**2)       
    assignment = np.argmin(distances, axis = 0)    
    return assignment       
 
def updateCentroids(assignment, normal_hemoglobin, normal_glucose):
#This changes the value of every centroid so that it is the average value of all the data points 
#assigned to it. It take the parameters of the normalized data and the assignment of all the 
#data points. It returns the new values of the centroids.
    K = centroids.shape[0]
    new_centroids = np.zeros((K, 2))
    new_middle = assignment
    for i in range (K):
        average_hemoglobin = np.mean(normal_hemoglobin[new_middle==i])
        average_glucose = np.mean(normal_glucose[new_middle==i])
        new_centroids[i,0] = average_hemoglobin
        new_centroids[i,1] = average_glucose
    return new_centroids

def iterate(assignment, centroids):
#This repeats the process of updating the centroids and assigning each data point to its closest
#centroid 1,000 times. It takes the parameters of the assignments and centroids, and returns the 
#new assignments and centroid.
    iterations = 0
    while iterations <= 1000:
        assignment = assign(centroids, normal_hemoglobin, normal_glucose)
        centroids = updateCentroids(assignment, normal_hemoglobin, normal_glucose)
        iterations+=1
    return assignment, centroids  

def graphingKMeans(glucose, hemoglobin, assignment, centroids):
#This graphs the data in order to visualize the centroids and all the points assigned to them.
#It takes the parameters of the glucose and hemoglobin data, the assignments, and the centroids.
#It has no return values.
    plt.figure()
    for i in range(assignment.max()+1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[assignment==i],glucose[assignment==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(centroids[i, 0], centroids[i, 1], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.title("Glucose vs. Hemoglobin (K Means Clustering)")
    plt.legend()
    plt.show()   
    
def falsePositiveChecker(assignment, classification):
#This checks the assignments of each data point to see if it matches the actual classifications. It takes 
#the assignments and classifications as parameters. It returns the rates for true positives, false positives,
#true negatives, and false negatives.
    true_positive = 0
    false_positive = 0
    true_negative = 0
    false_negative = 0
    for i in range(len(classification)):
        if classification[i] == 1 and assignment[i] == 1:
            true_positive += 1
        if classification[i] == 0 and assignment[i] == 1:
            false_positive += 1
        if classification[i] == 1 and assignment[i] == 1:
            true_negative += 1
        if classification[i] == 1 and assignment[i] == 0:
            false_negative += 1
    true_positive_rate =  (true_positive) / (true_positive + false_negative) 
    false_positive_rate = (false_positive) / (false_negative + true_positive)
    true_negative_rate = (true_negative) / (true_negative + false_positive)
    false_negative_rate = (false_negative) / (false_negative + true_positive)
    print(true_positive_rate, false_positive_rate, true_negative_rate, false_negative_rate)
    return true_positive_rate, false_positive_rate, true_negative_rate, false_negative_rate

            

