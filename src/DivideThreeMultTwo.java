import java.util.Scanner;
import java.util.Arrays;

public class DivideThreeMultTwo {
    /*
    Your problem is to rearrange (reorder) elements of this sequence in such a way that
    it can match possible Polycarp's game in the order of the numbers written on the board.
    I.e. each next number will be exactly two times of the previous number or exactly one third
    of previous number.
    It is guaranteed that the answer exists.
     */
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // Input 1
        sc.nextLine();
        String arrayAsStr = sc.nextLine(); // Input 2
        String[] arrayNumsStr = arrayAsStr.split(" ");
        int[] array = Arrays.stream(arrayNumsStr)
                            .mapToInt(Integer::parseInt)
                            .toArray();
        int[] answer = solve(n,array);
        System.out.println(Arrays.toString(answer));

    }
    private static int[] solve(int n, int[] array){
        int[] answer = new int[n];
        int[] antecessors = new int[n];
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
}
