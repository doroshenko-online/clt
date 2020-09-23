"use strict"; //включение "строгого" режима
let point = {};
point = {
	x: 10,
	y: 20
};
console.log(point);
console.log(point.x);
console.log(point.y);
point.x = 33;
console.log(point.x);

for (let field in point) {
	console.log(typeof(field));
	console.log(point[field]);
}

let point2 = {};
Object.assign(point2, point); //копирование одного объекта в другой
point.x = 333;
console.log(point2.x);
console.log(point.x);