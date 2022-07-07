def searchNext(A,visited,answer,j,answerToStr):
    if j == n:
        mapAnswerToStr = map(str,answer)
        answerToStr.append(mapAnswerToStr)
    else:
        for elem in A:
            if not visited.has_key(elem):
                if (answer[j-1] == 3*elem or answer[j-1] == elem/2):
                    answer[j] = elem
                    visited[elem] = True
                    searchNext(A,visited,answer, j+1,answerToStr)

if __name__ == "__main__":
    n = int(raw_input())
    A = list(map(int, raw_input().split(" ")))
    answer = []
    for k in range(n):
        answer.append(0)
    answerToStr = []

    for elem in A:
        answer[0] = elem
        visited = {}
        visited[elem] = True
        searchNext(A,visited,answer,1,answerToStr)

    print " ".join(answerToStr[0])