"use strict"; //включение "строгого" режима
//toString and valueOf

function Point(x, y) {
	this.x = x;
	this.y = y;
	this.toString = function() {return `Point with coordinates ${this.x} and ${this.y}`;} //вызывается если объект является строкой
	this.valueOf = function () {return Math.sqrt(this.x ** 2 + this.y ** 2)} //вызывается если объект является числом
}

let p = new Point(10, 20);
alert(p);
alert(Number(p));