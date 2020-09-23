"use strict"; //включение "строгого" режима
//Функции для работы с массивами

let [x, y] = [5, 7];

console.log(x);
console.log(y);

let array = [10 ,5 ,6, 78, 'sten'];

console.log(array.length);

//add to array

array.push(15); //add to end of array

console.log(array.length);
console.log(array);

array.unshift(75); //add before 1-st element in array
console.log(array.length);
console.log(array);

array.pop(); //delete last element of array
console.log(array.length);
console.log(array);

array.shift() //delete the 1-st element of array
console.log(array.length);
console.log(array);

console.log('-------------------------')

console.log(array.indexOf(6, 2)); //2-nd parametr for start index of search. If element not find method return -1. if element find then return index element of array

console.log(array.lastIndexOf(6)); //search from the end of array

let points = [
	{x: 5, y: 10},
	{x: 7, y: 15},
	{x: 5, y: 16},
];

function filter(item, index, array) {
	return item.x == 5;
}

console.log(points.find(filter));
console.log(points.findIndex(filter));

let pointsFilter = points.filter(filter);
console.log(pointsFilter);

console.log('-------------------------')

//sort
array.sort();
console.log(array);
array.sort(function(item1, item2) {
	//console.log(`${item1} - ${item2}`)
	return item1 - item2;
}
);

console.log(array);


console.log('-------------------------')

array = array.concat([2, 3], [4, 5]);
console.log(array);

//array.splice(3); //slice array
//array.splice(3, 1); //Удаляет элемент с по счету указанным во втором параметре после отсчета первого
array.splice(3, 2, 200, 300, 400); //Удаляет элемент с по счету указанным во втором параметре после отсчета первого и добавляет в массив на это место последующие указанные параметры
console.log(array);

let str = '15,10,40,25';

array = str.split(',');
console.log(array);

array = array.map(function(item, index, array){return Number(item);});
console.log(array);
