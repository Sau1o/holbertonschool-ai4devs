# Output Task 0: Implementation Artifacts

## File: pr_description.md

# Pull Request: Feature/Task Pagination and Search

## Summary
Implementação de paginação e busca textual no endpoint de listagem de tarefas (`GET /tasks`). Esta funcionalidade visa melhorar a performance do retorno de dados e a usabilidade para encontrar tarefas específicas.

## Changes
- **`src/api/routes.py`**:
    - Atualização do endpoint `list_tasks` para aceitar query parameters `limit`, `offset` e `q`.
    - Implementação de lógica de *slicing* para paginação.
    - Implementação de filtro de string (case-insensitive) para busca em `title` e `description`.
- **`src/core/utils.py`**:
    - Adição de função helper `paginate_data` para reutilização futura.
- **`tests/test_routes.py`**:
    - Adição de 5 novos testes cobrindo cenários de paginação, busca com sucesso, busca vazia e parâmetros inválidos.

## Context
~130 LOC (Lines of Code) adicionadas/modificadas.
**Related Issue:** #42 (Listagem lenta com muitos registros).
**Motivation:** O frontend estava travando ao tentar renderizar a lista completa de tarefas sem controle de quantidade.

---

## File: src/api/routes.py

```python
from flask import Blueprint, request, jsonify
from src.db.mock_db import tasks_db
from src.core.utils import paginate_data

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['GET'])
def list_tasks():
    """
    Retorna lista de tarefas com suporte a busca e paginação.
    Params:
        - q (str): Termo de busca (opcional)
        - limit (int): Máximo de itens por página (default: 10)
        - offset (int): Itens a pular (default: 0)
    """
    try:
        search_query = request.args.get('q', '').lower()
        limit = int(request.args.get('limit', 10))
        offset = int(request.args.get('offset', 0))
    except ValueError:
        return jsonify({"error": "Parâmetros de paginação inválidos"}), 400

    # 1. Filtragem (Search)
    filtered_tasks = tasks_db
    if search_query:
        filtered_tasks = [
            task for task in tasks_db
            if search_query in task['title'].lower() or
               search_query in task['description'].lower()
        ]

    # 2. Paginação
    paginated_result = paginate_data(filtered_tasks, limit, offset)

    return jsonify({
        "data": paginated_result,
        "meta": {
            "total_count": len(filtered_tasks),
            "limit": limit,
            "offset": offset,
            "page_size": len(paginated_result)
        }
    }), 200
