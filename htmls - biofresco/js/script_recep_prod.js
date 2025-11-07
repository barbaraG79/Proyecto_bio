const formulario = document.querySelector('.Formulario'); 
const mensaje = document.getElementById('mensaje');
const boton = document.getElementById('boton-terminar');
const mensaje2 = document.getElementById('mensaje2');

formulario.addEventListener('submit', function(event) {
    event.preventDefault(); 

    mensaje.textContent = '¡Producto agregado correctamente!';
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

boton.addEventListener('submit', function(event) {
    event.preventDefault();
    mensaje2.textContent = 'Recepción Finalizada con exito.';
    mensaje2.style.display = 'block';
    mensaje2.style.opacity = '1';

    setTimeout(() => {
        window.location.href = 'home.html'; // cambia esta ruta
    }, 5000);
}); 