
import java.math.*;
public class KnapSack {
    public static int fun(int[] val,int[] wt,int n,int W){
        if(n==0 || W==0){
            return 0;
        }
        if(wt[n-1] <= W){
            return Math.max(val[n-1] + fun(val,wt,n-1,W - wt[n-1]),fun(val,wt,n-1,W));
        }else{
            return fun(val,wt,n-1,W);
        }
    }
    public static void main(String args[]){
        int val[] = new int[]{60,100,120};
        int wt[] = new int[]{10,20,30};
        int W=50;
        int n= val.length;
        System.out.println(fun(val,wt,n,W));
    }
}
