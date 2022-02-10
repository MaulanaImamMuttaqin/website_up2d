let loading = document.querySelector("#loading")
let userInput = document.querySelector("#username")
let pass = document.querySelector("#pass")

console.log("woy")

function getCookie(name) {
    let cookie = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
    return cookie ? cookie[2] : null;
}

console.log(getCookie("csrftoken"))

const sendData = () => {
    loading.classList.remove("hidden")
    fetch("/auth/login/", {
        method: "POST",
        credentials: "same-origin",
        headers: new Headers({
            "X-CSRFToken": getCookie("csrftoken"),
            "Content-Type": "application/json"
        }),
        body: JSON.stringify({
            username: userInput.value,
            pass: pass.value
        })
    }).then(res => {
        loading.classList.add("hidden")
        res.json().then(data => {

            console.log(data)
        })
    })
}