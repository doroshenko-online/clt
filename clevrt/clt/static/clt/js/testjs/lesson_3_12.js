"use strict"; //включение "строгого" режима
//Примеси

let log = {
	toLog(str) {
		console.log(str);
	}
}

class Point {
	constructor(x, y) {
		this.x = x;
		this.y = y;
		this.toLog("Created a new object");
	}
}

class User {
	constructor() {
		this.toLog("Created a new User");
	}
}

//Добавление примеси в классы
Object.assign(Point.prototype, log);
Object.assign(User.prototype, log);

let p = new Point(10, 20);
let u = new User();

p.toLog("Some information");