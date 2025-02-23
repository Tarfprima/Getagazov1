// функция для вывода данных в консоль 
function printData(){
    // решил сделать используя getElementByID
    let firstName = document.getElementById('firstName').value
    let secondName = document.getElementById('lastName').value
    let userAge = document.getElementById('age').value
// вывод в консоль
    console.log("Я - " + firstName + ' ' + secondName)
    console.log('Мой возраст - ' + userAge)
}
