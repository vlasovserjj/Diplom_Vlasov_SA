import requests
from parametres import params, movie_id, invalid_movie_id
from environment import BASE_URL, headers
import allure
import pytest



@pytest.mark.positive_test
@allure.title("Проверка получения информации о фильме по ID")
@allure.description("Проверяет, что по введенному ID фильма находится искомый фильм")
@allure.feature("READ")
@allure.severity("critical")
def test_get_movie_by_id():  
    response = requests.get(f"{BASE_URL}/search?page=1&limit=15&query={movie_id}", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["docs"]["id"] == movie_id



@pytest.mark.positive_test
@allure.title("Проверка поиска фильма по названию")
@allure.description("Проверяет, что строка поиска работает и находит искомый фильм")
@allure.feature("READ")
@allure.severity("critical")
def test_search_movie_by_name():
    response = requests.get(f"{BASE_URL}/search?page=1&limit=15&query=", headers=headers, params=params)
    assert response.status_code == 200
    data = response.json()
    assert any("Шерлок Холмс" in item["name"] for item in data["docs"])



@pytest.mark.positive_test
@allure.title("Проверка пагинации при получении списка фильмов")
@allure.description("Проверяет, что на одной странице результатов поиска 10 резулоьтатов")
@allure.feature("READ")
@allure.severity("critical")
def test_pagination_movies():
    response = requests.get(f"{BASE_URL}/search?page=1&limit=15&query=", headers=headers, params=params)
    assert response.status_code == 200
    data = response.json()
    assert data["page"] == 2
    assert len(data["docs"]) <= 10



@pytest.mark.negative_test
@allure.title("Проверка обработки некорректного ID")
@allure.description("Проверяет что поиск фильма по некорректному ID выдаёт ошибку")
@allure.feature("READ")
@allure.severity("critical")
def test_get_movie_invalid_id():
    response = requests.get(f"{BASE_URL}/{invalid_movie_id}", headers=headers)
    assert response.status_code == 401



@pytest.mark.negative_test
@allure.title("Проверка авторизации без токена")
@allure.description("Проверяет что без токена авторизации будет выдаваться сообщение об отсутствии авторизации")
@allure.feature("READ")
@allure.severity("critical")
def test_unauthorized_access():
    response = requests.get(f"{BASE_URL}/{movie_id}") 
    assert response.status_code == 401 or response.status_code == 403