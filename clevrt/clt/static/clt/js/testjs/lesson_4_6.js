"use strict"; //включение "строгого" режима
//объект map

let m = new Map();

m.set('key', 'value');
m.set('age', 25);
m.set('single', false);

console.log(m);
console.log(m.size); //length of object
console.log(m.get('key'));
console.log(m.has('key'));

m.set('single', true);
console.log(m);

for (let i of m.keys()) {
	console.log(i);
}

for (let i of m.values()) {
	console.log(i);
}

console.log('-----------------------------');

for (let entry of m.entries()) {
	console.log(`Key ${entry[0]} | value ${entry[1]}`);
}

//same

for (let entry of m) {
	console.log(`Key ${entry[0]} | value ${entry[1]}`);
}


m.clear(); //delete all elements in object Map