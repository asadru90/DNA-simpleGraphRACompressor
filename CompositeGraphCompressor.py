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


def unionListCompositeSequential(lst1, lst2):

    final_list = []
    list1Count = len(lst1)
    list2Count = len(lst2)
    i = 0
    print("unionListCompositeSequential Function called!", list1Count, list2Count)
    if list1Count < list2Count:
        for idx in range(0, list1Count):
            temp1 = list(lst1[idx])
            temp1.sort()
            temp1 = repairAlgoDefFunc(temp1)
            temp2 = list(lst2[idx])
            temp2.sort()
            temp2 = repairAlgoDefFunc(temp2)
            temp = temp1 + temp2
            print("List", i, temp1, temp2, len(temp1), len(temp2))
            final_list.append(temp)
            i += 1
        for idx in range(i, list2Count):
            temp = list(lst2[idx])
            temp.sort()
            print("List", i, temp, len(temp))
            temp = repairAlgoDefFunc(temp)
            final_list.append(temp)
            i += 1
    elif list2Count < list1Count:
        for idy in range(0, list2Count):
            print("asad")
            temp1 = list(lst1[idy])
            temp1.sort()
            temp1 = repairAlgoDefFunc(temp1)
            temp2 = list(lst2[idy])
            temp2.sort()
            temp2 = repairAlgoDefFunc(temp2)
            temp = temp1 + temp2
            print("List", i, temp1, temp2, len(temp1), len(temp2))
            final_list.append(temp)
            i += 1
        for idx in range(i, list1Count):
            temp = list(lst1[idx])
            temp.sort()
            temp = repairAlgoDefFunc(temp)
            print("List", i, temp, len(temp))
            final_list.append(temp)
            i += 1
    else:
        for idx in range(0, list1Count):
            temp1 = list(lst1[idx])
            temp1.sort()
            temp1 = repairAlgoDefFunc(temp1)
            temp2 = list(lst2[idx])
            temp2.sort()
            temp2 = repairAlgoDefFunc(temp2)
            temp = temp1 + temp2
            print("List", i, temp1, temp2, len(temp1), len(temp2))
            final_list.append(temp)
            i += 1
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
            i += 1
        for idx in range(i, list2Count):
            temp = list(set(lst2[idx]))
            temp.sort()
            final_list.append(temp)
    elif list2Count < list1Count:
        for idy in range(0, list2Count):
            temp = list(set(unionLists(lst1[idy], lst2[idy])))
            temp.sort()
            final_list.append(temp)
            i += 1
        for idx in range(i, list1Count):
            temp = list(set(lst1[idx]))
            temp.sort()
            final_list.append(temp)
    else:
        for idx in range(0, list1Count):
            temp = list(set(unionLists(lst1[idx], lst2[idx])))
            temp.sort()
            final_list.append(temp)
            i += 1
    return final_list


def countMostDictInit(nxtTerm):
    for idx in range(0, nxtTerm + 1):
        for idy in range(0, nxtTerm + 1):
            countMostPairDict[(idx, idy)] = 0


def findMostPair(rePairList, nxtTerm):
    flag = 0;
    fprev = 0;
    fTerm = 0;
    sTerm = 0;
    countDuplicate = 0
    edgeListCount = len(rePairList)
    if edgeListCount > 1:
        for idx in range(0, edgeListCount - 1):
            fTerm = rePairList[idx]
            sTerm = rePairList[idx + 1]
            if (fTerm == sTerm):
                countDuplicate = countDuplicate + 1
                if countDuplicate < 2:
                    inc = countMostPairDict[(fTerm, sTerm)]
                    countMostPairDict[(fTerm, sTerm)] = inc + 1
                else:
                    countDuplicate = 0
            else:
                inc = countMostPairDict[(fTerm, sTerm)]
                countMostPairDict[(fTerm, sTerm)] = inc + 1
                countDuplicate = 0

    findMaxCount = 0;
    prevMaxCount = 0
    for idx in range(1, nxtTerm + 1):
        for idy in range(1, nxtTerm + 1):
            nextMax = countMostPairDict[(idx, idy)]
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
        for idx in range(0, len(rePairList) - 1):
            if flag == 1:
                flag = 0
                continue
            else:
                if fTerm == rePairList[idx] and sTerm == rePairList[idx + 1]:
                    rePairListTemp.append(lTerm)
                    flag = 1
                else:
                    rePairListTemp.append(rePairList[idx])
                    flag = 0
        if flag == 0:
            rePairListTemp.append(rePairList[idx + 1])
        return rePairListTemp
    return rePairList


