"use strict"; //включение "строгого" режима
//регулярные выражения

function isHaveLink(str) {
	let reg = /https?:\/\/.+?\.[a-z]{2,}\s/im; // i в конце игнорирует регистр, m - поиск по всем строкам. ? после + ограничиват "жадность"
	console.log(str.match(reg));
	return str.match(reg);
}

function checkEmail(str) {
	let reg = /^[a-z0-9_][a-z0-9._-]*[a-z0-9_]*@([a-z0-9]+[a-z0-9_-]*[a-z0-9]+\.)+[a-z0-9]+$/i;
	console.log(str.match(reg));
	return str.match(reg);
}

let str1 = "Some string on siteL http://aaaaa.ru - check it!";
let str2 = "Thank's for information";

if (isHaveLink(str1)) console.log("Find link in string 1");
if (isHaveLink(str2)) console.log("Find link in string 2");

let email1 = "myemail123@gmail.com.ua";
let email2 = "myemail123@";

if (checkEmail(email1)) console.log("Find email in string 1");
if (checkEmail(email2)) console.log("Find email in string 2");


let money = "I have 100 dollars and 57 cent";

let reg = /\d+/g; //g - global search

let matches = money.match(reg);

for (let item of matches) {
	console.log(item);
}

money = money.replace(reg, "N");
console.log(money);