"use strict"; //включение "строгого" режима
let arr = []; // Same let arr = new Array();
arr = ['String', 10, true, false, 'Alex'];

function printArray(arr) {
	console.log(arr.length);
	for (let i = 0; i < arr.length; i++) {
		console.log(arr[i]);
	}
	
	for (let key in arr) {
		console.log(arr[key]);
	}
	
	for (let elem of arr) {
		console.log(elem);
	}
}	

function getAverageValue(arr) {
	let sum = 0;
	for (let elem of arr) {
		sum += +elem;
	}
	return sum/arr.length
}

printArray(arr);

let avg = getAverageValue([1, 2, 67, 33, '2', 4, 10, 22, '31']);
console.log(avg);