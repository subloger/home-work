'use strict';

let fitlerPopup = document.querySelector('.filterPopup');
let fitlerLabel = document.querySelector('.filterLabel');
let filterIcon = document.querySelector('.filterIcon');

fitlerLabel.addEventListener('click', function () {
    fitlerPopup.classList.toggle('hidden');
    fitlerLabel.classList.toggle('filterLabelPink');
    filterIcon.classList.toggle('filterIconPink');

    if (filterIcon.getAttribute('src') === 'images/filter.svg') {
        filterIcon.setAttribute('src', 'images/filterHover.svg')
    } else {
        filterIcon.setAttribute('src', 'images/filter.svg')
    }
});

let filterHeaders = document.querySelectorAll('.filterCategoryHeader');
filterHeaders.forEach(function (header) {
    header.addEventListener('click', function (event) {
        event.target.nextElementSibling.classList.toggle('hidden');
    })
});

let filterSizes = document.querySelector('.filterSizes');
let filterSizeWrap = document.querySelector('.filterSizeWrap');
filterSizeWrap.addEventListener('click', function () {
    filterSizes.classList.toggle('hidden');
});


// Домашнее задание *****************************************************


let addButton = [];
let listEl = document.querySelectorAll('.featuredItem button');
listEl.forEach(el => { addButton.push(el) });

let tableProducts = document.querySelector('tableListTop');
let tr = document.querySelector('tbody');
let sum = document.querySelector('.right');
let countEl = document.querySelector('.cartIcon').nextElementSibling;

// Список продуктов

const listProducts = {
    0: { id: 1, name: "ELLERY X M'O CAPSULE 1", price: 23, count: 0 },
    1: { id: 2, name: "ELLERY X M'O CAPSULE 2", price: 40, count: 0 },
    2: { id: 3, name: "ELLERY X M'O CAPSULE 3", price: 52, count: 0 },
    3: { id: 4, name: "ELLERY X M'O CAPSULE 4", price: 28, count: 0 },
    4: { id: 5, name: "ELLERY X M'O CAPSULE 5", price: 68, count: 0 },
    5: { id: 6, name: "ELLERY X M'O CAPSULE 6", price: 33, count: 0 },
};

let sumElem = 0;
let sumCount = 0;

// Функция обновления строк в корзине

function addHtml(id) {
    if (addButton[id] && listProducts[id].count == 0) {
        let startElem = document.querySelector(`tr:nth-child(${id + 2})`);
        startElem.innerHTML += `<td class="height">${listProducts[id].name}</td>
                             <td>${listProducts[id].count += 1}</td>
                             <td>${listProducts[id].price}</td>
                             <td>${listProducts[id].count * listProducts[id].price}.00 $</td>`;

    } else {
        let elem = document.querySelector(`tr:nth-child(${id + 2})`);
        elem.innerHTML = `<td>${listProducts[id].name}</td>
                              <td>${listProducts[id].count += 1}</td>
                              <td>${listProducts[id].price}</td>
                              <td>${listProducts[id].count * listProducts[id].price}.00 $</td>`;

    }

    for (let i = 0; i < addButton.length; i++) {
        sumElem += listProducts[i].price * listProducts[i].count;
        sumCount += listProducts[i].count;
    };

    sum.innerHTML = `Товаров в корзине на сумму:  $${sumElem}`;
    countEl.textContent = `${sumCount}`;
    sumElem = 0;
    sumCount = 0;
}

let isCreated = false;   // Переменная для контроля создания ячеек таблицы

// Вызов функции по нажатию на кнопку добавить

for (let i = 0; i < addButton.length; i++) {
    addButton[i].addEventListener('click', event => {
        if (isCreated === false) {
            for (let i = 0; i < addButton.length; i++) {
                let trElem = document.createElement('tr');
                tr.append(trElem);
            }
            isCreated = true;
        }
        addHtml(i)
    });
}

// Показать/скрыть корзину

let divList = document.querySelector('.hidden');
let buttElem = document.querySelector('.cartIcon');
buttElem.addEventListener('click', event => {
    divList.classList.toggle('hidden');
});
