"use strict"; //включение "строгого" режима
class Point {
	z = 5;
	
	//Конструктор
	constructor(x, y) {
		this.x = x;
		this.y = y;
	}
	
	getDistance() {
		return Math.sqrt(this.x ** 2 + this.y ** 2);
	}
	
}

let p = new Point(10, 20);
console.log(p);
console.log(p.getDistance());