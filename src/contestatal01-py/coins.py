def greedy(n,s):
    coins = []
    for i in range(1,n+1):
        coins.append(i)
    sum = 0
    coinIndex = len(coins)-1
    numOfCoins = 0
    while(sum < s):
        nextCoin = coins[coinIndex]
        if(sum + nextCoin <= s):
            sum += nextCoin
            numOfCoins += 1
        else:
            diff = s-sum 
            nextCoin = coins[diff-1]
            sum += nextCoin 
            numOfCoins += 1
    return numOfCoins     

if __name__ == "__main__":
    inputStr = input ("")
    input = inputStr.split(" ")
    answer = greedy (int(input[0]), int(input[1]))
    print(answer)