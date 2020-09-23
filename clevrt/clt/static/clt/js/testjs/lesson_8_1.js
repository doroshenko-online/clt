"use strict"; //включение "строгого" режима
//запросы через fetch

async function getData(url, json = false, headers = false) {
    await new Promise(function (resolve, reject) { //ожидаем асинхронный промис и выполняем дальше
        setTimeout(() => resolve(), 2000);
    })
    let response = await fetch(url);
    let text;
    if (json) {
        text = await response.json(); //получить json из ответа
    } else {
        text = await response.text(); //получить текст из ответа        
    }
    if (response.ok) {
        console.log(response);
        console.log('Code: ' + response.status);
        console.log('Take data: ' + text);
        if (json) console.log('JSON: ' + text['name'] + ' ' + text.age + ' лет')
    }
    else {
        console.log('Error: ' + response.status);
    }

    if (headers) {
        for (let [key, value] of response.headers) {
            console.log(key + ': ' + value);
        }
    }
}

getData('http://localhost:8000/test2', true, true)