"use strict"; //включение "строгого" режима
let x = 0;
function test1() {
	console.log(x);
}

function test2() {
	let x = 0;
	function print(x) {
		console.log(x);
	}
	print(x);
}
x = 5;
test1();
test2();
