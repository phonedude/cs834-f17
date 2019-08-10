'''
Created on Nov 22, 2017

@author: nauman
'''
import math

def singleLinkage(clusterPointA, clusterPointB):
    minDistance = math.inf
    for i in range(0, len(clusterPointA)):
        for j in range(0,len(clusterPointB)):
            distance = math.sqrt(math.pow((clusterPointA[i][0]-clusterPointB[j][0]),2) + math.pow((clusterPointA[i][1]-clusterPointB[j][1]),2))
            if minDistance > distance:
                minDistance = distance
    return minDistance
    
def agglomerativeSingleLinkageCluster(clusterValue, clusterPoints):
    
    distanceMatrix = []
    finalClusters = []
    
    for i in range(0,len(clusterPoints)):
        finalClusters.append([i])
 
    for c in range(len(clusterPoints), clusterValue, -1):
        bestClusterA = []
        bestClusterB  = []
        bestCost = math.inf
        for i in range(0,len(clusterPoints)):
            temp = []
            for j in range(0,len(clusterPoints)):
                temp.append(0)
            distanceMatrix.append(temp)
             
        for i in range(0,len(clusterPoints)):
            for j in range((i+1),len(clusterPoints)):
                distance = singleLinkage(clusterPoints[i], clusterPoints[j])
                distanceMatrix[i][j] = (distance)
                if bestCost > distance:
                    bestCost = distance
                    if bestClusterA and bestClusterB:
                        bestClusterA.pop()
                        bestClusterB.pop()
                    bestClusterA.append(clusterPoints[i])
                    bestClusterB.append(clusterPoints[j])
        clusterPoints.remove(bestClusterB[0])
        index = clusterPoints.index(bestClusterA[0])
        for x in range(0,len(bestClusterB[0])):
            clusterPoints[index].append(bestClusterB[0][x])
    return (clusterPoints)

def completeLinkage(clusterPointA, clusterPointB):
    maxDistance = 0
    for i in range(0, len(clusterPointA)):
        for j in range(0,len(clusterPointB)):
            distance = math.sqrt(math.pow((clusterPointA[i][0]-clusterPointB[j][0]),2) + math.pow((clusterPointA[i][1]-clusterPointB[j][1]),2))
            if maxDistance < distance:
                maxDistance = distance
    return maxDistance 
   
def agglomerativeCompleteLinkageCluster(clusterValue, input):
    
    distanceMatrix = []
    finalClusters = []
    
    clusterPoints = input
    for i in range(0,len(clusterPoints)):
        finalClusters.append([i])
 
    for c in range(len(clusterPoints), clusterValue, -1):
        bestClusterA = []
        bestClusterB  = []
        bestCost = 0
        for i in range(0,len(clusterPoints)):
            temp = []
            for j in range(0,len(clusterPoints)):
                temp.append(0)
            distanceMatrix.append(temp)
             
        for i in range(0,len(clusterPoints)):
            for j in range((i+1),len(clusterPoints)):
                distance = completeLinkage(clusterPoints[i], clusterPoints[j])
                distanceMatrix[i][j] = (distance)
                if bestCost < distance:
                    bestCost = distance
                    if bestClusterA and bestClusterB:
                        bestClusterA.pop()
                        bestClusterB.pop()
                    bestClusterA.append(clusterPoints[i])
                    bestClusterB.append(clusterPoints[j])
        clusterPoints.remove(bestClusterB[0])
        index = clusterPoints.index(bestClusterA[0])
        for x in range(0,len(bestClusterB[0])):
            clusterPoints[index].append(bestClusterB[0][x])
    return (clusterPoints)        

def averageLinkage(clusterPointA, clusterPointB):
    averageDistance = 0
    for i in range(0, len(clusterPointA)):
        for j in range(0,len(clusterPointB)):
            averageDistance = averageDistance +  math.sqrt(math.pow((clusterPointA[i][0]-clusterPointB[j][0]),2) + math.pow((clusterPointA[i][1]-clusterPointB[j][1]),2))
    averageDistance = averageDistance/(len(clusterPointA) +len(clusterPointB))
    return averageDistance


