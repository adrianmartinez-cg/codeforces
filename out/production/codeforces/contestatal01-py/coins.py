def greedyAlg(n,s):
    coins = []
    for k in range(1,n+1):
        coins.append(k)
    sum = 0
    nextCoinIndex = len(coins)-1
    numOfCoins = 0
    while(sum < s):
        nextCoin = coins[nextCoinIndex]
        if(sum + nextCoin <= s):
            sum += nextCoin
            numOfCoins += 1
        else:
            nextCoinIndex = (s-sum)-1 
            nextCoin = coins[coinIndex]
            sum += nextCoin 
            numOfCoins += 1
    return numOfCoins     

inputStr = input ("")
input = inputStr.split(" ")
answer = greedyAlg(int(input[0]), int(input[1]))
print(answer)