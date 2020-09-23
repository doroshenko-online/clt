"use strict"; //включение "строгого" режима
for (let i = 0; i < 5; i++) {
	if (i == 2) continue;
	if (i == 3) break;
	console.log(i);
}

let i = 0;
while(i < 5) {
	console.log(i)
	i++;
}

i = 0;
do {
	console.log(i);
	i++
} while (i < 5);

let summa = 0;
let n = 10;
i = 1;
while(i <= n) {
	summa += i;
	i++;
}
console.log(summa);
//same
summa = 0;
i = 1;
for (; i <= 10; i++) {
	summa += i;
}

console.log(summa);