def agglomerativeAverageLinkageCluster(clusterValue, clusterPoints):

    distanceMatrix = []
    finalClusters = []
    
    for i in range(0,len(clusterPoints)):
        finalClusters.append([i])
 
    for c in range(len(clusterPoints), clusterValue, -1):
        bestClusterA = []
        bestClusterB  = []
        bestCost = math.inf
        for i in range(0,len(clusterPoints)):
            temp = []
            for j in range(0,len(clusterPoints)):
                temp.append(0)
            distanceMatrix.append(temp)
             
        for i in range(0,len(clusterPoints)):
            for j in range((i+1),len(clusterPoints)):
                distance = averageLinkage(clusterPoints[i], clusterPoints[j])
                distanceMatrix[i][j] = (distance)
                if bestCost > distance:
                    bestCost = distance
                    if bestClusterA and bestClusterB:
                        bestClusterA.pop()
                        bestClusterB.pop()
                    bestClusterA.append(clusterPoints[i])
                    bestClusterB.append(clusterPoints[j])
        clusterPoints.remove(bestClusterB[0])
        index = clusterPoints.index(bestClusterA[0])
        for x in range(0,len(bestClusterB[0])):
            clusterPoints[index].append(bestClusterB[0][x])
    return (clusterPoints)    
             
def averageGroupLinkage(clusterPointA, clusterPointB):
    centroidX_A = 0
    centroidY_A = 0
    centroidX_B = 0
    centroidY_B = 0
    centroidA = []
    centroidB = []
    for i in range(0, len(clusterPointA)):
        centroidX_A = centroidX_A + clusterPointA[i][0]
        centroidY_A = centroidY_A + clusterPointA[i][1]
    centroidA.append(centroidX_A/(len(clusterPointA)))
    centroidA.append(centroidY_A/(len(clusterPointA)))
    for j in range(0,len(clusterPointB)):
        centroidX_B = centroidX_B + clusterPointB[j][0]
        centroidY_B = centroidY_B + clusterPointB[j][1]
    centroidB.append(centroidX_B/(len(clusterPointB)))
    centroidB.append(centroidY_B/(len(clusterPointB)))    
    clusterDistance =   math.sqrt(math.pow((centroidA[0]-centroidB[0]),2) + math.pow((centroidA[1]-centroidB[1]),2))
    return clusterDistance


def agglomerativeAverageGroupLinkageCluster(clusterValue, clusterPoints):

    distanceMatrix = []
    finalClusters = []
    
    for i in range(0,len(clusterPoints)):
        finalClusters.append([i])
 
    for c in range(len(clusterPoints), clusterValue, -1):
        bestClusterA = []
        bestClusterB  = []
        bestCost = math.inf
        for i in range(0,len(clusterPoints)):
            temp = []
            for j in range(0,len(clusterPoints)):
                temp.append(0)
            distanceMatrix.append(temp)
             
        for i in range(0,len(clusterPoints)):
            for j in range((i+1),len(clusterPoints)):
                distance = averageGroupLinkage(clusterPoints[i], clusterPoints[j])
                distanceMatrix[i][j] = (distance)
                if bestCost > distance:
                    bestCost = distance
                    if bestClusterA and bestClusterB:
                        bestClusterA.pop()
                        bestClusterB.pop()
                    bestClusterA.append(clusterPoints[i])
                    bestClusterB.append(clusterPoints[j])
        clusterPoints.remove(bestClusterB[0])
        index = clusterPoints.index(bestClusterA[0])
        for x in range(0,len(bestClusterB[0])):
            clusterPoints[index].append(bestClusterB[0][x])
    return (clusterPoints)             
                
def wardMethod(clusterPointA, clusterPointB):
    centroidX_A = 0
    centroidY_A = 0
    centroidX_B = 0
    centroidY_B = 0
    centroidA = []
    centroidB = []
    for i in range(0, len(clusterPointA)):
        centroidX_A = centroidX_A + clusterPointA[i][0]
        centroidY_A = centroidY_A + clusterPointA[i][1]
    centroidA.append(centroidX_A/(len(clusterPointA)))
    centroidA.append(centroidY_A/(len(clusterPointA)))
    for j in range(0,len(clusterPointB)):
        centroidX_B = centroidX_B + clusterPointB[j][0]
        centroidY_B = centroidY_B + clusterPointB[j][1]
    centroidB.append(centroidX_B/(len(clusterPointB)))
    centroidB.append(centroidY_B/(len(clusterPointB)))    
    clusterDistance =   math.sqrt(math.pow((centroidA[0]-centroidB[0]),2) + math.pow((centroidA[1]-centroidB[1]),2))
    variance = len(clusterPointA)* len(clusterPointB)* clusterDistance/ len(clusterPointA)+ len(clusterPointB)
    return variance


