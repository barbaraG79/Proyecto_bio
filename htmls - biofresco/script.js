document.getElementById('notifBtn').addEventListener('click', function() {
            togglePanel('notifPanel');
        });

document.getElementById('settingsBtn').addEventListener('click', function() {
            togglePanel('settingsPanel');
        });

        // Funciones de apertura/cierre
        function togglePanel(id) {
            const panel = document.getElementById(id);
            const otherPanel = id === 'notifPanel' ? document.getElementById('settingsPanel') : document.getElementById('notifPanel');
            otherPanel.classList.remove('active');
            panel.classList.toggle('active');
        }

        function closePanel(id) {
            document.getElementById(id).classList.remove('active');
        }