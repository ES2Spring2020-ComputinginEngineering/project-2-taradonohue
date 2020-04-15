#driver
#Please place your FUNCTION code for step 4 here.
import KMeansClustering_functions as kmc #Use kmc to call your functions



glucose, hemoglobin, classification = openckdfile()

normal_glucose, normal_hemoglobin, classification = normalizeData(glucose, hemoglobin, classification)
centroids = createCentroid(2)
assignment = assign(centroids, normal_glucose, normal_hemoglobin)
assignment, centroids = iterate(assignment, centroids)
graphingKMeans(normal_glucose, normal_hemoglobin, assignment, centroids)
falsePositiveChecker(assignment, classification)