def produceInputList(vertexCount):
    repairList = []
    # asking number of vertices to put in list
    edgeCount = 0
    countReplace = 0
    singleEdgesList = []

    # iterating till vertexCount to append all the elements of every adjacency list into single list
    for i in range(1, vertexCount + 1):
        numEdgeList = int(math.ceil(randrange(vertexCount)))
        edgeList = []
        edgesList = []
        # repairList.append(-1)
        for j in range(numEdgeList):
            # randomly generate each adjacency list of vertex j
            ele = int(randrange(vertexCount)) + 1
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


def repairAlgoDefForAll(edgeList):
    newEdgeList = []
    print(len(edgeList))
    for idx in edgeList:
        for i in range(0, len(idx) - 1):
            for j in range(i + 1, len(idx)):
                    idx[j] = idx[j] - idx[i]
        newEdgeList.append(idx)
    return newEdgeList

def repairAlgoDefFunc(edgeList):
    newEdgeList = edgeList
    totalLen = len(edgeList)
    #print("Edges List:", edgeList)
    for i in range(1, totalLen):
        j = i + 1
        prev = edgeList[totalLen-j]
        next = edgeList[totalLen-i]
        newEdgeList[totalLen-i] = next - prev
    return newEdgeList


def repairAlgoDictFunc(repairList, vertexCount, edgeCount, maxPairLimit):
    maxPairCount = []
    dictRules = []
    nextNum = vertexCount
    bitsPerInt = math.ceil(math.log2(vertexCount))
    maxBinaryNum = pow(2, bitsPerInt) 

    print("Repair Algorithms Running!...")
    # Replace the common pair of edges with dictionary rules

    maxPair = maxPairLimit + 1
    while (maxPair > maxPairLimit) and (nextNum < maxBinaryNum):

        maxCount = 0
        countMostDictInit(nextNum + 1)
        for edgList in repairList:
            firstNT, secNT, maxPair = findMostPair(edgList, nextNum)

        if maxPair > 1:
            nextNum = nextNum + 1
            dictRules.append((nextNum, firstNT, secNT))
            print(nextNum, firstNT, secNT, maxPair)

        count = 0
        repairTempList = []
        for edgList in repairList:
            edgList = replaceListWithTerminal(edgList, nextNum, firstNT, secNT)
            repairTempList.append(edgList)

        # print (repairTempList)
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
        elif srcVertx == i + 1:
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


def printCompositeGraphResults(remList, dictRules, vertexCount, edgeCount, representAM, representAL, compositeGraphsCount):

    print("============= Composite Graph Dataset Results ============")
    countIntRemList = 0
    bitsPerInt = math.ceil(math.log2(vertexCount))
    for edgList in remList:
        countIntRemList = countIntRemList + len(edgList)
    totalIntCount = len(dictRules) * 2 + countIntRemList
    representCGB = (totalIntCount * bitsPerInt) + edgeCount
    representCGA = (edgeCount * compositeGraphsCount)
    representCG  = representCGB + representCGA

    print("Edges Count:", edgeCount)
    print("Vertex Count:", vertexCount)
    print("BitsPerInteger:", bitsPerInt)
    print("Dict Rules Count:", len(dictRules))
    print("Remaining List Count:", countIntRemList)
    print("Total Integer Count:", totalIntCount)
    print("Edges/Vertex ratio:", edgeCount / vertexCount)
    print("Composite graph represent Before:", representCGB, "bits")
    print("Composite graph represent After:", representCGA, "bits")
    print(len(dictRules) * 2 * bitsPerInt, countIntRemList * bitsPerInt, vertexCount, countIntRemList)
    print("Total AM required:", representAM, "bits")
    print("Total AL required:", representAL, "bits")
    print("Total CG required:", representCG, "bits")
    print("AM/CG Compression Ratio:", representAM / representCG, "bits")
    print("AL/CG Compression Ratio:", representAL / representCG, "bits")
    print("============= Graph Dataset Results ============")

