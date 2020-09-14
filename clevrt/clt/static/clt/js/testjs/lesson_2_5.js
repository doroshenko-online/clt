"use strict"; //включение "строгого" режима
let str = "12.5";
console.log(typeof(str));
let number = Number(str); //преобразование строки в число
console.log(typeof(number) + " " + number);

console.log(Number('abc'));
console.log(Number(true));
console.log(Number('1') + Number('2'));
console.log(3 + 'number');
console.log(String(true));
console.log(Boolean(15) + " " + Boolean(0) + " " + Boolean(""));
console.log(true + true);

let a = '15';
let b = '17';
console.log(a + b);
console.log(+a + +b); //преобразование строки в число

//ДЗ

let x = "12.5";
let y = "-5.7";
console.log(x + y);
x = Number(x);
y = Number(y);
/* второй вариант записи преобразования строк в числа
x = +x;
y = +y;
*/
console.log(x + y);