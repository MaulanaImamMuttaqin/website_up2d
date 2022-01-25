let loading = document.querySelector("#loading")
let userInput = document.querySelector("#username")
let pass = document.querySelector("#pass")

const sendData = () => {
    loading.classList.remove("hidden")
    fetch("/api/login/", {
        method: "POST",
        credentials: "same-origin",
        headers: new Headers({
            'content-type': 'application/json',
            "X-CSRFToken": getCookie("csrftoken"),
            "Accept": "application/json",
            "Content-Type": "application/json"
        }),
        body: JSON.stringify({
            username: userInput.value,
            pass: pass.value
        })
    }).then(res => {
        loading.classList.add("hidden")
        res.json().then(data => {

            console.log(data.response)
        })
    })
}