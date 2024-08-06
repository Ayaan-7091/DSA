package Java.Recursion;

public class oneToN {
    
    public static void print(int n,int x,int sum){

           
           if(n>=x){
            sum = sum + n;
            n--;
            print(n,x,sum);
           }
           else if(n<x){
                System.out.println(sum);
           } 

    }
    public static void main(String[] args){

        int n = 15;
        print(n,1,0);
    }
}
