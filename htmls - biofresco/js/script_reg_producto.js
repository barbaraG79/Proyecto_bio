// para que aparezca un mensaje de que registramos el producto
const formulario = document.querySelector('.Formulario'); 
const mensaje = document.getElementById('mensaje');

formulario.addEventListener('submit', function(event) {
    event.preventDefault(); 

    mensaje.textContent = '¡Producto registrado correctamente!';
    mensaje.style.display = 'block';
    mensaje.style.opacity = '1';

    formulario.reset();

    // Hacer que el mensaje desaparezca después de 3 segundos
    setTimeout(() => {
        mensaje.style.transition = 'opacity 0.5s';
        mensaje.style.opacity = '0';
        setTimeout(() => {
            mensaje.style.display = 'none';
        }, 500);
    }, 5000);
}); 
