"use strict"; //включение "строгого" режима
//

console.log(document.body)
console.log(document.head)

console.log('-------------------------');

for (let node of document.body.childNodes) {
    //console.log(node);
    if (node.nodeName == 'UL') console.log(node.childNodes[3].parentNode);
}

console.log('-------------------------');

let elem = document.body.childNodes[9]

for (let k in elem){
    console.log(elem.innerHTML);
}

elem.innerHTML = "<li>pidor1</li>\n<li>pidor2</li>\n<li>pidor3</li>"
