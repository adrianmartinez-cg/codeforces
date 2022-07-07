def showRaylor(pop,dur,n,t):
    v = []
    X = [0 for _ in pop]
    rec = {}
    for i in range(len(pop)):
        v.append(pop[i]/dur[i])
    popSorted = [x for _,x in sorted(zip(v,pop),reverse=True)]
    durSorted = [x for _,x in sorted(zip(v,dur),reverse=True)]

    tempo = 0
    i = -1
    while tempo < t:
        i+=1
        if tempo + durSorted[i] <= t:
            X[i] = 1
            tempo += durSorted[i]
        else:
            X[i] = (t-tempo)/durSorted[i]
            tempo = t
        rec[durSorted[i]] = X[i]
    ret = []
    for i in range(n):
        if dur[i] in rec:
            ret.append(rec[dur[i]])
        else:
            ret.append(0)
    return ret

pop = [96,80,45,100,80]
dur = [3,4,5,2,8]
n = 5
t = 15
print(showRaylor(pop,dur,n,t))