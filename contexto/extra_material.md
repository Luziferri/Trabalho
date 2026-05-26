Material adicional — funcionalidades do projeto não presentes nos MDs

Este ficheiro documenta as partes do projeto implementadas nesta sessão que não constam dos ficheiros de apoio (`contexto/*.md`). O objetivo é explicá-las de forma pedagógica para integrar no plano das aulas.

1. Visão geral
- Acrescentei um sistema de "Slots de Construção" persistentes por utilizador com tarefas assíncronas (sem worker), controladas por timestamps.
- Objetivo pedagógico: ligar conceitos de frontend (DOM, fetch, timers) com backend (modelos, persistência, endpoints JSON) — material não coberto nos MDs.

2. Modelo `ConstructionSlot` (SQLAlchemy)
- Local: `models.py`
- Estrutura (campos relevantes):
  - `id` (Integer, PK)
  - `user_id` (FK para `user.id`)
  - `slot_number` (Integer) — índice do slot para o utilizador
  - `building_type` (String) — tipo de edifício (
  - `is_active` (Boolean)
  - `created_at` (DateTime)
  - Campos de tarefa:
    - `task_type` (String) — e.g. `construction`, `minerar`, `comerciar`, `defender`
    - `task_started_at` (DateTime)
    - `task_duration` (Integer) — segundos
    - `task_collected` (Boolean)

3. Lógica de slots e tarefas (server-side)
- `ensure_user_construction_slots(user)`: garante que cada utilizador tem `TOTAL_CONSTRUCTION_SLOTS` linhas na tabela (preenchimento automático).
- `slot_task_status(slot)`: função utilitária que calcula `processing`, `completed` ou `collected` com base em `task_started_at` e `task_duration`.
- Finalização "on-demand": não há worker/cron; quando o dashboard é acedido ou o utilizador tenta recolher, o servidor verifica timestamps e aplica recompensas (incrementa recursos do `user`) e limpa campos de task.

4. Mapeamento de Tarefas (`TASKS`) — em `app.py`
- Exemplo:
  TASKS = {
    'minerar': {'duration': 300, 'reward': {'madeira': 50}},
    'comerciar': {'duration': 600, 'reward': {'joias': 10, 'comida': 5}},
    'defender': {'duration': 1200, 'reward': {'soldados': 2}},
  }
- Duração em segundos, recompensa em pares recurso→quantidade.

5. Endpoints (API)
- `POST /slot/<slot_id>/start_order`
  - Requisitos: sessão ativa, slot pertence ao user, slot activo (tem um edifício)
  - Verifica se não há tarefa em processamento
  - Inicia a tarefa: define `task_type`, `task_started_at`, `task_duration`, `task_collected=False`
  - Resposta JSON: `{'success': True, 'message': 'Tarefa iniciada.', 'task': <task>, 'duration': <seconds>}`

- `POST /slot/<slot_id>/collect`
  - Requisitos: sessão e slot válidos
  - Verifica `slot_task_status(slot)` == `completed`
  - Aplica recompensa (incrementa campos do `user`), marca `task_collected=True` e limpa os campos de tarefa
  - Resposta JSON: `{'success': True, 'message': 'Recompensa recolhida.', 'reward': {}}`

- `POST /construir_edificio?tipo=<tipo>`
  - Usa `ensure_user_construction_slots` para encontrar slot livre
  - Deduz custos e inicia uma `task_type='construction'` com duração aleatória entre 1 e 10 minutos
  - Redirect para `/dashboard` (com `flask.flash` notificações)

- `POST /colher?recurso=<recurso>`
  - Endpoint ajax-friendly que incrementa imediatamente um recurso e responde em JSON quando solicitado com `Accept: application/json`.

6. Frontend (principais pontos)
- `templates/dashboard.html`
  - Mostra cada slot com `slot.task_status`, `slot.task_type` e `slot.task_remaining` (segundos).
  - Gera formulários para `start_order` e `collect` com `action` apropriada.
  - Usa atributos `data-remaining="<segundos>"` no elemento `.slot-remaining` para o contador em tempo real.

- `static/js/main.js`
  - Ajuda pedagógica: contém comentários que ligam o código às aulas (Lab04/05/08).
  - Usa `document.addEventListener('DOMContentLoaded', ...)` e `fetch()` para as chamadas AJAX.
  - Contador em tempo real: um `setInterval` actualiza cada span `.slot-remaining` a cada segundo, formata mm:ss, e quando chega a 0 revela o botão de recolher e agenda um `location.reload()` curto para sincronizar com o servidor.

7. Como isto mapeia aos MDs (sugestões de integração)
- Lab04 (JavaScript): adicionar uma secção "Exemplo prático: Contador ligado a timestamp do servidor".
  - Mostrar o snippet de `setInterval` e a lógica de `data-remaining`.

- Lab05 (DOM e formulários): explicar como construir formulários que não recarregam a página (AJAX) e atualizar o DOM (`updateResourceCard`).
  - Inserir um pequeno excerpt do `main.js` mostrando `fetch()` para `colher_recurso`.

- Lab08 (Flask): adicionar um anexo que descreve o endpoint `/slot/<id>/start_order` e as verificações de sessão/autoridade, e o padrão de resposta JSON.

8. Exemplos de uso (cURL + fetch)
- cURL iniciar tarefa:
  curl -X POST -b "cookie-file" "http://localhost:5000/slot/123/start_order" -d "task=minerar" -H "Accept: application/json"

- fetch (exemplo minimal):
  fetch('/slot/123/start_order', {method: 'POST', credentials: 'same-origin', body: new URLSearchParams({task:'minerar'}), headers:{'Accept':'application/json'}})
    .then(r=>r.json()).then(j=>console.log(j))

9. Testes sugeridos para o laboratório
- Cria um user de testes e inicia várias tarefas em slots diferentes.
- Verifica no dashboard que os contadores descem em tempo real e que o botão de recolher aparece quando chegam a zero.
- Testa o fluxo com a Network tab do browser para inspecionar as respostas JSON dos endpoints.

10. Observações finais
- Esta abordagem (finalização "on-demand") é adequada para projetos educativos com SQLite e sem worker. Para produção, usar um scheduler (APScheduler) ou Celery para garantir finalizações pontuais sem dependência do acesso do utilizador.

---
