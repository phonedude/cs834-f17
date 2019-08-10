'''
Created on Dec 12, 2017

@author: nauman
'''

import numpy as np

def pageRank(G,s, iteration):
    file = open("Output.txt", "w")
    pagerank = []
    nodes = G.shape[0]
    outlinks = []
    file.write("****PageRank**** \n")
    for i in range(0,nodes):
        outlinks.append(0) 
        pagerank.append(1/nodes)
    
    for i in range(0, nodes):
        for j in range(0, nodes):
            if G[j][i] == 1:
                outlinks[i] +=1
    print(pagerank)
    print(outlinks)
   
    for i in range(0,iteration):
        for j in range(0,nodes):
            pr = 0.0
            for k in range(0,nodes):
                if G[j][k] == 1:
                    print(str(j)+"  " + str(k))
                    pr += float(s*pagerank[k]/outlinks[k])
                    print(pr)
            if pr!= 0:
                pagerank[j]= float((1-s)/nodes) + pr
        file.write("Iteration: " + str(i) + "\n")
        file.write(str(pagerank)) 
        file.write("\n")
    file.close()

def hitsAlgorithm(G,iteration):
    file = open("Output.txt", "a+")
    file.write("**** HITS Algorithm**** \n")
    authority = []
    hub = []
    nodes = G.shape[0]
    for i in range(0,nodes):
        authority.append(1)
        hub.append(1)
    for i in range(0,iteration):
        new_authority = [0] * nodes
        new_hub = [0]* nodes
        for j in range(0,nodes):
            for k in range(0,nodes):
                if G[j][k] == 1:
                    new_authority[j] += hub[k]
                if G[k][j] == 1:
                    new_hub[j] += authority[k]
        sumAuthority = 0
        sumHub = 0
        for j in range(0,nodes):
            sumAuthority += new_authority[j]
            sumHub += new_hub[j]
        for j in range(0,nodes):
            authority[j] = new_authority[j]/sumAuthority
            hub[j] = new_hub[j]/sumHub
        file.write("Iteration:" + str(i) + "\n")
        file.write("Authority: " + str(authority) + "\n")
        file.write("Hub: " + str(hub) + "\n")
    file.close()
    
if __name__=='__main__':
    # Example extracted from 'Introduction to Information Retrieval'
    G = np.array([[0,0,1,0,1,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,1,0,0,0,0],
                  [0,1,1,1,0,0,0],
                  [0,0,0,0,0,0,0]])
    pageRank(G,s=.85, iteration = 5)
    hitsAlgorithm(G, iteration = 5)

