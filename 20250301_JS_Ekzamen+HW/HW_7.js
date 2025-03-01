window.addEventListener('load', alertwar);

function alertwar() {
    let n = prompt('введите число');
    for (let i = 0; i < n; i++) {
        let h1 = document.createElement('h1');
        h1.textContent = 'Это тоже цикл и гадский промпт на входе!';
        document.body.appendChild(h1);
    }
}
