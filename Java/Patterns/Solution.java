import java.util.Scanner;

public class Solution {
    public static int sumOfAllDivisors(int n){
        // Write your code here.
        int sum = 0;

        for(int i=1;i<=n;i++){
            if(n%i == 0){
                sum = sum + i;
            }
        }

        return  sum;
       
    }


    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n;
        System.out.println("Enter N!");
        n = sc.nextInt();
        int divisorSum=0;

        for(int i=1;i<=n;i++){
            divisorSum = divisorSum + sumOfAllDivisors(i);
        }
        System.out.println(divisorSum);
    }
}