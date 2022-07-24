def isValid(X,elem):
    for x in X:
        if x == elem:
            return False
    return True

def perm(X,A,i):
    n = len(A)
    if i == n:
        print(X)
    else:
        for j in range(n):
            if isValid(X,A[j]):
                X[i] = A[j]
                perm(X.copy(),A,i+1)

A = [1,2,3]
X = [-1,-1,-1]
perm(X,A,0)