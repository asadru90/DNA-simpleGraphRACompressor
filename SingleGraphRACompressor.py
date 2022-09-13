
import csv
from random import randrange
import math
from pathlib import Path
import os

compositEdgesList = []
countMostPairDict = {}

def unionLists(lst1, lst2):
    final_list = lst1 + lst2
    return final_list
    
def unionListObjects(lst1, lst2):
    final_list = []
    list1Count = len(lst1)
    list2Count = len(lst2)
    i = 0
    if list1Count < list2Count:
        for idx in range(0, list1Count):
            temp = list(set(unionLists(lst1[idx], lst2[idx])))
            temp.sort()
            final_list.append(temp)
            i+=1
        for idx in range(i, list2Count):
            temp = list(set(lst2[idx]))
            temp.sort()
            final_list.append(temp)
    elif list2Count < list1Count:
        for idy in range(0, list2Count):
            temp = list(set(unionLists(lst1[idy], lst2[idy])))
            temp.sort()
            final_list.append(temp)
            i+=1
        for idx in range(i, list1Count):
            temp = list(set(lst1[idx]))
            temp.sort()
            final_list.append(temp)
    else:
        for idx in range(0, list1Count):
            temp = list(set(unionLists(lst1[idx], lst2[idx])))
            temp.sort()
            final_list.append(temp)
            i+=1
    return final_list
    
def countMostDictInit(nxtTerm):
  for idx in range(1, nxtTerm+1):
    for idy in range(1, nxtTerm+1): 
        countMostPairDict[(idx,idy)] = 0  

def findMostPair(rePairList, nxtTerm):
    flag = 0; fprev = 0; fTerm = 0; sTerm = 0; countDuplicate = 0
    edgeListCount = len(rePairList)
    if edgeListCount > 1:
        for idx in range(0, edgeListCount-1):
            fTerm = rePairList[idx] 
            sTerm = rePairList[idx+1]
            if (fTerm == sTerm):
                countDuplicate = countDuplicate + 1
                if countDuplicate < 2:
                    inc = countMostPairDict[(fTerm,sTerm)]
                    countMostPairDict[(fTerm,sTerm)] = inc+1
                else:
                    countDuplicate = 0
            else:
                inc = countMostPairDict[(fTerm,sTerm)]
                countMostPairDict[(fTerm,sTerm)] = inc+1
                countDuplicate = 0
                
                
    findMaxCount = 0; prevMaxCount = 0
    for idx in range(1, nxtTerm+1):
        for idy in range(1, nxtTerm+1):
            nextMax = countMostPairDict[(idx,idy)]
            if nextMax > prevMaxCount:
                prevMaxCount = nextMax
                fTerm = idx
                sTerm = idy
    return (fTerm, sTerm, prevMaxCount)
            
    
def replaceListWithTerminal(rePairList, lTerm, fTerm, sTerm):
    flag = 0
    rePairListTemp = []
    edgeListCount = len(rePairList)
    if edgeListCount > 1:
        for idx in range(0, len(rePairList)-1):
            if flag == 1:
                flag = 0
                continue
            else:
                if fTerm == rePairList[idx] and sTerm == rePairList[idx+1]:
                    rePairListTemp.append(lTerm)
                    flag = 1
                else:
                    rePairListTemp.append(rePairList[idx])
                    flag = 0
        if flag == 0:
            rePairListTemp.append(rePairList[idx+1])
        return rePairListTemp
    return rePairList
    
def produceInputList(vertexCount):
    
    repairList = [] 
    # asking number of vertices to put in list
    edgeCount = 0
    countReplace = 0
    singleEdgesList = []

    # iterating till vertexCount to append all the elements of every adjacency list into single list
    for i in range(1, vertexCount+1):
        numEdgeList = int(math.ceil(randrange(vertexCount)))
        edgeList = []
        edgesList = []
        #repairList.append(-1)
        for j in range(numEdgeList):
            #randomly generate each adjacency list of vertex j
            ele = int(randrange(vertexCount))+1
            if ele not in edgeList:
                edgeCount = edgeCount + 1;                   
                edgeList.append(ele)
        edgeList.sort()
        repairList.append(edgeList)
    return repairList, edgeCount
  

