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


def unionListCompositeConcateInterleving(lst1, lst2):

    final_list = []
    list1Count = len(lst1)
    list2Count = len(lst2)
    i = 0
    print("unionListCompositeSequential Function called!", list1Count, list2Count)
    if list1Count < list2Count:
        for idx in range(0, list1Count):
            temp1 = list(lst1[idx])
            temp1.sort()
            #print("List", i, temp1)
            temp1 = repairAlgoDefFunc(temp1)
            temp2 = list(lst2[idx])
            temp2.sort()
            #print("List", i, temp2)
            temp2 = repairAlgoDefFunc(temp2)
            temp = temp1 + temp2
            #print("List", i, temp1, temp2, len(temp1), len(temp2), temp)
            final_list.append(temp)
            i += 1
        for idx in range(i, list2Count):
            temp = list(lst2[idx])
            temp.sort()
            #print("List_B", i, temp, len(temp))
            temp = repairAlgoDefFunc(temp)
            final_list.append(temp)
            #print("List_A", i, temp)
            i += 1
    elif list2Count < list1Count:
        for idy in range(0, list2Count):
            temp1 = list(lst1[idy])
            temp1.sort()
            #print("List", i, temp1)
            temp1 = repairAlgoDefFunc(temp1)
            temp2 = list(lst2[idy])
            temp2.sort()
            #print("List", i, temp2)
            temp2 = repairAlgoDefFunc(temp2)
            temp = temp1 + temp2
            #print("List", i, temp1, temp2, len(temp1), len(temp2), temp)
            final_list.append(temp)
            i += 1
        for idx in range(i, list1Count):
            temp = list(lst1[idx])
            temp.sort()
            #print("List", i, temp)
            temp = repairAlgoDefFunc(temp)
            #print("List", i, temp, len(temp))
            final_list.append(temp)
            i += 1
    else:
        for idx in range(0, list1Count):
            temp1 = list(lst1[idx])
            temp1.sort()
            #print("List", i, temp1)
            temp1 = repairAlgoDefFunc(temp1)
            temp2 = list(lst2[idx])
            temp2.sort()
            #print("List", i, temp2)
            temp2 = repairAlgoDefFunc(temp2)
            temp = temp1 + temp2
            #print("List", i, temp1, temp2, len(temp1), len(temp2), temp)
            final_list.append(temp)
            i += 1
    return final_list


def unionListCompositeConcateAfter(lst1, lst2):

    list1Count = len(lst1)
    list2Count = len(lst2)
    i = 0
    print("unionListCompositeSequential Function called!", list1Count, list2Count)
    for idx in range(0, list2Count):
        temp1 = list(lst2[idx])
        temp1.sort()
        #print("List", i, temp1)
        temp2 = repairAlgoDefFunc(temp1)
        #print("List", i, temp1, temp2, len(temp1), len(temp2), temp)
        lst1.append(temp2)
        i += 1
    return lst1

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
    while (maxPair > maxPairLimit+1) and (nextNum < maxBinaryNum):

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

    return i, edgesList, countVertex


def printSingleGraphResults(remList, dictRules, vertexCount, edgeCount, representAM, representAL):

    countIntRemList = 0
    bitsPerInt = math.ceil(math.log2(vertexCount))
    for edgList in remList:
        countIntRemList = countIntRemList + len(edgList)
    totalIntCount = len(dictRules) * 2 + countIntRemList
    represent1 = (totalIntCount * bitsPerInt)
    represent2 = vertexCount + countIntRemList
    represent3 = represent1 + represent2

    print("============= Single Graph Dataset Results ============")
    print("Edges Count:", edgeCount)
    print("Vertex Count:", vertexCount)
    print("Dict Rules Count:", len(dictRules))
    print("Remaining List Count:", countIntRemList)
    print("Total Integer Count:", totalIntCount)
    print("Edges/Vertex ratio:", edgeCount / vertexCount)
    print("BitsPerInteger:", bitsPerInt)
    print("Bits required for 2*DL+RL integers:", represent1, "bits")
    print("Bits required for |V|+|RL|:", represent2, "bits")
    print("Bits required for ((2*DL+RL)*bitsPerInt)+|V|+|RL|:", represent3, "bits")
    print("Total AM required:", representAM, "bits")
    print("Total AL required:", representAL, "bits")
    print("Total CG required:", represent3, "bits")
    print("AM/CG Compression Ratio:", representAM / represent3, "bits")
    print("AL/CG Compression Ratio:", representAL / represent3, "bits")
    print("============= Single Graph Dataset Results ============")

