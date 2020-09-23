"use strict"; //включение "строгого" режима
//JSON

class Point {
	constructor(x, y) {
		this.x = x;
		this.y = y;
	}
}

class Circle {
	constructor(p, r) {
		this.p = p;
		this.r = r;
		this.colors = ['green', 'red', 'blue']
	}
}

let p = new Point(10, 25);
let c = new Circle(p, 10);
console.log(p);
console.log(c.p.x);

let json = JSON.stringify(c);

console.log(json);

let obj = JSON.parse(json);

console.log(obj);
console.log(obj.p.x);
console.log(obj.colors);