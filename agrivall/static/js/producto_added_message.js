function mostrarProductoAñadido(message) {
    // Esta función quita el d-none del div del mensaje, espera X segundos y lo vuelve a esconder
    if (!message || message.trim() === "") return;

    const toast = document.getElementById("cartToast");
    const toastBody = document.getElementById("cartToastBody");

    toastBody.textContent = `✓ ${message}`;
    toast.classList.remove("d-none");

    setTimeout(() => {
        toast.classList.add("d-none");
        toastBody.textContent = "";
    }, 1500);
}