def printCompositeGraphResults(remList, dictRules, maxvertexCount, totaledgeCount, representAM, representAL, totalvertexCount):

    countIntRemList = 0
    bitsPerInt = math.ceil(math.log2(maxvertexCount))
    for edgList in remList:
        countIntRemList = countIntRemList + len(edgList)
    totalIntCount = len(dictRules) * 2 + countIntRemList
    represent1 = (totalIntCount * bitsPerInt)
    represent2 = totalvertexCount + countIntRemList
    represent3 = represent1 + represent2

    print("============= Composite Graph Dataset Results ============")
    print("Total Edges Count (Comp)|E|:", totaledgeCount)
    print("Maximum Vertex Count:", maxvertexCount)
    print("Total Vertex Count (Comp)|V|:", totalvertexCount)
    print("Dict Rules Count:", len(dictRules))
    print("Remaining List Count:", countIntRemList)
    print("Total Integer Count:", totalIntCount)
    print("Edges/Vertex ratio:", totaledgeCount / maxvertexCount)
    print("BitsPerInteger:", bitsPerInt)
    print("Bits required for 2*DL+RL integers:", represent1, "bits")
    print("Bits required for (Comp)|V|+(Comp)|E|:", represent2, "bits")
    print("Bits required for ((2*DL+RL)*bitsPerInt)+(Comp)|V|+(Comp)|E|:", represent3, "bits")
    print("Total AM required:", representAM, "bits")
    print("Total AL required:", representAL, "bits")
    print("Total CG required:", represent3, "bits")
    print("AM/CG Compression Ratio:", representAM / represent3, "bits")
    print("AL/CG Compression Ratio:", representAL / represent3, "bits")
    print("============= Composite Graph Dataset Results ============")

def printSimpleCompressionGraphResults(datasetNamePath, edgeCount, vertexCount):
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


def dataCleaningForEnzymes(mypath):
    file = open(mypath)
    csvreader = csv.reader(file)
    rows = []
    i = 0
    for row in csvreader:
        i = i + 1
        string = ''.join(map(str, row))
        newRow = string.split(' ')
        if i > 1:
            node = int(newRow[1])
            edge = int(newRow[0])
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

def dataCleaningForProteinsDataset(mypath, i):
    if i == 0:
        return dataCleaningForProtein(mypath)
    if i == 1:
        return dataCleaningForStudentsNetwork(mypath)

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
    maxPairLimit = 2
    datasetsPath = r"D:\PhDGoetheUni\Works\NEXTConference22\Datasets\ProteinDataset"
    datasetNamePath = ["","","","",""]
    rows = [0,0,0,0,0]
    edgeList = [[],[],[],[],[]]
    vertexCount = [0, 0, 0, 0, 0]
    edgeCount = [0, 0, 0, 0, 0]
    compositeEdgesList = []
    totalEdgesCount = 0
    totalVertexCount = 0
    maxVertexCount = 0
    totalNonEmptyListCount = 0

    totalBitsAM = 0
    totalBitsAL = 0
    bitsAM = [0, 0, 0, 0, 0]
    bitsAL = [0, 0, 0, 0, 0]

    datasetsNameFile = ["Liver-Cancer.csv", "Breast-Cancer.csv", "Kidney-Normal.csv", "Breast-Normal.csv"]

    compositeEdgesList = []
    j = 0
    for i in range(compositeGraphsCount):
        datasetNamePath[i] = datasetsPath + "\\" + datasetsNameFile[i]
        if i == 1:
            rows[i] = dataCleaningForPPINetwork(datasetNamePath[i])
        else:
            rows[i] = dataCleaningForPPINetwork(datasetNamePath[i])
        nonEmptyVertexListCount, edgeList[i], vertexCount[i] = convertCSVtoList(rows[i])
        edgeCount[i] = edgesCountList(edgeList[i])
        compositeEdgesList = unionListCompositeConcateAfter(compositeEdgesList, edgeList[i])
        totalEdgesCount = totalEdgesCount + edgeCount[i]
        totalVertexCount = totalVertexCount + vertexCount[i]
        maxVertexCount = max(maxVertexCount, vertexCount[i])
        bitsAL[i], bitsAM[i] = printSimpleCompressionGraphResults(datasetNamePath[i], edgeCount[i], vertexCount[i])
        totalBitsAM = totalBitsAM + bitsAM[i]
        totalBitsAL = totalBitsAL + bitsAL[i]
        j = j + 1
        totalNonEmptyListCount = totalNonEmptyListCount + nonEmptyVertexListCount

    totalEdgesSumCount = edgesCountList(compositeEdgesList)
    print("Total Edges Count:", totalEdgesSumCount, totalEdgesCount, totalEdgesCount - totalEdgesSumCount)
    print("Empty Vertex List Count:", "Total:", totalVertexCount, "Total Non-empty:", totalNonEmptyListCount,
          "Total Empty:", totalVertexCount - totalNonEmptyListCount, "Total required bits:",
          maxVertexCount + (2 * (totalVertexCount - totalNonEmptyListCount)))
    if compositeGraphsCount > 1:
        totalVertexCount = maxVertexCount + (2 * (totalVertexCount - totalNonEmptyListCount))

    remList, dictRules = repairAlgoDictFunc(compositeEdgesList, maxVertexCount, totalEdgesSumCount, maxPairLimit)
    if compositeGraphsCount == 1:
        printSingleGraphResults(remList, dictRules, totalVertexCount, totalEdgesSumCount, totalBitsAM, totalBitsAL)
    else:
        printCompositeGraphResults(remList, dictRules, maxVertexCount, totalEdgesSumCount, totalBitsAM,
                                       totalBitsAL, totalVertexCount)
