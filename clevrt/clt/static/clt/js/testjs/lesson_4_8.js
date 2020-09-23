"use strict"; //включение "строгого" режима
//Функции работы с датой и временем

let date = new Date();
console.log(date);

console.log(date.getTime()); //unix format
console.log((date.getTime() / 1000) / 60 / 60 / 24 / 365); //unix format
console.log(date.getFullYear());
console.log(date.getMonth()); //start with 0 to 11
console.log(date.getDate());
console.log(date.getHours());
console.log(date.getMinutes());
console.log(date.getSeconds());
console.log(date.getMilliseconds());
console.log(date.getDay());

console.log(date.getUTCDate()); 

console.log('-------------------------');

date.setFullYear(2021);
date.setMonth(11);
console.log(date.getFullYear());
console.log(date.getMonth()); //start with 0 to 11
console.log(date);

console.log('-------------------------');

date = new Date(86400000);
console.log(date);

date = new Date(2020, 1, 27, 12, 40, 50, 100);
console.log(date);
console.log(date.getMilliseconds());
console.log(date.getTime());

date.setDate(date.getDate() + 5);
console.log(date);

console.log('-------------------------');

//YYYY-MM-DDTHH:mm:ss.sss+-hh:mm

let ms = Date.parse('2022-12-21T23:59:59.999+03:00')
console.log(new Date(ms));