def printSingleGraphResults(datasetNamePath, edgeCount, vertexCount):
    print("============= Sinlge Graph Dataset Results ============")
    bitsPerInt = math.ceil(math.log2(vertexCount))
    representAL = (vertexCount + edgeCount) * bitsPerInt
    representAM = vertexCount * vertexCount
    print("Dataset Name:", datasetNamePath)
    print("BitsPerInteger:", bitsPerInt)
    print("Edges Count:", edgeCount)
    print("Vertex Count:", vertexCount)
    print("Edges/Vertex ratio:", edgeCount / vertexCount)
    print("Total AM required:", representAM, "bits")
    print("Total AL required:", representAL, "bits")
    print("AM/AL Compression Ratio:", representAM/representAL, "bits")
    print("============= Graph Dataset Results ============")
    return representAL, representAM

def dataCleaningForPPINetwork(mypath):
    i = 1
    j = 1
    rows = []
    proteinNodeDict = {}

    file = open(mypath)
    csvreader = csv.reader(file)
    for row in csvreader:
        if j == 1:
            string = ''.join(map(str, row))
            newRow = string.split('#')
            j = j + 1
        else:
            string = ','.join(map(str, row))
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
            string = ''.join(map(str, row))
            newRow = string.split('#')
            j = j + 1
        else:
            string = ','.join(map(str, row))
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
            string = ''.join(map(str, row))
            newRow = string.split('#')
            j = j + 1
        else:
            string = ','.join(map(str, row))
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
        string = ''.join(map(str, row))
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
        string = ''.join(map(str, row))
        newRow = string.split('\t')
        if i > 1:
            node = int(newRow[1])
            edge = int(newRow[0])
            rows.append([node, edge])
    file.close()
    return rows

def checkCommonEdges(edgeList1, edgeList2, edgeCount1, edgeCount2):
    compositeEdgesList = []
    compositeEdgesList = unionListObjects(edgeList1, compositeEdgesList)
    compositeEdgesList = unionListObjects(edgeList2, compositeEdgesList)
    totalEdgesCount = edgeCount1 + edgeCount2
    totalEdgesSumCount = edgesCountList(compositeEdgesList)
    commonEdgesSumCount = totalEdgesCount - totalEdgesSumCount
    print(totalEdgesSumCount, edgeCount1, edgeCount2, commonEdgesSumCount)
    print("#####################################################################")


if __name__ == "__main__":

    compositeGraphsCount = 2
    compositeCount = 0
    maxPairLimit = 1
    datasetsPath = r"D:\Datasets\PPINetworkAnalysis-master\data"
    datasetNamePath = ["","","","",""]
    rows = [0,0,0,0,0]
    edgeList = [[],[],[],[],[]]
    vertexCount = [0, 0, 0, 0, 0]
    edgeCount = [0, 0, 0, 0, 0]
    compositeEdgesList = []
    totalEdgesCount = 0
    totalVertexCount = 0
    totalBitsAM = 0
    totalBitsAL = 0
    bitsAM = [0, 0, 0, 0, 0]
    bitsAL = [0, 0, 0, 0, 0]

    datasetsNameFile = ["Liver-Normal.csv", "Colon-Normal.csv", "Kidney-Normal.csv", "Breast-Normal.csv"]

    compositeEdgesList = []
    for i in range(compositeGraphsCount):
        datasetNamePath[i] = datasetsPath + "\\" + datasetsNameFile[i]
        rows[i] = dataCleaningForPPINetwork(datasetNamePath[i])
        edgeList[i], vertexCount[i] = convertCSVtoList(rows[i])
        edgeCount[i] = edgesCountList(edgeList[i])
        compositeEdgesList = unionListCompositeSequential(edgeList[i], compositeEdgesList)
        totalEdgesCount = totalEdgesCount + edgeCount[i]
        totalVertexCount = max(totalVertexCount, vertexCount[i])
        bitsAL[i], bitsAM[i] = printSingleGraphResults(datasetNamePath[i], edgeCount[i], vertexCount[i])
        totalBitsAM = totalBitsAM + bitsAM[i]
        totalBitsAL = totalBitsAL + bitsAL[i]

    totalEdgesSumCount = edgesCountList(compositeEdgesList)
    #print(totalEdgesSumCount, totalEdgesCount, totalEdgesCount- totalEdgesSumCount)

    remList, dictRules = repairAlgoDictFunc(compositeEdgesList, totalVertexCount, totalEdgesSumCount, maxPairLimit)
    printCompositeGraphResults(remList, dictRules, totalVertexCount, totalEdgesSumCount, totalBitsAM, totalBitsAL, compositeCount)
