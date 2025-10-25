from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from parametres import url, search_locator, movie_name, loc_elements, logot, login_loc
import unittest
import pytest
import allure


class KinoPoiskUITests(unittest.TestCase):
    def setUp(self):
        with allure.step("Запуск браузера"):
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            self.driver.maximize_window()
            self.driver.implicitly_wait(6)
            self.driver.get(url)
    
    def tearDown(self):
        with allure.step("Выход из браузера"):
            self.driver.quit()


    @pytest.mark.positive_test
    @allure.title("Проверка наличия поля 'поиск'")
    @allure.description("Проверяет, что на главной странице отображается поле 'поиск'")
    @allure.feature("READ")
    @allure.severity("critical")
    def test_search_field_presence(self):
        """Проверить, что поле поиска отображается на главной странице"""
        search_field = self.driver.find_element(By.CSS_SELECTOR, search_locator)
        self.assertTrue(search_field.is_displayed(), "Поле поиска не отображается")


    @pytest.mark.positive_test
    @allure.title("Проверка функции поиск фильмов")
    @allure.description("Проверяет, что на главной странице работает поле 'поиск'")
    @allure.feature("READ")
    @allure.severity("critical")
    def test_search_functionality(self):
        """Проверить, что поиск работает и результаты появляются"""
        search_field = self.driver.find_element(By.CSS_SELECTOR, search_locator)
        search_field.send_keys(movie_name + Keys.RETURN)
        results = self.driver.find_elements(By.CSS_SELECTOR, loc_elements)
        self.assertGreater(len(results), 0, "Результаты поиска не найдены")


    @pytest.mark.positive_test
    @allure.title("Проверка отображение логотипа 'Кинопоиск'")
    @allure.description("Проверяет, что на главной странице есть логотип 'Кинопоиск'")
    @allure.feature("READ")
    @allure.severity("critical")
    def test_main_logo_presence(self):
        """Проверить, что логотип Кинопоиска отображается"""
        logo = self.driver.find_element(By.CSS_SELECTOR, logot)
        self.assertTrue(logo.is_displayed(), "Логотип не отображается")
    

    @pytest.mark.positive_test
    @allure.title("Проверка перехода в раздел 'Фильмы'")
    @allure.description("Проверяет, что с главной страницы есть возможность перейти в раздел 'Фильмы'")
    @allure.feature("READ")
    @allure.severity("critical")    
    def test_navigation_to_movies_section(self):
        """Проверить переход в раздел 'Фильмы' с главной"""
        movies_link = self.driver.find_element(By.LINK_TEXT, "Фильмы")
        movies_link.click()
        self.assertIn("movies", self.driver.current_url, "Не произошёл переход в раздел 'Фильмы'")
    

    @pytest.mark.positive_test
    @allure.title("Проверка кнопки 'Войти'")
    @allure.description("Проверяет, что на главной странице присутствует и работает кнопка 'Войти'")
    @allure.feature("READ")
    @allure.severity("critical")     
    def test_user_login_button(self):
        """Проверить, что кнопка входа пользователя видна и кликабельна"""
        login_button = self.driver.find_element(By.CSS_SELECTOR, login_loc)
        self.assertTrue(login_button.is_displayed() and login_button.is_enabled(), "Кнопка входа недоступна")

if __name__ == "__main__":
    unittest.main()