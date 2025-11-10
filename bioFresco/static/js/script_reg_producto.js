// // para que aparezca un mensaje de que registramos el producto
// const formulario = document.querySelector('.Formulario'); 
// const mensaje = document.getElementById('mensaje');

// formulario.addEventListener('submit', function(event) {
//     event.preventDefault(); 

//     mensaje.textContent = '¡Producto registrado correctamente!';
//     mensaje.style.display = 'block';
//     mensaje.style.opacity = '1';

//     formulario.reset();

//     // Hacer que el mensaje desaparezca después de 3 segundos
//     setTimeout(() => {
//         mensaje.style.transition = 'opacity 0.5s';
//         mensaje.style.opacity = '0';
//         setTimeout(() => {
//             mensaje.style.display = 'none';
//         }, 500);
//     }, 5000);
// }); 

// Obtener CSRF token desde cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// Para mensaje y formulario
document.addEventListener("DOMContentLoaded", function () {
    const formulario = document.querySelector('.Formulario'); 
    const mensaje = document.getElementById('mensaje');

formulario.addEventListener('submit', async function(event) {
    event.preventDefault();

    const data = {
        id_producto: document.getElementById('codigo').value,
        nombre: document.getElementById('nombre').value,
        descripcion: document.getElementById('descripcion').value,
        vida_util: document.getElementById('vida').value
    };
    console.log("📨 Enviando datos:", data);
    try {
        const response = await fetch('/registro_producto/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        console.log("📩 Respuesta del servidor:", result);

        // Mostrar mensaje
        mensaje.textContent = result.message;
        mensaje.style.display = 'block';
        mensaje.style.opacity = '1';

        // Si fue exitoso, limpiar formulario
        if (result.success) {
            formulario.reset();
        }

        // Desaparecer después de 3 segundos
        setTimeout(() => {
            mensaje.style.transition = 'opacity 0.5s';
            mensaje.style.opacity = '0';
            setTimeout(() => {
                mensaje.style.display = 'none';
                mensaje.style.transition = ''; // limpiar transición
            }, 500);
        }, 3000);

    } catch (error) {
        console.error('Error:', error);

        mensaje.textContent = 'Error al conectar con el servidor';
        mensaje.style.display = 'block';
        mensaje.style.opacity = '1';

        setTimeout(() => {
            mensaje.style.transition = 'opacity 0.5s';
            mensaje.style.opacity = '0';
            setTimeout(() => {
                mensaje.style.display = 'none';
                mensaje.style.transition = '';
            }, 500);
        }, 3000);
    }
});
});
