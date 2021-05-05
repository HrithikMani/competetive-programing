
import java.math.*;
import java.util.*;

public class KnapSack {
    public static void display(int[][] a){
        for(int i=0;i<a.length;i++){
            for(int j=0;j<a[0].length;j++){
                System.out.print(a[i][j]+" ");
            }
            System.out.println();
        }
    }

    public static int fun(int[] val,int[] wt,int n,int W,int[][] dp){
        display(dp);
        if(n==0 || W==0){
            return 0;
        }
        if(dp[n][W] != 0){
            return dp[n][W];
        }
        if(wt[n-1] <= W){
            dp[n][W] = Math.max(val[n-1] + fun(val,wt,n-1,W - wt[n-1],dp),fun(val,wt,n-1,W,dp));
            return dp[n][W];
        }else{
            dp[n][W] = fun(val,wt,n-1,W,dp);
            return dp[n][W];
        }
    }
    public static void main(String args[]){
        int val[] = new int[]{60,100,120};
        int wt[] = new int[]{10,20,30};
        int W=10;
        int n= val.length;

        int[][] dp =new int[n+1][W+1];

        System.out.println(fun(val,wt,n,W,dp));
    }
}
