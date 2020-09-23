"use strict"; //включение "строгого" режима
class Point {
	static counter = 0;
	constructor(x, y) {
		this.x = x;
		this.y = y;
		Point.counter++;
	}
	
	static getCounter() {
		console.log(Point.counter)
		return Point.counter
	}
	
	static getDistance(p1, p2) {
		console.log(Math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2));
		return Math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2);
	}
	
}

let p = new Point(5, 20);


console.log(Point.counter)

let p2 = new Point(10, 30);

console.log(Point.counter)

Point.getCounter()
Point.getDistance(p, p2)