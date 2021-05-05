package Dp;
import java.util.*;
public class Subset {
    
    public static Map<Integer,Integer> map = new HashMap<Integer,Integer>();


    public static int fun(int[] arr,int n,int sum){
        if(n ==0 ){
            return 0;
        }
        if(sum <=0){
            return 1;
        }
        if(arr[n-1] <= sum){
            return fun(arr,n-1,sum-arr[n-1]) + fun(arr,n-1,sum);
        }else{
            return fun(arr,n-1,sum);
        }
    }
 
    public static void main(String args[]){
        int arr[] = {1,2,3};
        int target= 5;

        

        System.out.println(fun(arr,arr.length,target));

    }
}
