function mostrarProductoAñadido(message) {

    const toastElement = document.getElementById("cartToast");
    const toastBody = document.getElementById("cartToastBody");

    toastBody.innerHTML = `✓ ${message}`;

    const toast = bootstrap.Toast.getOrCreateInstance(
        toastElement,
        {
            autohide: true,
            delay: 1500
        }
    );

    toast.show();
}