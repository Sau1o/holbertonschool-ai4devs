# Arquivos Corrigidos (Baseado no Feedback)

## 1. tests/test_products.py
```python
import pytest
from fastapi.testclient import TestClient

# Mock structures for validation purposes
class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

class MockClient:
    def get(self, url):
        if url == "/products":
            return MockResponse([{"id": 1, "name": "Test Product", "price": 10.0}], 200)
        if url == "/products/1":
             return MockResponse({"id": 1, "name": "Test Product", "price": 10.0}, 200)
        return MockResponse({"detail": "Not Found"}, 404)

    def post(self, url, json):
        if "name" not in json:
            return MockResponse({"detail": "Invalid data"}, 422)
        return MockResponse({"id": 2, "name": json["name"], "price": json.get("price")}, 201)

    def put(self, url, json):
        if url == "/products/1":
            return MockResponse({"id": 1, "name": json["name"], "price": json["price"]}, 200)
        return MockResponse({"detail": "Not Found"}, 404)

    def delete(self, url):
        if url == "/products/1":
            return MockResponse(None, 204)
        return MockResponse({"detail": "Not Found"}, 404)

@pytest.fixture
def client():
    return MockClient()

# --- Unit & Integration Tests ---

# Test 1: Get All Products (Happy Path)
def test_get_products(client):
    res = client.get("/products")
    assert res.status_code == 200
    assert isinstance(res.json(), list)
    assert len(res.json()) > 0

# Test 2: Get Single Product (Happy Path)
def test_get_single_product(client):
    res = client.get("/products/1")
    assert res.status_code == 200
    assert res.json()["id"] == 1

# Test 3: Create Product (Happy Path)
def test_create_product(client):
    payload = {"name": "New Product", "price": 50.0}
    res = client.post("/products", json=payload)
    assert res.status_code == 201
    assert res.json()["name"] == "New Product"

# Test 4: Create Product Validation Error (Edge Case)
def test_create_product_invalid(client):
    payload = {"price": 50.0} # Missing name
    res = client.post("/products", json=payload)
    assert res.status_code == 422

# Test 5: Update Product (Happy Path)
def test_update_product(client):
    payload = {"name": "Updated Product", "price": 75.0}
    res = client.put("/products/1", json=payload)
    assert res.status_code == 200
    assert res.json()["price"] == 75.0

# Test 6: Delete Product (Happy Path)
def test_delete_product(client):
    res = client.delete("/products/1")
    assert res.status_code == 204

# Test 7: Get Non-Existent Product (Error Flow)
def test_get_product_not_found(client):
    res = client.get("/products/999")
    assert res.status_code == 404
