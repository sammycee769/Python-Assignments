const prompt = require("prompt-sync")();

const sapaSlice = 4;
const sapaPrice = 2000;

const smallMoneySlice = 6;
const smallMoneyPrice = 2400;

const bigBoysSlice = 8;
const bigBoysPrice = 3000;

const odogwuSlice = 12;
const odogwuPrice = 4200;

console.log(`
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
`);


let numberOfPeople = parseInt(prompt("How Many Guests Do You Intend Serving: "));
let pizzaType = prompt("What Type Of Pizza Do You Intend Buying: ").toLowerCase();

if (
  !["sapa size", "small money size", "big boys size", "odogwu size"].includes(pizzaType) ||
  numberOfPeople <= 0
) {
  console.log("Invalid Selection");
  process.exit(0);
}

let pizzaBox = 0;
let amountToPay = 0;
let leftover = 0;

if (pizzaType === "sapa size" && numberOfPeople % sapaSlice === 0) {
  pizzaBox = numberOfPeople / sapaSlice;
  amountToPay = sapaPrice * pizzaBox;
  leftover = 0;
}
else if (pizzaType === "sapa size" && numberOfPeople % sapaSlice !== 0) {
  pizzaBox = Math.floor(numberOfPeople / sapaSlice) + 1;
  amountToPay = sapaPrice * pizzaBox;
  leftover = (pizzaBox * sapaSlice) - numberOfPeople;
}


else if (pizzaType === "small money size" && numberOfPeople % smallMoneySlice === 0) {
  pizzaBox = numberOfPeople / smallMoneySlice;
  amountToPay = smallMoneyPrice * pizzaBox;
  leftover = 0;
}
else if (pizzaType === "small money size" && numberOfPeople % smallMoneySlice !== 0) {
  pizzaBox = Math.floor(numberOfPeople / smallMoneySlice) + 1;
  amountToPay = smallMoneyPrice * pizzaBox;
  leftover = (pizzaBox * smallMoneySlice) - numberOfPeople;
}


else if (pizzaType === "big boys size" && numberOfPeople % bigBoysSlice === 0) {
  pizzaBox = numberOfPeople / bigBoysSlice;
  amountToPay = bigBoysPrice * pizzaBox;
  leftover = 0;
}
else if (pizzaType === "big boys size" && numberOfPeople % bigBoysSlice !== 0) {
  pizzaBox = Math.floor(numberOfPeople / bigBoysSlice) + 1;
  amountToPay = bigBoysPrice * pizzaBox;
  leftover = (pizzaBox * bigBoysSlice) - numberOfPeople;
}


else if (pizzaType === "odogwu size" && numberOfPeople % odogwuSlice === 0) {
  pizzaBox = numberOfPeople / odogwuSlice;
  amountToPay = odogwuPrice * pizzaBox;
  leftover = 0;
}
else if (pizzaType === "odogwu size" && numberOfPeople % odogwuSlice !== 0) {
  pizzaBox = Math.floor(numberOfPeople / odogwuSlice) + 1;
  amountToPay = odogwuPrice * pizzaBox;
  leftover = (pizzaBox * odogwuSlice) - numberOfPeople;
}

console.log("Number of boxes of pizza to buy =", pizzaBox, "boxes");
console.log("Number of left over slice after serving =", leftover, "slices");
console.log("Amount =", amountToPay);





