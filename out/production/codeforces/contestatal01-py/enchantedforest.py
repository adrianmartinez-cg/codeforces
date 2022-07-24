# Author : Pedro Adrian
def solve(n,k,A):
    mushrooms = 0
    if(k < n):
        maxSum = maxSubArraySum(A,n,k)
        mushrooms = maxSum + k*(k-1)/2
    else:
        sumOfArray = sumArray(A)
        mushroomsSpawned = n*k
        inacessibleMushrooms = n*(n+1)/2
        mushrooms = sumOfArray + mushroomsSpawned - inacessibleMushrooms
    return mushrooms
    
def sumArray(A):
    subSum = 0
    for i in range(n):
        subSum+=A[i]
    return subSum

def maxSubArraySum(A, n, k):
    result = 0
    for i in range(k):
        result += A[i]
 
    currSum = result
    for i in range(k, n): 
        currSum += A[i] - A[i-k]
        result = max(result, currSum)
    return result
 

if __name__ == "__main__":
    numTestCases = int(input())
    outputValues = []
    for i in range(numTestCases):
        inputStr1 = input("").split(" ") 
        n = int(inputStr1[0])
        k = int(inputStr1[1])
    
        A = list(map(int, input().split(" ")))
    
        partialSolution = solve(n,k,A)
        outputValues.append(int(partialSolution))
    for i in range(len(outputValues)):
        print(outputValues[i])