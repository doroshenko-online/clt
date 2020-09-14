"use strict"; //включение "строгого" режима
//var a; //не рекомендуется, используется в старых скриптах
let a; //объявление переменной a
a = 5;
console.log(a);
a = 'Hello';
console.log(a);
let name = 'Alex'; //создали переменную и присвоили значение
console.log(name);
let age = 18.7, single = true; //number and boolean set variable
let str_1 = "${name} холостой, вам ${age} лет"
let str_2 = `${name} холостой, вам ${age} лет` //конкатенация строк(нужны обратные апострофы)
console.log(str_1);
console.log(str_2);
console.log(name + ' холостой, вам ' + age + ' лет'); //конкатенация

let inf = 1 / 0; //Infinity тип - бесконечность
console.log(inf);

let nan = "abc" * 5; //NaN - тип данных
console.log(nan);

let und; //undefined
console.log(und);

let n = null; //null
console.log(n);

console.log(typeof(age)); //вывод типа данных переменной

//ДЗ
let age_1 = 20;
let name_1 = 'Дмитрий', single_1 = true;
console.log(typeof(age_1));
console.log(typeof(name_1));
console.log(typeof(single_1));
let str_11 = `Меня зовут ${name_1}, мне ${age_1} лет, моё семейное положение - ${single_1}`;
console.log(str_11);