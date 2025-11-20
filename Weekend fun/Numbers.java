import java.util.Scanner;
public class Numbers{
    public static void main(String [] args){
    Scanner input = new Scanner(System.in);

    System.out.print("Enter any number (Enter -1 to exit)");
    int number = input.nextInt();


    int zero = 0;
    int negative = 0;
    int positive = 0;

    int sentinel = -1;

//    if(number == sentinel){
//        System.out.print("Enter a number (Enter -1 to exit)");
//    }

    while(number != sentinel){
        System.out.print("Enter any number (Enter -1 to exit)");
        number = input.nextInt();

        if(number < 0){
            negative += number;
        }
        else if(number > 0){
            positive += number;
        }
        else if(number == 0){
            zero += number;
        }

    }
    System.out.println("Total Positive numbers are: " + positive);
    System.out.println("Total Negative numbers are: " + negative);
    System.out.println("Total zero numbers are: " + zero);



}


}
