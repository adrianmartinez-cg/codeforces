import java.util.Scanner;
import java.util.Arrays;

public class DivideThreeMultTwo {
    /*
    Problem:
    Your problem is to rearrange (reorder) elements of this sequence in such a way that
    it can match possible Polycarp's game in the order of the numbers written on the board.
    I.e. each next number will be exactly two times of the previous number or exactly one third
    of previous number.
    It is guaranteed that the answer exists.

    Author : Pedro Adrian
     */
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // Input 1
        sc.nextLine();
        String arrayAsStr = sc.nextLine(); // Input 2
        String[] arrayNumsStr = arrayAsStr.split(" ");
        long[] array = Arrays.stream(arrayNumsStr)
                             .mapToLong(Long::parseLong)
                             .toArray();
        long[] answer = solve(n,array);
        showAnswer(answer);

    }
    private static long[] solve(int n, long[] array){
        long[] answer = new long[n];
        long[] antecessors = new long[n];
        int first = 0;
        for(int i = 0 ; i < n ; i++) {
            boolean foundAntecessor = false;
            for (int j = 0; j < n; j++) {
                if (i != j) {
                    if (array[i] == array[j] * 2 || array[i] == array[j] / 3) {
                        antecessors[i] = j;
                        foundAntecessor = true;
                        break;
                    }
                }
            }
            if (!foundAntecessor) {
                answer[0] = array[i];
                first = i;
                antecessors[i] = -1;
            }
        }
        int subIndexInAnswer = 1;
        int nextIndexToFind = first;

        for(int k = subIndexInAnswer; k < n; k++){
            for (int i =0; i<n; i++){
                if(antecessors[i] == nextIndexToFind){
                    answer[subIndexInAnswer] = array[i];
                    nextIndexToFind = i;
                    subIndexInAnswer++;
                    break;
                }
            }
        }
        return answer;
    }

    private static void showAnswer(long[] array){
        for(long number:array){
            System.out.print(number + " ");
        }
        System.out.print("\n");
    }
}
