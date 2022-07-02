import java.util.Arrays;
import java.util.Scanner;

public class Coins {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String inputStr = sc.nextLine();
        String[] numbersAsStr = inputStr.split(" ");
        long[] input = Arrays.stream(numbersAsStr)
                .mapToLong(Long::parseLong)
                .toArray();
        int answer = greedy(input[0],input[1]);
        System.out.println(answer);
    }

    private static int greedy(long n,long s) {
        int[] coins = new int[(int)n];
        for(int i =1; i <= n; i++){
            coins[i-1]=i;
        }
        long sum = 0;
        int coinIndex = coins.length-1;
        int numOfCoins = 0;

        while(sum < s){
            int coin = select(coins,coinIndex,sum,s);
            sum += coin;
            numOfCoins++;
        }

        return numOfCoins;
    }

    private static int select(int[] coins, int i ,long partialSum, long s){
        int maxCoin = coins[i];
        if(partialSum + maxCoin <= s){
            return maxCoin;
        } else {
            return select(coins,i-1,partialSum,s);
        }
    }
}
