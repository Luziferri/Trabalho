document.addEventListener('DOMContentLoaded', function () {
    const rankingBody = document.getElementById('ranking-body');

    async function fetchRanking() {
        try {
            const response = await fetch('/api/ranking');
            const data = await response.json();
            
            // Limpa a tabela
            rankingBody.innerHTML = '';

            // Preenche a tabela com os novos dados
            data.forEach((player, index) => {
                let badge = '';
                
                // Atribuição de Badges para o Top 3
                if (index === 0) badge = '🥇 ';
                else if (index === 1) badge = '🥈 ';
                else if (index === 2) badge = '🥉 ';

                const tr = document.createElement('tr');
                
                // Highlight visual se quiseres dar destaque à linha do Top 3
                if (index < 3) {
                    tr.style.fontWeight = 'bold';
                }

                tr.innerHTML = `
                    <td>${index + 1}º</td>
                    <td>${badge}${player.username}</td>
                    <td>${player.score}</td>
                `;
                rankingBody.appendChild(tr);
            });
        } catch (error) {
            console.error("Erro ao atualizar o ranking:", error);
        }
    }

    // Chama a função imediatamente ao carregar a página
    fetchRanking();

    // Atualiza em tempo real a cada 5 segundos (5000 milissegundos)
    setInterval(fetchRanking, 5000);
});