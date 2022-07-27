#Para printar a resposta
def printDepths(depths):
    for depth in depths:
        toString = ""
        for i in range(len(depth)): 
            toString+=str(depth[i])
            if i != len(depth) - 1:
                toString+=" "
        print(toString)

# Encontra o indice do elemento máximo de um intervalo, e soma com um deslocamento d,
# para retornar qual o indice do mesmo no array original
def findMax(A,d):
    maxIndex = 0
    maxValue = -1
    for i in range(len(A)):
        if A[i] > maxValue:
            maxValue = A[i]
            maxIndex = i 
    return maxIndex + d

# A - Array , n - n de elems. , k - profundidade atual , depths - profundidades dos nos
# d - deslocamento a ser considerado ao fazer a chamada do metodo para um array "filho" 
# a direita
def permutationTransform(A,n,k,depths,d=0):
    maxIndex = findMax(A,d)
    depths[maxIndex] = k # registra a profundidade do nó em depths
    maxIndexLocal = maxIndex - d # indice do elemento no array da chamada atual
    left = A[0:maxIndexLocal]
    if(len(left) > 0):
        permutationTransform(left,len(left),k+1,depths,d)
    right = A[maxIndexLocal+1:n]
    if(len(right)>0):
        permutationTransform(right,len(right),k+1,depths,maxIndex+1)

#Autor : Pedro Adrian Pereira
if __name__ == "__main__":
    t = int(input())
    depthsList = []
    for _ in range(t):
        n = int(input())
        A = list(map(int,input().split()))
        depths = [0 for elem in A]
        permutationTransform(A,n,0,depths)
        depthsList.append(depths)
    printDepths(depthsList)