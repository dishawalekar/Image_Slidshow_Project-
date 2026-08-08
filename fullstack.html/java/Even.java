import java.util.Scanner;
public class Even{
    public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the number:");
    int num = sc.nextInt();
    if (num %2 == 0) {
        System.out.println(num + " even number");
    }
    else{
        System.out.println(num + " odd number");
    }

    }
}