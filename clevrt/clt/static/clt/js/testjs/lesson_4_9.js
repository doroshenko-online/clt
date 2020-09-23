"use strict"; //включение "строгого" режима
//setTimeout and setInterval

function toLog(msg) {
	console.log(msg);
}

let c = 0;

function forInterval() {
	c++;
	console.log('Start interval: ' + c)
}

setTimeout(toLog, 1000, Math.round(Math.random() * 10)); //start after 1 second
setTimeout(() => toLog(Math.round(Math.random() * 10)), 2000);

let tid = setTimeout(() => toLog(Math.round(Math.random() * 10)), 2000);

//clearTimeout(tid);

let iid = setInterval(forInterval, 500);

//clearInterval(iid);