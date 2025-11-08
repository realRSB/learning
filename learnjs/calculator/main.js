let num1 = document.getElementById("num1-el")
let num2 = document.getElementById("num2-el")
let finalEl = document.getElementById("final")
let saveEl = document.getElementById("save-el")

function add () {
    let result = Number(num1.value) + Number(num2.value)
    finalEl.textContent = result
    save(result)
}

function subtract () {
    let result = Number(num1.value) - Number(num2.value)
    finalEl.textContent = result
    save(result)
}

function multiply () {
    let result = Number(num1.value) * Number(num2.value)
    finalEl.textContent = result
    save(result)
}

function divide () {
    let result = Number(num1.value) / Number(num2.value)
    finalEl.textContent = result
    save(result)
}

function save(result) {
    let finalStr = result + " - "
    saveEl.textContent += finalStr
}

