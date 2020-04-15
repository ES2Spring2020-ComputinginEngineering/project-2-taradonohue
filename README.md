This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).


This repository contains files that analyze the CKD data. The nearest neighbor classification file contains several functions that use nearest neighbor and k-nearest neighbor methods to make a prediction about the test case. In orde to run the k-nearest neighbor code, you must choose the (odd) number of neighbors the classification of the test case will be based on, and input that value into the k parameter in the k_neighbor function in the main script. It contains the following functions:
 
openckdfile takes in the data from the csv. It has no parameters, and returns glucose, hemoglobin, and classification. 

normalizeData normalizes the data so everything is on a scale of 0-1. It takes in the parameters of the glucose and hemoglobin data, and the classifications of each points. It returns the normalized versions of glucose and hemoglobin, as well as their classifications. 

graphData graphs the data. It takes in the parameters, glucose, hemoglobin, and classification, and has no return values.

createTestCase creates a random value to be used as the test case. It has no parameters, and returns new_hemoglobin and new_glucose, the coordinates of the test case.

calculateDistanceArray calculates the distance of every point from the test case. It takes in the test case coordinates and the normalized data as parameters. It returns all of the distances from the test case as an array.

nearestNeighborClassifier finds the closest point to the test case, and makes a guess about the classification of the test case based on the classification of the nearest neighbor. It takes in the parameters of the test case coordinates, the glucose, hemoglobin, and classification data, as well as the distance array. It returns the classification of the nearest neighbor.

graphTestCase graphs the data and the test case. It takes in the parameters of the test case coordinates and the data points.

kNearestNeighborClassifier finds the k nearest number of neighbors, and determines the classification of the test case based on the the average value of the classifications of the nearest neighbors. It takes the parameters k (the number of data points to test), the test case, the data points, and their classifications. It returns the prediction for the classification of the test case.


The K Means Clustering functions file contains the functions needed to run the code in the corresponding driver. The driver uses the functions to classify the data points. It uses randomly created intial centroids, assigns each point to its closest centroid, and iterates through the process 1,000 times before graphing the final assignments. In order to run it, the number of centroids to be used has to be input into the driver as the parameter in the createCentroid function. It contains the following functions:

openckdfile takes in the data from the csv. It has no parameters, and returns glucose, hemoglobin, and classification.

normalizeData normalizes the data so everything is on a scale of 0-1. It takes in the parameters of the glucose and hemoglobin data, and the classifications of each points. It returns the normalized versions of glucose and hemoglobin, as well as their classifications.

createCentroid creates random centroids to start the k means clustering process with. It takes the parameter k, the number of centroids to make, and returns the values of the centroids.
 
assign assigns every data point to the centroid that it is closest to. It takes in the centroids and the 
#normalized data as parameters. It returns the assignment of every data point as an array.

updateCentroids changes the value of every centroid so that it is the average value of all the data points assigned to it. It take the parameters of the normalized data and the assignment of all the data points. It returns the new values of the centroids.

iterate repeats the process of updating the centroids and assigning each data point to its closest centroid 1,000 times. It takes the parameters of the assignments and centroids, and returns the new assignments and centroid.

graphingKMeans graphs the data in order to visualize the centroids and all the points assigned to them. It takes the parameters of the glucose and hemoglobin data, the assignments, and the centroids. It has no return values.

falsePositiveChecker checks the assignments of each data point to see if it matches the actual classifications. It takes the assignments and classifications as parameters. It returns the rates for true positives, false positives, true negatives, and false negatives.
 
 
 