def edgesCountList(edgeList):
    edgesCount = 0 
    for idx in edgeList:
        edgesCount = edgesCount + len(idx)
    return edgesCount
    
def repairAlgoDefFunc(edgeList):
    newEdgeList = []
    for idx in edgeList:
        for i in range(0, len(idx)-1):
            for j in range(i+1, len(idx)):
                idx[j] = idx[j] - idx[i]
        newEdgeList.append(idx)
    return newEdgeList
        
def repairAlgoDictFunc(repairList, vertexCount, edgeCount, maxPairLimit):
        
    maxPairCount = []
    dictRules = []
    nextNum = vertexCount

    print ("Repair Algorithms Running!...")
    #Replace the common pair of edges with dictionary rules
    
    maxPair = maxPairLimit + 1
    while maxPair > maxPairLimit:
        
        maxCount = 0
        countMostDictInit(nextNum+1)
        for edgList in repairList:
                firstNT,secNT,maxPair = findMostPair(edgList, nextNum)
                
        if maxPair > 1:
            nextNum = nextNum + 1
            dictRules.append((nextNum,firstNT,secNT))
            print (nextNum, firstNT,secNT,maxPair)
 
        count = 0
        repairTempList = []
        for edgList in repairList:
            edgList = replaceListWithTerminal(edgList, nextNum, firstNT, secNT)
            repairTempList.append(edgList)
        
        #print (repairTempList)  
        repairList = repairTempList 
        maxPairCount = []
    return repairList, dictRules

def convertCSVtoList(rows):
  edgeList = []
  edgesList = []
  i = 1
  countVertex = 0
  srcVertx = 0

  for row in rows:
      srcVertx = int(row[0])
      dstVertx = int(row[1])
      countVertex = max(countVertex, srcVertx, dstVertx)

      if srcVertx == i:
        edgeList.append(dstVertx)
      elif srcVertx == i+1:
        edgesList.append(edgeList)
        edgeList = []
        edgeList.append(dstVertx)
        i = i + 1
      else:
        edgesList.append(edgeList)
        while i < srcVertx:
          edgesList.append([])
          i = i + 1
        edgeList.append(dstVertx)
 
  return edgesList, countVertex


def printResults (datsetNamePath, repairList, vertexCount, edgeCount, edgeSumCount, dictRules, totalListCount):
    #printing the output results
    countTotalInt = 0; countRemList = 0
    nextNum = len(dictRules) + vertexCount
    for edgList in repairList:
        countRemList = countRemList + len(edgList)
    countTotalInt = len(dictRules)*2 + countRemList
    print ("=========================")
    print ("Dataset Name:", datsetNamePath)
    print ("Total graphs:", totalListCount)
    print ("Vertices per graph:", vertexCount)
    print ("Total edges:", edgeCount)
    print ("Composit edges:", edgeSumCount)
    print ("Edges/Vertex ratio:", edgeCount/(vertexCount*totalListCount))
    print ("Remaining list:", countRemList)
    print ("Dictionary rules:", len(dictRules))
    print ("Total integers required:", countTotalInt)
    print ("=========================")

    bitsPerIntOrg = math.ceil(math.log2(vertexCount))
    bitsPerIntZip = math.ceil(math.log2(nextNum))
    orignalBits = ((edgeCount+vertexCount)*totalListCount)*bitsPerIntOrg
    
    if totalListCount > 1: 
        compressedBits = ((edgeSumCount*totalListCount) + (countTotalInt* bitsPerIntOrg) + vertexCount + countRemList)
    else:
        compressedBits = ((countTotalInt* bitsPerIntOrg) + vertexCount + countRemList)

    print ("Bits per integer:", bitsPerIntOrg, "bits")
    print ("Total AL required bits:", orignalBits, "bits")
    print ("Total compression required bits:", compressedBits, "bits")
    print ("AL Compression ratio:", orignalBits/compressedBits, "times")
    print ("Total AM required bits:", vertexCount*vertexCount*totalListCount, "bits")
    print ("AM Compression ratio:", vertexCount*vertexCount*totalListCount/compressedBits, "times")
    print ("=========================")
    #print(repairList)
    #print(dictRules)


