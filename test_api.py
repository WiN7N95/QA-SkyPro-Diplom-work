import requests
import allure
import pytest

BASE_URL = "https://web-gate.chitai-gorod.ru/api/v1"
BASE_URL_2 = "https://web-gate.chitai-gorod.ru/api/v2"
API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIwNjMzMjE5LCJpYXQiOjE3MTk2NTI5MjAsImV4cCI6MTcxOTY1NjUyMCwidHlwZSI6MjB9.lr6ZnJ87bUPlyl_nz4IJyQHBikwPK-5d2HUdmdZbM5c"
book_id = "harry-potter-and-the-philosophers-stone-in-reading-order-1-2444651"

@allure.feature("API")
@allure.story("Получение списка книг")
@pytest.mark.api_test
@pytest.mark.positive_test

def test_get_books():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {API_TOKEN}'
    }
    response = requests.get(f"{BASE_URL_2}/products", headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Получение информации о книге по ID")
@pytest.mark.api_test
@pytest.mark.positive_test

def test_get_book_by_id():
    book_id = "harry-potter-and-the-philosophers-stone-in-reading-order-1-2444651"    
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {API_TOKEN}'
    }

    response = requests.get(f"{BASE_URL}/products/slug/{book_id}", headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"
    assert "Роулинг" in response.text
    
@allure.feature("API")
@allure.story("Поиск книги на кириллице")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_search_books_rus():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {API_TOKEN}'
    }

    response = requests.get(f"{BASE_URL_2}/search/product?phrase=Гарри Поттер", headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Поиск книги на латинице")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_search_books_eng():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {API_TOKEN}'
    }

    response = requests.get(f"{BASE_URL_2}/search/product?phrase=Harry Potter", headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Поиск по символам")
@pytest.mark.api_test
@pytest.mark.negative_test
def test_search_unicode_symbols():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {API_TOKEN}'
    }

    response = requests.get(f"{BASE_URL_2}/search/product?phrase=! @ * £ $ % № #", headers=headers)
    assert response.status_code == 422, f"Ожидался статус-код 422, но получен {response.status_code}"


@allure.feature("API")
@allure.story("Пробел")
@pytest.mark.api_test
@pytest.mark.negative_test
def test_search_space():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {API_TOKEN}'
    }

    response = requests.get(f"{BASE_URL_2}/search/product?phrase=   ", headers=headers)
    assert response.status_code == 422, f"Ожидался статус-код 422, но получен {response.status_code}"


@allure.feature("API")
@allure.story("Получение списка книг по ID категории")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_get_category_books():
        headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {API_TOKEN}'
    }

        response = requests.get(f"{BASE_URL_2}/products?forceFilters[categories]=110227", headers=headers)
        assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Получение списка книг по фильтру")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_get_filtres_books():
        headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {API_TOKEN}'
    }

        response = requests.get(f"{BASE_URL_2}/products?filters[onlyNew]=1", headers=headers)
        assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"      


@allure.feature("API")
@allure.story("Получение списка книг по ID автора")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_get_books_by_author():      
        headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {API_TOKEN}'
    }

        response = requests.get(f"{BASE_URL_2}/products/facet?filters[authors]=593125", headers=headers)
        assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}" 

@allure.feature("API")
@allure.story("Добавление книги в корзину")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_add_book_to_cart():
    data = {
        "id": '2996532',
        "adData": {
            "item_list_name": "search",
            "product_shelf": ""
        }
    }
    
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {API_TOKEN}'
    }

    response = requests.post(f"{BASE_URL}/cart/product", json=data, headers=headers)
    assert response.status_code == 400, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Получение списка книг в корзине")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_get_cart():
    
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {API_TOKEN}'
    }

    response = requests.get(f"{BASE_URL}/cart", headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Удаление книги из корзины")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_del_book_from_cart():
    
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {API_TOKEN}'
    }

    response = requests.delete(f"{BASE_URL}/cart", headers=headers)
    assert response.status_code == 204, f"Ожидался статус-код 200, но получен {response.status_code}"