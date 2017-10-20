
import java.util.Scanner;


public class Labtask {
    public static void main(String[] args) {
        String myString;
    int c = 0;

    Scanner scan = new Scanner(System.in);

    System.out.println("Please enter a string.");
    myString = scan.nextLine();

    while(c < myString.length())
    {
        System.out.println("" + myString.charAt(c));
        c ++;


    }
    }
    
}
