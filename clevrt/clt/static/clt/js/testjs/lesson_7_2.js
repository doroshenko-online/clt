"use strict"; //включение "строгого" режима
//Асинхронность. промисы


// function loadjQuery(success, error) {
//     let jquery = document.createElement('script');
//     jquery.src = 'https://code.jquery.com/jquery-3.4.1.min.js';
//     document.head.append(jquery);
//     jquery.onload = success;
//     jquery.onerror = error;
// }

// loadjQuery(
//     function() {
//         console.log('Script uploaded')
//         $();
//     },
//     function() {
//         console.log('error at upload')
//     }
// );

function success() {
    console.log('Success task');
}

function error(e) {
    console.log('Error task ' + e);
}

let ps = new Promise(function (resolve, reject) {
    resolve('success');
})

let pe = new Promise(function (resolve, reject) {
    reject('reject');
})

console.log(ps);
console.log(pe);

ps.then(success, error);
pe.then(success, error);

ps.finally(() => console.log('finally ps'));
ps.finally(() => console.log('finally pe'));

function loadjQuery() {
    return new Promise(function (resolve, reject) {
        let jquery = document.createElement('script');
        jquery.src = 'https://code.jquery.com/jquery-3.4.1.min.js';
        document.head.append(jquery);
        jquery.onload = resolve;
        jquery.onerror = () => reject(new Error('Error upload')); //используется передача стрелочной функции, так как в обычную передать параметры мы не можем сразу
    })
}

let p = loadjQuery();
p.then(success, error);
p.then(loadjQuery).then(loadjQuery).then(success).catch(error);

