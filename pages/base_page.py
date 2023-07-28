from config import URL
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """
    Этот класс представляет базовую страницу для всех остальных страниц.
    Он содержит общие методы, используемые на разных страницах.
    """

    def __init__(self, driver):
        """
        Конструктор класса BasePage.

        :param driver: объект Selenium WebDriver
        """
        self.driver = driver
        self.base_url = URL

    def go_to_site(self):
        """
        Переходит на базовый URL веб-сайта.

        :return: None
        """
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        """
        Находит элемент на странице с использованием заданного локатора.

        :param locator: кортеж с стратегией и значением локатора
        :param time: максимальное время ожидания появления элемента (по умолчанию 10 секунд)
        :return: объект WebElement
        """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator), message=f"Не удалось найти элемент по локатору {locator}"
        )

    def find_elements(self, locator, time=10):
        """
        Находит все элементы на странице с использованием заданного локатора.

        :param locator: кортеж с стратегией и значением локатора
        :param time: максимальное время ожидания появления элементов (по умолчанию 10 секунд)
        :return: список объектов WebElement
        """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator), message=f"Не удалось найти элементы по локатору {locator}"
        )

    def click_element(self, locator):
        """
        Нажимает на элемент, найденный по заданному локатору.

        :param locator: кортеж с стратегией и значением локатора
        :return: None
        """
        self.find_element(locator).click()

    def input_data(self, locator, text):
        """
        Вводит заданный текст в поле ввода, найденное по заданному локатору.

        :param locator: кортеж с стратегией и значением локатора
        :param text: текст для ввода в поле ввода
        :return: None
        """
        self.find_element(locator).send_keys(text)

    def status_code(self):
        return requests.get(self.base_url).status_code

    def switch_tab(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    def input_data_dict(self, data_dict):
        for locator, value in data_dict.items():
            self.input_data(locator, value)
