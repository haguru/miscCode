#!/usr/bin/pyhton

from sklearn.metrics import mean_squared_error
from random import randint
import string

letters = string.letters + " "
RAND_MAX = 2147483647

def rand():
    return randint(0,RAND_MAX)

class candidate:
    def __init__(self,cstr,target):
        self.target = target
        self.cstr = cstr
        self.error = self.cost()

    def cost(self):
        yt,yp = [],[]
        if len(self.cstr)== len(self.target):
            for char in range(len(self.cstr)):
                yt.append(ord(self.target[char]))
                yp.append(ord(self.cstr[char]))
        error =  mean_squared_error(yt,yp)
        return error


def neighborHood(tabuList, candidateSize,target):
    Clist = []
    flag = False
    for i in range(candidateSize):
        char = rand()%len(target)
        cstrX = rand()%len(tabuList)
        cstr = tabuList[cstrX].cstr
        while target[char] == cstr[char]:
            char = rand()%len(target)
        cstr = list(cstr)
        cstr[char] = chr((rand()%90) +32) #letters[(rand()%(len(letters)))]
        cstr = "".join(cstr)
        for j in tabuList:
            if cstr == j:
                flag = True
                break
        if flag == False:
            Clist.append(candidate(cstr,target))
    return Clist

def locateBest(candidateList):
    newList = sorted(candidateList, key=lambda candidate: candidate.error)
    return newList[0]


def tabuSearch(tabuListSize,candidateSize,target):
    cstr = ""
    for char in target:
        cstr = cstr + letters[(rand()%(len(letters)))]
    bestCandidate = candidate(cstr,target)
    tabuList = [bestCandidate]
    candidateList = []
    itr = 0
    while bestCandidate.error !=0:
        print "Error: ",bestCandidate.error, " cstr = ",bestCandidate.cstr
        candidateList = neighborHood(tabuList,candidateSize,target)
        tempCandidate = locateBest(candidateList)
        if tempCandidate.error < bestCandidate.error:
            bestCandidate = tempCandidate
            tabuList.append(tempCandidate)
            while len(tabuList) > tabuListSize:
                tabuList.pop()
        print "Error: ",bestCandidate.error, " cstr = ",bestCandidate.cstr, "iteration: ",itr
        itr+=1


tabuSearch(100,1000)
