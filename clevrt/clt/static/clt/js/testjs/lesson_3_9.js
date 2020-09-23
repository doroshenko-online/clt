"use strict"; //включение "строгого" режима
class Shape {
	constructor(x, y) {
		this.x = x;
		this.y = y;
	}
	
	getDistance() {
		return Math.sqrt(this.x ** 2 + this.y ** 2);
	}
	
	draw() {console.log("parent");};
}

class Point extends Shape {
	draw() {
		console.log("paint point");
	}
}

class Circle extends Shape {
	constructor(x, y, r) {
		super(x, y);			//вызов родительского конструктoра
		this.r = r;
	}
	
	draw() {
		super.draw();
		console.log("paint circle");
	}
}

let s = new Shape(5, 7);
let p = new Point(15, 20);
let c = new Circle(10, 15, 30);

console.log(s);
console.log(p);
console.log(c);

console.log(s.getDistance());
console.log(p.getDistance());
console.log(c.getDistance());

s.draw()
p.draw()
c.draw()