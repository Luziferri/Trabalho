document.addEventListener('DOMContentLoaded', function() {
    console.log('main.js loaded - DOM ready');
    const container = document.getElementById('toast-container');
    const resourceStateUrl = '/api/resource-state';
    let nextTickSeconds = null;

    window.showToast = function(message, type) {
        if (!container) return;

        const toast = document.createElement('div');
        toast.className = 'toast ' + (type || 'success');
        toast.textContent = message;

        container.appendChild(toast);

        setTimeout(() => {
            toast.classList.add('show');
        }, 10);

        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => {
                toast.remove();
            }, 400);
        }, 3000);
    };

    const serverFlashes = document.querySelectorAll('.flash-message');
    serverFlashes.forEach(msg => {
        const type = msg.dataset.category;
        const text = msg.textContent;
        window.showToast(text, type);
        msg.style.display = 'none';
    });

    function updateResourceHud(resources) {
        document.querySelectorAll('[data-resource-key]').forEach(card => {
            const key = card.dataset.resourceKey;
            if (resources[key] === undefined) return;
            const valueNode = card.querySelector('p');
            if (valueNode) {
                valueNode.textContent = resources[key];
            }
        });
    }

    function updateGenerationHud(generation) {
        document.querySelectorAll('[data-generation-key]').forEach(node => {
            const key = node.dataset.generationKey;
            if (generation[key] === undefined) return;
            node.textContent = generation[key];
        });
    }

    function updateBuildingMap(buildings) {
        document.querySelectorAll('[data-building-count]').forEach(node => {
            const key = node.dataset.buildingCount;
            if (buildings[key] === undefined) return;

            node.textContent = buildings[key];

            const card = node.closest('.map-building');
            if (card) {
                card.style.display = buildings[key] > 0 ? 'flex' : 'none';
            }
        });
    }

    function updateTickCountdown(seconds) {
        if (Number.isFinite(seconds)) {
            nextTickSeconds = seconds;
        }

        document.querySelectorAll('[data-tick-countdown]').forEach(node => {
            if (nextTickSeconds === null) return;
            node.textContent = nextTickSeconds;
        });
    }

    function applyGameState(state) {
        if (!state) return;
        if (state.resources) {
            updateResourceHud(state.resources);
        }
        if (state.generation) {
            updateGenerationHud(state.generation);
        }
        if (state.buildings) {
            updateBuildingMap(state.buildings);
        }
        if (typeof state.next_tick_in === 'number') {
            updateTickCountdown(state.next_tick_in);
        }
    }

    async function syncResourceState() {
        try {
            const response = await fetch(resourceStateUrl, {
                method: 'POST',
                credentials: 'same-origin',
                headers: {
                    'Accept': 'application/json'
                }
            });

            if (!response.ok) {
                const message = await response.text();
                throw new Error(message || response.statusText);
            }

            const data = await response.json();
            if (data && data.success) {
                applyGameState(data);
                return;
            }

            window.showToast((data && data.message) ? data.message : 'Erro ao sincronizar recursos.', 'danger');
        } catch (error) {
            window.showToast(error.message || 'Erro de rede.', 'danger');
        }
    }

    syncResourceState();
    setInterval(syncResourceState, 5000);

    setInterval(() => {
        if (nextTickSeconds === null) return;
        if (nextTickSeconds > 0) {
            nextTickSeconds -= 1;
            updateTickCountdown();
        }
    }, 1000);
});
