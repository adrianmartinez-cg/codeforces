import java.util.LinkedList;
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
        long[] answer = solveA(n,array);
        showAnswer(answer);
    }
    private static long[] solveA(int n, long[] array){
        long[] answer = new long[n];
        long[] predecessors = new long[n];
        int first = 0;
        for(int i = 0 ; i < n ; i++) {
            boolean foundPredecessor = false;
            for (int j = 0; j < n; j++) {
                if (i != j) {
                    if (array[i] == array[j] * 2 || array[i] == array[j] / 3) {
                        predecessors[i] = j;
                        foundPredecessor = true;
                        break;
                    }
                }
            }
            if (!foundPredecessor) {
                answer[0] = array[i];
                first = i;
                predecessors[i] = -1;
            }
        }

        int nextAnswerIndex = 1;
        int nextPredecessorToFind = first;

        for(int k = nextAnswerIndex; k < n; k++){
            for (int i =0; i<n; i++){
                if(predecessors[i] == nextPredecessorToFind){
                    answer[nextAnswerIndex] = array[i];
                    nextPredecessorToFind = i;
                    nextAnswerIndex++;
                    break;
                }
            }
        }
        return answer;
    }

    private static Long[] solve(int n, long[] array){
        LinkedList<Long> answer = new LinkedList<>();
        for(int i=0; i<n;i++){
            for(int j=0; j<n; j++){
                if(i != j){
                    if (array[i] == array[j] * 2 || array[i] == array[j] / 3){

                    }
                }
            }
        }
        return answer.toArray(new Long[0]);
    }

    private static void showAnswer(long[] array){
        for(long number:array){
            System.out.print(number + " ");
        }
        System.out.print("\n");
    }
}
