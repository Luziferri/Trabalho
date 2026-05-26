document.addEventListener('DOMContentLoaded', function() {
    console.log('main.js loaded - DOM ready');
    
    const container = document.getElementById('toast-container');
    const resourceStateUrl = '/api/resource-state';
    let nextTickAtMs = null;
    let isSyncingResourceState = false;
    let serverTimeOffsetMs = 0; 

    // Inicialização da data
    const initialTickNode = document.querySelector('[data-tick-countdown]');
    if (initialTickNode && initialTickNode.dataset.nextTickAt) {
        nextTickAtMs = Date.parse(initialTickNode.dataset.nextTickAt);
    }

    // --- FUNÇÕES DE UPDATE DE UI ---
    window.showToast = function(message, type) {
        if (!container) return;
        const toast = document.createElement('div');
        toast.className = 'toast ' + (type || 'success');
        toast.textContent = message;
        container.appendChild(toast);
        setTimeout(() => toast.classList.add('show'), 10);
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 400);
        }, 3000);
    };

    function updateResourceHud(resources) {
        document.querySelectorAll('[data-resource-key]').forEach(card => {
            const key = card.dataset.resourceKey;
            if (resources[key] !== undefined) {
                const valueNode = card.querySelector('p');
                if (valueNode) valueNode.textContent = resources[key];
            }
        });
    }

    function updateGenerationHud(generation) {
        document.querySelectorAll('[data-generation-key]').forEach(node => {
            const key = node.dataset.generationKey;
            if (generation[key] !== undefined) node.textContent = generation[key];
        });
    }

    function updateBuildingMap(buildings) {
        document.querySelectorAll('[data-building-count]').forEach(node => {
            const key = node.dataset.buildingCount;
            if (buildings[key] !== undefined) {
                node.textContent = buildings[key];
                const card = node.closest('.map-building');
                if (card) card.style.display = buildings[key] > 0 ? 'flex' : 'none';
            }
        });
    }

    // --- LÓGICA DO RELÓGIO ---
    function renderTickCountdown() {
        if (nextTickAtMs === null) return;

        const agora = Date.now() + serverTimeOffsetMs;
        let segundosRestantes = Math.max(0, Math.ceil((nextTickAtMs - agora) / 1000));
        
        document.querySelectorAll('[data-tick-countdown]').forEach(node => {
            node.textContent = segundosRestantes;
        });

        if (segundosRestantes === 0 && !isSyncingResourceState) {
            syncResourceState();
        }
    }

    function applyGameState(data) {
        if (!data) return;

        // Ajusta o offset apenas se o servidor enviar a hora (essencial para evitar saltos)
        if (data.server_time) {
            serverTimeOffsetMs = Date.parse(data.server_time) - Date.now();
        }

        if (data.resources) updateResourceHud(data.resources);
        if (data.generation) updateGenerationHud(data.generation);
        if (data.buildings) updateBuildingMap(data.buildings);
        
        if (data.next_tick_at) {
            nextTickAtMs = Date.parse(data.next_tick_at);
        }
        // Nota: Removido renderTickCountdown() daqui para evitar duplicação
    }

    async function syncResourceState() {
        if (isSyncingResourceState) return;
        isSyncingResourceState = true;
        try {
            const response = await fetch(resourceStateUrl, {
                method: 'POST',
                headers: { 'Accept': 'application/json' }
            });
            const data = await response.json();
            if (data && data.success) {
                applyGameState(data);
            }
        } catch (error) {
            console.error('Erro de sincronização:', error);
        } finally {
            isSyncingResourceState = false;
        }
    }

    // Exposto para handlers fora do escopo do DOMContentLoaded (ex.: submit AJAX global)
    window.syncResourceState = syncResourceState;

    // --- DISPARADORES ---
    syncResourceState(); // Carregamento inicial
    setInterval(renderTickCountdown, 1000); // Relógio (1s)
    setInterval(syncResourceState, 5000);   // Sync (5s)
});



// ajax

document.addEventListener('submit', function(event) {
    if (event.target.classList.contains('ajax-form')) {
        event.preventDefault(); 
        const form = event.target;
        
        fetch(form.action, {
            method: 'POST',
            headers: { 'Accept': 'application/json' }
        })
        .then(() => {
            // Sincroniza imediatamente após a construção
            syncResourceState(); 
        })
        .catch(err => console.error(err));
    }
});