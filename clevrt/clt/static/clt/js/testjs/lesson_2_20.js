"use strict"; //включение "строгого" режима

let arr = [];
while(true) {
	let code = prompt('let number code of oparation')
	if (code == '1') {
		arr[arr.length] = prompt("let element");
	}	
	else if (code == '2') {
		alert(arr);
	}else if (code == '3') break;
	else alert("Unknown code");
}