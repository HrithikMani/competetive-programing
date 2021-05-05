package Recursion;

public class Brackets {
    public static void fun(char[] a, int pos, int open,int close, int n){
        if(close == n){
            for(char i:a){
                System.out.print(i);
            }
            System.out.println();
            return;
        }

        if(open>close){
            a[pos]=']';
            fun(a,pos+1,open,close+1,n);
        }
        if(open<n){
            a[pos]='[';
            fun(a,pos+1,open+1,close,n);
        }


    }
    public static void main(String args[]){
        int n=3;
        char[] a = new char[n*2];
        fun(a,0,0,0,n);
    }   
}
