import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get("https://www.chitai-gorod.ru/")
        self._driver.implicitly_wait(15)
        
    @allure.step("Принятие файлов куки")
    def set_cookie_policy(self): 
        cookie = {"name": "cookie_policy", "value": "1"}
        self._driver.add_cookie(cookie)

    @allure.step("Поиск книги на кириллице")
    def search_book_rus_ui(self, term):
        search_input = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "header-search__input"))
        )
        search_input.send_keys(term)
        self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
        txt = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p'))
        ).text
        return txt

    @allure.step("Поиск книги на латинице")
    def search_book_eng_ui(self, term):
        search_input = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "header-search__input"))
        )
        search_input.send_keys(term)
        self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
        txt = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p'))
        ).text
        return txt

    @allure.step("Поиск по символам")
    def search_invalid_ui(self, term):
        search_input = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "header-search__input"))
        )
        search_input.send_keys(term)
        self._driver.find_element(By.CLASS_NAME, "header-search__button").click()
        txt = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "catalog-empty-result__description"))
        ).text
        return txt

    @allure.step("Проверка пустой корзины")
    def get_empty_cart(self):
        cart_icon = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "header-cart__icon--desktop"))
        )
        cart_icon.click()
        txt = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "empty-title"))
        ).text
        return txt