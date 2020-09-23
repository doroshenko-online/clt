"use strict"; //включение "строгого" режима
//async/await

function success() {
    console.log('Success');
}

function error(msg) {
    console.log(msg);
}

async function test() {
    console.log('test function');
    //throw new Error('error msg');
    let p = await new Promise(function(resolve, reject) {
        setTimeout(() => resolve(), 2000);
    });
    console.log('end of function TEST()');

}

test().then(success, error);
console.log('Hello')