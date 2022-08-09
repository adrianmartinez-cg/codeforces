import math
def findGoodSubSeq(A,n,divideBy):
    M = [0 for _ in range((10**6)+1)]

    M[0] = 1
    M[1] = 1

    for i in range(2,n+1):
        indexesToUpdate = []

        for j in range(1,int(math.sqrt(A[i]))+1):
            if(A[i] % j == 0):
                indexesToUpdate.append(j)
                if((A[i]//j) != j):
                    indexesToUpdate.append(int(A[i]//j))
                    
    indexesToUpdate.sort(reverse=True)

    for j in indexesToUpdate:
        M[j] += M[j-1]
        M[j] %= divideBy

    count = 0 
    for i in range(1,n+1):
        count = (count+M[i])%divideBy
    
    return count

#Autor: Pedro Adrian Pereira Martinez
if __name__ == "__main__":
    divideBy = 10**9 + 7
    n = int(input())
    A = list(map(int,input().split()))
    A.insert(0,0)
    numberSubSeq = findGoodSubSeq(A,n,divideBy)
    print(numberSubSeq)