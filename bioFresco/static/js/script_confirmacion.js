document.addEventListener("DOMContentLoaded", function() {
    const pedidoForm = document.getElementById("pedidoForm");
    const mensaje = document.getElementById("mensaje");
    const mensajeTexto = document.getElementById("mensajeTexto");
    const cancelarBtn = document.getElementById("cancelarBtn");
    const motivoBox = document.getElementById("motivoCancelacion");
    const enviarMotivo = document.getElementById("enviarMotivo");

    // Confirmar entrega
    pedidoForm.addEventListener("submit", function(e){
        e.preventDefault();
        mensajeTexto.textContent = "✅ Pedido confirmado exitosamente.";
        mensaje.style.display = "flex";
        setTimeout(() => {
            window.location.href = "menu.html"; // cambiar por tu URL Django si quieres
        }, 2000);
    });

    // Mostrar cuadro de motivo
    cancelarBtn.addEventListener("click", function(){
        motivoBox.style.display = "block";
    });

    // Enviar motivo
    enviarMotivo.addEventListener("click", function(){
        const motivo = document.getElementById("motivo").value.trim();
        if(motivo === ""){
            alert("Por favor, indique el motivo de la cancelación.");
            return;
        }
        mensajeTexto.textContent = "❌ Entrega cancelada.\nMotivo: " + motivo;
        mensaje.style.display = "flex";
        motivoBox.style.display = "none";
        pedidoForm.reset();
    });

    // Cerrar mensaje
    window.cerrarMensaje = function(){
        mensaje.style.display = "none";
    };
});
