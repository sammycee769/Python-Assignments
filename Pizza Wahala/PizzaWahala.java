import java.util.Scanner;

public class PizzaWahala {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int sapaSlice = 4, sapaPrice = 2000;
        int smallMoneySlice = 6, smallMoneyPrice = 2400;
        int bigBoysSlice = 8, bigBoysPrice = 3000;
        int odogwuSlice = 12, odogwuPrice = 4200;

        System.out.println("""
--------Menu-------
Sapa size
Sapa_slice = 4
Sapa_price = 2000

Small Money size
Small_money_slice = 6
Small_money_price = 2400

Big Boys size
Big_boys_slice = 8
Big_boys_price = 3000

Odogwu size
Odogwu_slice = 12
Odogwu_price = 4200
""");
int numberOfPeople;

        while (true) {
            System.out.print("How Many Guests Do You Intend Serving: ");

            if (!input.hasNextInt()) {
                System.out.println("Invalid input! Please enter only numbers.");
                input.next(); 
            } else {
                numberOfPeople = input.nextInt(); 
                input.nextLine(); 
                break; 
            }
        }

        System.out.print("What Type Of Pizza Do You Intend Buying: ");
        String pizzaType = input.nextLine().toLowerCase();


        if (
            (!pizzaType.equals("sapa size") &&
             !pizzaType.equals("small money size") &&
             !pizzaType.equals("big boys size") &&
             !pizzaType.equals("odogwu size")) || numberOfPeople <= 0
        ) {
            System.out.println("Invalid Selection");
            return;
        }

        int pizzaBox = 0;
        int amountToPay = 0;
        int leftover = 0;

        if (pizzaType.equals("sapa size") && numberOfPeople % sapaSlice == 0) {
            pizzaBox = numberOfPeople / sapaSlice;
            amountToPay = sapaPrice * pizzaBox;
            leftover = 0;
        }
        else if (pizzaType.equals("sapa size") && numberOfPeople % sapaSlice != 0) {
            pizzaBox = (numberOfPeople / sapaSlice) + 1;
            amountToPay = sapaPrice * pizzaBox;
            leftover = (pizzaBox * sapaSlice) - numberOfPeople;
        }

        else if (pizzaType.equals("small money size") && numberOfPeople % smallMoneySlice == 0) {
            pizzaBox = numberOfPeople / smallMoneySlice;
            amountToPay = smallMoneyPrice * pizzaBox;
            leftover = 0;
        }
        else if (pizzaType.equals("small money size") && numberOfPeople % smallMoneySlice != 0) {
            pizzaBox = (numberOfPeople / smallMoneySlice) + 1;
            amountToPay = smallMoneyPrice * pizzaBox;
            leftover = (pizzaBox * smallMoneySlice) - numberOfPeople;
        }

        else if (pizzaType.equals("big boys size") && numberOfPeople % bigBoysSlice == 0) {
            pizzaBox = numberOfPeople / bigBoysSlice;
            amountToPay = bigBoysPrice * pizzaBox;
            leftover = 0;
        }
        else if (pizzaType.equals("big boys size") && numberOfPeople % bigBoysSlice != 0) {
            pizzaBox = (numberOfPeople / bigBoysSlice) + 1;
            amountToPay = bigBoysPrice * pizzaBox;
            leftover = (pizzaBox * bigBoysSlice) - numberOfPeople;
        }

        else if (pizzaType.equals("odogwu size") && numberOfPeople % odogwuSlice == 0) {
            pizzaBox = numberOfPeople / odogwuSlice;
            amountToPay = odogwuPrice * pizzaBox;
            leftover = 0;
        }
        else if (pizzaType.equals("odogwu size") && numberOfPeople % odogwuSlice != 0) {
            pizzaBox = (numberOfPeople / odogwuSlice) + 1;
            amountToPay = odogwuPrice * pizzaBox;
            leftover = (pizzaBox * odogwuSlice) - numberOfPeople;
        }

        System.out.println("Number of boxes of pizza to buy = " + pizzaBox + " boxes");
        System.out.println("Number of left over slice after serving = " + leftover + " slices");
        System.out.println("Amount = " + amountToPay);
    }
}

