package Java.Recursion;

import java.util.Scanner;

public class printNTimes {


    public static void printN(int n){

        if(n>0){
        System.out.println(n);
        n--;
        printN(n);
        }
        
    }
    
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int temp = n;
        printN(n);

        
}
}


