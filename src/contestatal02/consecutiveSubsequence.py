def printIndexes(indexes):
    toString = ""
    for i in range(len(indexes)-1,-1,-1):
        toString+= str(indexes[i])
        if i != 0:
            toString+=" "
    print(toString)

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

    next = last 
    elemsLeft = k

    for i in range(len(A)-1,-1,-1):
        if(A[i] == next):
            if (elemsLeft > 0):
                indexes.append(i+1)
                next -= 1
                elemsLeft -=1
            else:
                break 
        
    return k , indexes

# Author: Pedro Adrian Pereira
# Problem: Consecutive subsequence

if __name__ == "__main__":
    n = int(input())
    A = list(map(int,input().split()))
    k , indexes = findConsecutiveSubsequence(A,n)
    print(k)
    printIndexes(indexes)