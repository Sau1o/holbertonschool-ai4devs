# Output Task 3: Human Review Simulation

## File: human_review_log.md

# Human Review Log

**Reviewer:** Senior Backend Engineer
**Date:** 2025-12-26
**Focus:** Business Logic, Architecture, and Best Practices.

---

## Reviewer Comments

### 1. ⚠️ Localization / Accent Insensitivity
- **File:** `src/services/task_service.py` (Line 18-20)
- **Comment:** A busca está usando apenas `.lower()`, o que funciona para o inglês, mas falha para usuários brasileiros. Se eu buscar "relatorio" e a tarefa for "Relatório", não vai encontrar.
- **Suggestion:** Sugiro usar `unidecode` ou normalização Unicode para remover acentos antes da comparação, garantindo uma busca mais fluida para o usuário final.

### 2. 🔧 Configuration Management
- **File:** `src/config.py`
- **Comment:** Boas práticas de *The Twelve-Factor App*. Embora tenhamos extraído as constantes, elas ainda estão "hardcoded" no arquivo Python.
- **Suggestion:** O ideal seria que `MAX_PAGE_LIMIT` e outros valores pudessem ser sobrescritos por variáveis de ambiente (`os.getenv`), facilitando ajustes em produção sem novo deploy.

### 3. 🏗️ Architecture / Dependency Injection
- **File:** `src/services/task_service.py`
- **Comment:** A classe `TaskService` importa `tasks_db` diretamente. Isso cria um acoplamento forte com a camada de dados (mesmo sendo um Mock).
- **Suggestion:** Para melhorar a testabilidade e seguir o princípio de Inversão de Dependência, deveríamos passar o repositório/db no construtor do serviço ou como argumento dos métodos, em vez de importá-lo globalmente.

### 4. 📄 API Contract / Metadata
- **File:** `src/api/routes.py`
- **Comment:** No objeto `meta` da resposta, estamos retornando `total_count`. É importante esclarecer se esse total é o **total global** de tarefas no banco ou o **total de itens encontrados após o filtro de busca**.
- **Suggestion:** Se for após o filtro, renomeie para `filtered_count` ou documente explicitamente no Swagger/OpenAPI para não confundir o frontend na hora de montar a paginação.

### 5. 🧪 Test Coverage Edge Case
- **File:** `tests/test_routes.py`
- **Comment:** Faltou um caso de teste para "Página Inexistente".
- **Suggestion:** O que acontece se eu pedir `offset=1000` quando só existem 20 itens? A API retorna array vazio corretamente (o que é bom), mas seria interessante ter um teste garantindo que o `meta` reflete isso (offset alto, data vazio) e não quebra a aplicação.
