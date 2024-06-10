var btnSignin = document.querySelector("#signin");
var btnSignup = document.querySelector("#signup");

var body = document.querySelector("body");

// Função para verificar a URL atual e definir a classe do corpo de acordo
function checkUrlAndSetBodyClass() {
    if (window.location.pathname === "/usuario/login/") {
        body.className = "sign-in-js";
    } else if (window.location.pathname === "/usuario/register/") {
        body.className = "sign-up-js";
    }
}

// Verificar a URL quando a página carrega
checkUrlAndSetBodyClass();

btnSignin.addEventListener("click", function () {
    body.className = "sign-in-js";
});

btnSignup.addEventListener("click", function () {
    body.className = "sign-up-js";
});
