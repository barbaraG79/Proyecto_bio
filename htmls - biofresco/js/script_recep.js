const formulario = document.querySelector('.Formulario'); 
const mensaje = document.getElementById('mensaje');

formulario.addEventListener('submit', function(event) {
    event.preventDefault(); 

    mensaje.textContent = '¡Recepción registrada correctamente!';
    mensaje.style.display = 'block';
    mensaje.style.opacity = '1';
    

    // Hace que el mensaje desaparezca después de 5 segundos
    setTimeout(() => {
        mensaje.style.transition = 'opacity 0.5s';
        mensaje.style.opacity = '0';
        setTimeout(() => {
            mensaje.style.display = 'none';
        }, 500);
    }, 5000);

    setTimeout(() => {
        window.location.href = 'recepcion_producto.html'; //ruta
    }, 5000);
}); 