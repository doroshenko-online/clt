"use strict"; //включение "строгого" режима
function div(x, y) {
	let result;
	try {
		if (y == 0) {
			throw new Error("Division by zero") //выброс исключения типа Error
		}
		result = x/y;
		return result;
	}
	catch(e) {
		console.log("Error: " + e + " | " + e.name);
	}
	finally {
		console.log("Выполняется finally в любом случае")
	}
}

let d = div(10, 5);
console.log(d);
console.log(div(10, 0));

window.onerror = function(msg, url, line) {		//обработчик вывода ошибок
	alert(`Error: ${msg} on ${line} line in file ${url}`);
}

x = 10;
