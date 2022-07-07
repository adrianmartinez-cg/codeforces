def exchange(A,B):
    values = []
    sumA = sum(A)
    sumB = sum(B)
    for i in range(len(A)):
        elemA = A[i]
        for j in range(len(B)):
            elemB = B[j]
            nextSumA = sumA - elemA + elemB
            nextSumB = sumB - elemB + elemA 
            if(nextSumA == nextSumB):
                values = [elemA,elemB]
                break 
        if len(values) > 0: break 
    return values 

print(exchange([0,2,2],[1,2,3]))
print(exchange([1,2,3],[4,5]))
print(exchange([2,3,4],[1,2,3,3]))
print(exchange([1,5],[3,3]))    