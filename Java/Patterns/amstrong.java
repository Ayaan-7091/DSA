import java.util.Scanner;

public class amstrong {

    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter N! : ");
        int n =sc.nextInt();
        int temp = n;
        String tempStr = Integer.toString(n);
        int length = tempStr.length();
        int result = 0;

        while(n>0){
            int x = n%10;
            double number =  Math.pow(x, length);
            System.out.println(number);           
            result = result + (int)number;
            n=n/10;
        }
        System.out.println(result);
        if(temp == result){
            System.out.println(true);
        }else{
            System.out.println(false);
        }
        
    }
    
}
