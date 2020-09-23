"use strict"; //включение "строгого" режима
//практика

let count = 10;
let names = ['Alex', 'John', 'Mathew', 'Derek', 'Stuart', 'Michael', 'Gary', 'Rohn', 'Tony'];

let users = [];
for (let i = 0; i < count; i++) {
    let user = {
        name: names[Math.floor(Math.random() * names.length)],
        age: Math.floor(Math.random() * 100) + 1,
        single: Math.random() > 0.5
    };
    users.push(user);
}

console.log(users);

for (let user of users) {
    let template = document.getElementById('user-template').cloneNode(true);
    template.removeAttribute('id');
    template.querySelector('.name').innerHTML = user.name;
    template.querySelector('.age').innerHTML = user.age;
    template.querySelector('.single').innerHTML = (user.single)? 'Yes' : 'No';
    document.body.append(template);
}