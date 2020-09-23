"use strict"; //включение "строгого" режима
class Point {
	z = 5;
	constructor(x, y) {
		this._x = x;
		this._y = y;
	}
	
	get distance() {
		return Math.sqrt(this._x ** 2 + this._y ** 2);
	}
	
	get x() {
		return this._x * 10;
	}
	
	get y() {
		return this._y * 10;
	}
	
	set x(coor) {
		if (coor < 0) this._x = 0;
		else this._x = coor;
	}
		
	set y(coor) {
		if (coor < 0) this._y = 0;
		else this._y = coor;
	}
}

let p = new Point(10, 15);
console.log(p.distance);
console.log(p.x);

p.x = -100;
console.log(p.x);