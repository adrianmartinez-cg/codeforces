def printIndexes(indexes):
    toString = ""
    for i in range(len(indexes)):
        toString+= str(indexes[i])
        if i != len(indexes) - 1:
            toString+=" "
    return toString

def findConsecutiveSubsequence(A,n):
    maxSsElem = {} # Holds the value of the maximum subsequence that can be formed with a certain element of A
    k = 0
    indexes = []
    last = 0

    for elem in A:
        if (elem - 1) in maxSsElem:
            maxSsElem[elem] = maxSsElem[elem-1] + 1
        else:
            maxSsElem[elem] = 1
        if maxSsElem[elem] > k:
            k = maxSsElem[elem]
            last = elem

    for index in range(last-k+1,last+1):
        indexes.append(index)
    
    return k,indexes

# Author: Pedro Adrian Pereira
# Problem: Consecutive subsequence

if __name__ == "__main__":
    n = int(input())
    A = list(map(int,input().split()))
    k , indexes = findConsecutiveSubsequence(A,n)
    print(k)
    printIndexes(indexes)