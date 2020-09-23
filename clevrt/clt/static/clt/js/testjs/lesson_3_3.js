"use strict"; //включение "строгого" режима
function Point(x, y) {
	this.x = x;
	this.y = y;
	this.print = function() {
		console.log(`Coord: x: ${this.x} y: ${this.y}`);
	}
	this.distance = function() {
		console.log(Math.sqrt(this.x ** 2 + this.y ** 2));
		return Math.sqrt(this.x ** 2 + this.y ** 2);
	}
	
}

let p = new Point(10, 20);
console.log(p.x + " | " + p.y);
p.x = 333;
p.print()
p.distance();