"use strict"; //включение "строгого" режима
/*
function sum(x, y, z) {
	return x + y + z;
}
console.log(sum(5, 10, 30));
*/

//same

let sum = (x, y, z) => (x + y + z); //стрелочная функция. В первых скобках параметры, а во вторых скобках результат, который возвращает функция
let hello = () => console.log("Hello");
console.log(sum(5, 10, 30));
console.log(sum);
hello();

let div = (x, y) => {
	if (y == 0) return false;
	return x/y;
}

console.log(div);
console.log(div(10, 5));
console.log(div(10, 0));