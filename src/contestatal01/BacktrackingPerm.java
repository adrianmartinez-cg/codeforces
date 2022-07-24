package contestatal01;

import java.util.Arrays;

public class BacktrackingPerm {
    public static void main(String[] args){
        int[] A = new int[]{1,2,3};
        int[] X = new int[]{-1,-1,-1};
        perm(X,A,0);
    }
    private static void perm(int[] X, int[] A, int i ){
        int n = A.length;
        if(i == n){
         System.out.println(Arrays.toString(X));
        }
        else{
            for(int j=0; j < n; j++){
                if(isValid(X,A[j])){
                    X[i] = A[j];
                    perm(X,A,i+1);
                }
            }
        }
    }

    private static boolean isValid(int[] X, int elem){
        for (int e : X){
            if(e==elem) {
                return false;
            }
        }
        return true;
    }

}
