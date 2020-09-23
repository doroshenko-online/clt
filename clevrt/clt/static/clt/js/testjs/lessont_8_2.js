"use strict"; //включение "строгого" режима
//Отправка POST-запросов

function a(result) {
    console.log(result);
}

//async/await
async function getResult2(x) {
    let response = await fetch('http://localhost:8000/test2/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf8',
        },
        body: JSON.stringify({ 'x': x })
    });
    
    if (response.ok) {
        //let text = resp.json();
        let text = await response.text();
        console.log(text)
        //console.log(text.x);
    } else {
        console.log('Error: ' + response.status);
    }
}

window.addEventListener("DOMContentLoaded", function () {//выполняются функции только при загрузке документа
    //через Promis
    function getResult(x, func) {
        let response = fetch('http://localhost:8000/test2/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json;charset=utf8',
            },
            body: JSON.stringify({ 'x': x })
        });
        return response.then(resp => resp.text()).then(result => func(result));
    }

    getResult(5, a);
    getResult2(5)
})