# Estrutura de Arquivos Gerada (Baseada na Lista 1)

## 1. tests/test_products.py
```python
import pytest
from fastapi.testclient import TestClient

# Nota: Assumindo que o arquivo principal da aplicação se chamaria 'main.py' e a instância 'app'
# Como a Lista 2 (Implementação) ainda não foi fornecida, este é um modelo padrão.
# from main import app 
# client = TestClient(app)

# Mock do client para fins de demonstração da estrutura de testes
class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

class MockClient:
    def get(self, url):
        if url == "/products":
            return MockResponse([{"id": 1, "name": "Test Product"}], 200)
        return MockResponse({"error": "Not Found"}, 404)

    def post(self, url, json):
        return MockResponse({"id": 2, "name": json["name"]}, 201)

    def put(self, url, json):
        return MockResponse({"id": 1, "name": json["name"]}, 200)

    def delete(self, url):
        return MockResponse({"message": "Deleted"}, 204)

@pytest.fixture
def client():
    return MockClient()

# Teste 1: Listar Produtos (GET)
def test_get_products(client):
    res = client.get("/products")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

# Teste 2: Criar Produto (POST)
def test_create_product(client):
    payload = {"name": "New Product", "price": 10.5}
    res = client.post("/products", json=payload)
    assert res.status_code == 201
    assert res.json()["name"] == "New Product"

# Teste 3: Atualizar Produto (PUT)
def test_update_product(client):
    payload = {"name": "Updated Product", "price": 20.0}
    # Assumindo ID 1 existente
    res = client.put("/products/1", json=payload)
    assert res.status_code == 200
    assert res.json()["name"] == "Updated Product"

# Teste 4: Deletar Produto (DELETE)
def test_delete_product(client):
    res = client.delete("/products/1")
    assert res.status_code == 204

# Teste 5: Produto Não Encontrado (Integração/Fluxo de Erro)
def test_get_product_not_found(client):
    res = client.get("/products/999")
    assert res.status_code == 404
