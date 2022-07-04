def procura_proximo(resp, visitados, c):
    if c == n:
        final.append(map(str, resp))
        return

    for e in array:
        if e not in visitados and (e*3 == resp[c-1] or resp[c-1]*2 == e):
            resp[c] = e
            procura_proximo(resp, visitados.union({e}), c+1)


n = int(input())

array = list(map(int, input().split(" ")))
r = [0 for _ in range(n)]
final = []

for e in array:
    v = {e}
    r[0] = e
    procura_proximo(r, v, 1)


print (" ".join(final[0]))