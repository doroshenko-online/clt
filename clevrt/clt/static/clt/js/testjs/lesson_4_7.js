"use strict"; //включение "строгого" режима
//объект Set(множество)

let s = new Set([20, 30, 40, 20]);

console.log(s);

s.add(15);
console.log(s);
console.log(s.size);
console.log(s.has(15));

s.delete(30);
console.log(s);

for (let v of s) {
	console.log(v);
}

s.clear()
console.log(s);