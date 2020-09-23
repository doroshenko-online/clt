"use strict"; //включение "строгого" режима
// код стороннего разработчика начало
let point = {
	x: 10,
	y: 20
}

point.z = 30;
// код стороннего разработчика КОНЕЦ
let z = Symbol();
point[z] = 40;
console.log("Our value z: " + point[z]);
console.log("Someone else's value: " + point.z);