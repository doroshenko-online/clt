"use strict"; //включение "строгого" режима
//строковые функции

let str = 'Слово в кавычках \'work\''
console.log(str);

console.log(str.codePointAt(0)); //выдает код юникода символа

console.log(str.indexOf('c')); //индекс первого вхождения строки. Вторым параметром принимает индекс символа с которого начинать поиск. Если значение не найдено, то возвращает -1.


console.log(str.slice(10)); //удаляет левую часть строки начиная от указаного индекса символа. Вторым параметром принимает индекс окончания обрезки
console.log(str);
console.log(str.substr(5, 10)); //почти тоже самое что и slice


console.log(str.toLowerCase());
console.log(str.toUpperCase());


console.log(str.trim()); //удаляет проблеы и табуляции на концах строки