def agglomerativeWardMethod(clusterValue, clusterPoints):

    distanceMatrix = []
    finalClusters = []
    
    for i in range(0,len(clusterPoints)):
        finalClusters.append([i])
 
    for c in range(len(clusterPoints), clusterValue, -1):
        bestClusterA = []
        bestClusterB  = []
        bestCost = math.inf
        for i in range(0,len(clusterPoints)):
            temp = []
            for j in range(0,len(clusterPoints)):
                temp.append(0)
            distanceMatrix.append(temp)
             
        for i in range(0,len(clusterPoints)):
            for j in range((i+1),len(clusterPoints)):
                distance = wardMethod(clusterPoints[i], clusterPoints[j])
                distanceMatrix[i][j] = (distance)
                if bestCost > distance:
                    bestCost = distance
                    if bestClusterA and bestClusterB:
                        bestClusterA.pop()
                        bestClusterB.pop()
                    bestClusterA.append(clusterPoints[i])
                    bestClusterB.append(clusterPoints[j])
        clusterPoints.remove(bestClusterB[0])
        index = clusterPoints.index(bestClusterA[0])
        for x in range(0,len(bestClusterB[0])):
            clusterPoints[index].append(bestClusterB[0][x])
    return (clusterPoints) 
    
def main():
    clusters = 3
    input = [[[-4, -2]], [[-3, -2]], [[-2, -2]], [[-1, -2]], [[1, -1]], [[1, 1]], [[2, 3]], [[3, 2]], [[3, 4]], [[4,3]]]
    file = open("ClusteringOutput.txt", "w")
    clusterPointsSingle = agglomerativeSingleLinkageCluster(clusters,input)
    file.write("Single Linkage" + "\n")
    for i in range(0, len(clusterPointsSingle)):
        file.write("Cluster " + str(i+1) + ": " +str(clusterPointsSingle[i]) + "\n")
    inputComplete =[[[-4, -2]], [[-3, -2]], [[-2, -2]], [[-1, -2]], [[1, -1]], [[1, 1]], [[2, 3]], [[3, 2]], [[3, 4]], [[4,3]]]
    clusterPointsComplete = agglomerativeCompleteLinkageCluster(clusters,inputComplete)
    file.write("\nComplete Linkage\n")
    for i in range(0, len(clusterPointsComplete)):
        file.write("Cluster " + str(i+1) + ": " +str(clusterPointsComplete[i]) + "\n")
    inputAverage = [[[-4, -2]], [[-3, -2]], [[-2, -2]], [[-1, -2]], [[1, -1]], [[1, 1]], [[2, 3]], [[3, 2]], [[3, 4]], [[4,3]]]
    clusterPointsAverage = agglomerativeAverageLinkageCluster(clusters,inputAverage)
    file.write("\nAverage Linkage\n")
    for i in range(0, len(clusterPointsAverage)):
        file.write("Cluster " + str(i+1) + ": " +str(clusterPointsAverage[i])+ "\n")
    inputAverageGroup = [[[-4, -2]], [[-3, -2]], [[-2, -2]], [[-1, -2]], [[1, -1]], [[1, 1]], [[2, 3]], [[3, 2]], [[3, 4]], [[4,3]]]
    clusterPointsAverageGroup = agglomerativeAverageGroupLinkageCluster(clusters,inputAverageGroup)
    file.write("\nAverage Group Linkage\n")
    for i in range(0, len(clusterPointsAverageGroup)):
        file.write("Cluster " + str(i+1) + ": " +str(clusterPointsAverageGroup[i])+ "\n")
    inputWard = [[[-4, -2]], [[-3, -2]], [[-2, -2]], [[-1, -2]], [[1, -1]], [[1, 1]], [[2, 3]], [[3, 2]], [[3, 4]], [[4,3]]]
    clusterPointsWard = agglomerativeWardMethod(clusters,inputWard)
    file.write("\nWard's Algorithm Linkage\n")
    for i in range(0, len(clusterPointsWard)):
        file.write("Cluster " + str(i+1) + ": " +str(clusterPointsWard[i]) + "\n")
    file.close()
    
main()
    