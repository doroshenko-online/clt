"use strict"; //включение "строгого" режима
let a = prompt('Let number from 1 to 5');
a = +a;
console.log(a + " " + typeof(a));

switch (a) {
	case 1:
		alert("Your number is 1");
		break;
	case 2:
		alert("Your number is 2");
		break;
	case 3:
		alert("Your number is 3");
		break;
	case 4:
	case 5:
		alert("You write 4 or 5");
		break;
	default:
		alert("Wrong data");
}