import java.util.Scanner;
public class AgeCalculator{
public static void main(String [] args){
Scanner input = new Scanner(System.in);
System.out.println("Enter father's age");
int fathersAge = input.nextInt();
System.out.println("Enter son's age");
int sonsAge = input.nextInt();
int yearsAgo = ( 2 * sonsAge) - fathersAge;
if(fathersAge > 0  && fathersAge < 81 || sonsAge > 0 && sonsAge < 81){
System.out.printf("%d",yearsAgo);
}else{
System.out.print("Enter an age between 1 and 80");
}
}
}
