"use strict"; //включение "строгого" режима
let a = true;
let b = false;
console.log(a); //true
console.log(!a); //false
console.log(a && b); //логическое И
console.log(a || b); //логическое ИЛИ
console.log(a ^ b); //исключающее ИЛИ

//ДЗ
/*
1) Самостоятельно вычислите результат следующего выражения: (5 < 6 || (true && (5 >= 5 && (false || true) && (true && true))))
2) Выведите результат выражения в консоль и убедитесь, что в первом пункте Вы вычислили всё правильно.
*/

//1
/*
true
*/

//2
console.log((5 < 6 || (true && (5 >= 5 && (false || true) && (true && true)))));