document.addEventListener('DOMContentLoaded', function() {
    const container = document.getElementById('toast-container');

    // Função simples de criar notificação (Matéria de aula: DOM Manipulation)
    window.showToast = function(message, type) {
        if (!container) return;

        // Criar elemento (Lab 05)
        const toast = document.createElement('div');
        toast.className = 'toast ' + (type || 'success');
        toast.textContent = message;
        
        container.appendChild(toast);

        // Animação simples com CSS classes (Lab 06)
        setTimeout(() => {
            toast.classList.add('show');
        }, 10);

        // Remover após 3 segundos (Matéria de aula: Timers)
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => {
                toast.remove(); // Remove do HTML
            }, 400);
        }, 3000);
    };

    // Processar mensagens enviadas pelo Flask (Server-side rendering)
    const serverFlashes = document.querySelectorAll('.flash-message');
    serverFlashes.forEach(msg => {
        const type = msg.dataset.category;
        const text = msg.textContent;
        window.showToast(text, type);
        msg.style.display = 'none'; // Esconde a mensagem estática
    });

    function updateResourceCard(resourceName, newValue) {
        document.querySelectorAll('.stat-card').forEach(card => {
            const title = card.querySelector('h3');
            const value = card.querySelector('p');
            if (!title || !value) return;

            const cardName = title.textContent.trim().toLowerCase();
            if (cardName === resourceName) {
                value.textContent = newValue;
            }
        });
    }

    // Evita recarregar a página quando o jogador apanha madeira ou telhas
    document.querySelectorAll('.action-zone form').forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault();

            const xhr = new XMLHttpRequest();
            xhr.open('POST', this.action, true);
            xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');

            xhr.onload = function() {
                let data = null;

                try {
                    data = JSON.parse(xhr.responseText);
                } catch (error) {
                    window.showToast('Erro ao atualizar o recurso.', 'danger');
                    return;
                }

                if (xhr.status >= 200 && xhr.status < 300 && data && data.success) {
                    window.showToast('+' + data.amount + ' ' + data.recurso, 'success');
                    updateResourceCard(data.recurso, data.new_value);
                    return;
                }

                window.showToast((data && data.message) ? data.message : 'Erro ao colher recurso.', 'danger');
            };

            xhr.onerror = function() {
                window.showToast('Erro de rede.', 'danger');
            };

            xhr.send();
        });
    });
});
