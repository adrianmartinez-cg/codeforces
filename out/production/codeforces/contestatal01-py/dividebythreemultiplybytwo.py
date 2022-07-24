def divByThree(num):
    res = 0
    while(num%3 == 0):
        res+=1
        num /= 3
    return res

if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    A.sort(key = lambda x : (divByThree(x), -x ),reverse = True)
    print(" ".join(list(map(str,A))))