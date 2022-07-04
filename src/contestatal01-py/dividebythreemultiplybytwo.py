def searchNext(visited,answer,i,n):
    if i == n:
        mappedToStr = [str(x) for x in answer]
        ansToStr.append(mappedToStr)
        return
    else:
        for elem in A:
            if elem not in visited: 
                if (answer[i-1] == 3*elem or answer[i-1]== elem/2):
                    answer[i] = elem
                    searchNext(visited.union({elem}),answer, i+1, n)


n = int(input())
arrayAsStr = input().split()
A = [int(x) for x in arrayAsStr]
ans = []
for i in range(n):
    ans.append(0)
ansToStr= []

for elem in A:
    ans[0] = elem
    visited = {elem}
    searchNext(visited,ans,1,n)

print (" ".join(ansToStr[0]))