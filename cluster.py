#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:28:20 2018

@author: bhavana
"""
import numpy as np
import topkfiltering as topk
import json
import random
#import repposts as RP
#from sklearn.metrics import jaccard_similarity_score
#from similaritymeasures import Similarity
with open('output.json') as f:
    data = json.load(f)

user,post_ids=topk.distinctMatrices(data) 
posts=  topk.extractTweetIndexMatrix(post_ids) 
print(type(posts))
#events={0:[3,['dog', 'cat', 'cat', 'rat']],1:[7,['dog', 'cat', 'mouse']]}
#posts={0:[3,['dog', 'cat', 'cat', 'rat']],1:[7,['dog', 'cat', 'mouse']],2:[9,['bottle', 'cat', 'glass']]}

authMatrix, hubMatrix = topk.authority_hub_scores()
minDist = topk.minDistance(posts, authMatrix)
events = topk.topKEvents(posts, authMatrix, minDist)
#print events        
def random_authority(k=len(posts)):
    authority=np.random.rand(k,1)
    print(len(authority))
    return authority    
    
def jaccard_similarity(x,y):
 
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    if(union_cardinality==0): return 0
    return intersection_cardinality/float(union_cardinality)

def Cloning(li1): 
    li_copy = [] 
    li_copy.extend(li1) 
    return li_copy

def mat_cloning(mat):
    mat_copy=[]
    for k in mat:
        mat_copy.append(Cloning(k))
    
    return mat_copy

        

def cluster_and_isModify(old_list,similarity_mat):
    ls=[]
    for k in range(len(similarity_mat)):
        ls.append([])
    
    for j in range(len(similarity_mat[0])):
        max_val=similarity_mat[0][j]
        max_i=0
        for i in range(len(similarity_mat)):
            if(similarity_mat[i][j]>max_val):
                max_val=similarity_mat[i][j]
                max_i=i
        
        ls[max_i].append(j)
    #print ls    
    if old_list==ls :
        return [ls,True]
    else:
        return [ls,False]
    
def modify_V(list_events,authority):
    V=np.zeros((len(events),len(posts)))
    
    for i in range(len(list_events)):
        sum_auth=0
        if(len(list_events[i])!=0):
            for j in list_events[i]:
                #print authority[j]
                sum_auth+=authority[j]
                
            for j in list_events[i]:
                V[i][j]=authority[j]/sum_auth
    return V  

def modify_similarity(V,Jaccard): 
    similarity_mat=np.zeros((len(events),len(posts)))
    for i in range(len(events)):
        for j in range(len(posts)):
            sum=0
            for h in range(len(posts)):
                sum=sum+V[i][h]*Jaccard[j][h]
            similarity_mat[i][j]=sum
    #print similarity_mat
    return similarity_mat
            
def auto_event_cluster(authority,no_iter=1):
    
    #events=RP.topk()
    #posts=RP.distinct_posts()
    #Jaccard=np.zeros((len(events),len(posts)))
    Jaccard1=np.zeros((len(posts),len(posts)))
    similarity_mat=np.zeros((len(events),len(posts)))
    V=np.zeros((len(events),len(posts)))
    for i in range(len(events)):
        for j in range(len(posts)):
            similarity_mat[i][j]=jaccard_similarity(events[i][1],posts[j][1])
    
    for i in range(len(posts)):
        for j in range(len(posts)):
            Jaccard1[i][j]=jaccard_similarity(posts[i][1],posts[j][1])
            # print Jaccard1[i][j]
     
    list_events=[]   
   # similarity_mat=mat_cloning(Jaccard)
    count=0
    while(True):
        count+=1
        temp_list=cluster_and_isModify(list_events,similarity_mat)
        print temp_list[1]
        if count==no_iter:
            break 
        if not temp_list[1]:
            list_events=temp_list[0]
            
            V=modify_V(list_events,authority)
            similarity_mat=modify_similarity(V,Jaccard1)
            
            continue
        elif temp_list[1]:
            break
        
         
    return temp_list[0]

if __name__ == '__main__':
    #authMatrix, hubMatrix = topk.authority_hub_scores
    #list_events = auto_event_cluster(authMatrix, 100)
    #auto_event_cluster( random_authority(),10)
    list_events=auto_event_cluster(authMatrix,100)
    for k in list_events:
        print k
    #     for i in k:
    #         print posts[i][1]
    
    