"use strict"; //включение "строгого" режима
class Point {
	constructor(x, y) {
		this.x = x;
		this.y = y;
	}
}

let p = new Point(10, 20);
let descriptor = Object.getOwnPropertyDescriptor(p, 'x');
console.log(descriptor);
p.x = 15;
//delete p.x; - удаление объекта, доступен только если configurable: true

Object.defineProperty(p, 'x', {writable: true, enumerable: false, configurable: false})

for (let field in p) console.log(p[field]);

p.x = 25;
descriptor = Object.getOwnPropertyDescriptor(p, 'x');
console.log(descriptor);