def dataCleaningForPPINetwork(mypath):

    i = 1
    j = 1
    rows = []
    proteinNodeDict = {}
    
    file = open(mypath)
    csvreader = csv.reader(file)
    for row in csvreader:
        if j == 1:
            string =''.join(map(str,row))
            newRow = string.split('#')
            j = j + 1
        else:
            string =','.join(map(str,row))
            newRow = string.split(',')
            if (proteinNodeDict.get(newRow[0]) == None):
                proteinNodeDict[newRow[0]] = i 
                i = i + 1 
    file.close() 

    j = 1
    file = open(mypath)
    csvreader = csv.reader(file)
    for row in csvreader:
        if j == 1:
            string =''.join(map(str,row))
            newRow = string.split('#')
            j = j + 1
        else:
            string =','.join(map(str,row))
            newRow = string.split(',')
            if (proteinNodeDict.get(newRow[1]) == None):
                proteinNodeDict[newRow[1]] = i 
                i = i + 1
    file.close() 

    j = 1
    file = open(mypath)
    csvreader = csv.reader(file)
    for row in csvreader:
        if j == 1:
            string =''.join(map(str,row))
            newRow = string.split('#')
            j = j + 1
        else:
            string =','.join(map(str,row))
            newRow = string.split(',')
            node = int(proteinNodeDict.get(newRow[0]))
            edge = int(proteinNodeDict.get(newRow[1]))
            rows.append([node, edge])  
    file.close() 

    return rows

def dataCleaningForProtein(mypath):

    file = open(mypath)
    csvreader = csv.reader(file)
    rows = []
    i = 0
    for row in csvreader:
      i = i + 1
      string =''.join(map(str,row))
      newRow = string.split('\t')
      if i > 1:
        node = int(newRow[1])
        edge = int(newRow[0])
        rows.append([node, edge])  
    file.close() 
    return rows

def dataCleaningForStudentsNetwork(mypath):
    file = open(mypath)
    csvreader = csv.reader(file)
    rows = []
    i = 0
    for row in csvreader:
      i = i + 1
      if i > 1:
        node = int(row[0])
        edge = int(row[1])
        if row[2] == 'Partners': 
            rows.append([node, edge])  
    file.close() 
    return rows

def dataCleaningForSparseNeuron(mypath):
    file = open(mypath)
    csvreader = csv.reader(file)
    rows = []
    i = 0
    for row in csvreader:
      i = i + 1
      string =''.join(map(str,row))
      newRow = string.split('\t')
      if i > 1:
        node = int(newRow[1])
        edge = int(newRow[0])
        rows.append([node, edge])  
    file.close() 
    return rows

if __name__ == "__main__":
  
    totalListCount = 1
    maxPairLimit = 1
    datsetNamePath = r"C:\Users\admin\Desktop\Datasets\PPINetworkAnalysis-master\data\Breast-Cancer.csv"

    rows = dataCleaningForPPINetwork(datsetNamePath)
    edgeList, vertexCount = convertCSVtoList(rows)
    
    edgeCount = edgesCountList(edgeList)
    
    compositEdgesList = unionListObjects(edgeList,compositEdgesList)
    edgeSumCount = edgesCountList(compositEdgesList)

    defEdgeList = repairAlgoDefFunc(compositEdgesList)
    remList, dictRules = repairAlgoDictFunc(defEdgeList, vertexCount,edgeCount, maxPairLimit)

    printResults (datsetNamePath, remList, vertexCount, edgeCount, edgeSumCount, dictRules, totalListCount)   
