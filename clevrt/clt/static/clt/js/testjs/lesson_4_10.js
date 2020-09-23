"use strict"; //включение "строгого" режима
//Objects Intl

let str = 'ё';
let str1 = 'я';

console.log(str > str1);

let arr = ["Ёлка", "Ягода", "Апельсин"];

console.log(arr.sort());

let colaltor = new Intl.Collator();
console.log(arr.sort(function(item1, item2){return colaltor.compare(item1, item2)}));

let dtfen = new Intl.DateTimeFormat('en-EN', {
	year: 'numeric',
	month: 'numeric',
	day: 'numeric',
	hour: 'numeric',
	minute: 'numeric',
});

console.log(dtfen.format(new Date()));

let nfru = new Intl.NumberFormat();
let nfen = new Intl.NumberFormat('en-US');

console.log(nfru.format(3858633678.343));
console.log(nfen.format(3858633678.343));