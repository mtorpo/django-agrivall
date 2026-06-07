const nav = document.querySelector(".nav");
const abrir = document.querySelector("#abrir");
const cerrar = document.querySelector("#cerrar");

abrir.addEventListener('click', () => {
    nav.classList.add("visible");
    document.body.classList.add('bloquear-scroll');
})

cerrar.addEventListener('click', () => {
    nav.classList.remove('visible');
    document.body.classList.remove('bloquear-scroll');

})