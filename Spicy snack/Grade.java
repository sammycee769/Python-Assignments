import java.util.Scanner;
public class Grade{
public static void main(String [] args){
Scanner input = new Scanner(System.in);
System.out.println("Enter first grade");
firstGrade = input.nextInt();
System.out.println("Enter second grade");
secondGrade = input.nextInt();
System.out.println("Enter third grade");
thirdGrade = input.nextInt();
averageGrade = (firstGrade + secondGrade + thirdGrade) / 3 ;
if(90 <= averageGrade and averageGrade <= 100){
    println("Your grade is A");
}else if(80 <= averageGrade and averageGrade < 90){
    println("Your grade is B");
}else if(70 <= averageGrade and averageGrade < 80){
    println("Your grade is C");
}else if(60 <= averageGrade and averageGrade < 70){
    println("Your grade is D");
}else{
print("Your grade is F");
}
}
}

