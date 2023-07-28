from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Locators(BasePage):
    # Локаторы

    # Кнопка переключения языка страницы
    LOCATOR_LANG = (By.XPATH, '//div[@class="lang_switcher__name "]')

    # Идентификатор английского языка
    LOCATOR_LANG_ENG = (By.XPATH, '//div[contains(text(),\'Eng\')]')

    # Идентификатор английского текста на странице
    LOCATOR_LANG_ENG_TEXT = (By.XPATH, '//div[contains(text(),\'Educational Fund “Talent and success”\')]')

    # Идентификатор русского языка
    LOCATOR_LANG_RU = (By.XPATH, '//div[contains(text(),\'Рус\')]')

    # Идентификатор русского текста на странице
    LOCATOR_LANG_RU_TEXT = (By.XPATH, '//div[contains(text(),\'Образовательный Фонд «Талант и успех»\')]')

    # Идентификатор текст ссылка "Правила проведения"
    LOCATOR_BEHAVIOR_RULES = (By.XPATH, '//a[@href="https://edu.sirius.online"]')

    # Идентификатор страницы "Правила проведения"
    LOCATOR_BEHAVIOR_RULES_TITLE = (By.XPATH, '//meta[@property=\'og:title\' and @content=\'Сириус.Курсы\']')

    # Локатор ссылки на "Соглашение проверки персональных данных"
    LOCATOR_PERSONAL_DATA = (By.XPATH,
                             '//a[@href="https://sochisirius.ru/uploads/2021/05/210405%20Политика%20безопасности'
                             '%20в%20области%20обработки%20персональных%20данных.pdf"]')

    # Локатор сссылки на пользовательнсоке соглашение
    LOCATOR_TERMS_OF_USE = (By.XPATH, '//a[@href="https://sochisirius.ru/uploads/files/documents/agreement.pdf"]')

    # Локатор строки/бокса "Основная олимпиада"
    LOCATOR_MAIN_OLYMPIAD = (By.XPATH, '//span[contains(text(),\'Основная олимпиада\')]')

    # Локатор строки/бокса "Дополнительная олимпиада"
    LOCATOR_ADDITIONAL_OLYMPIAD = (By.XPATH, '//span[contains(text(),\'Дополнительная олимпиада\')]')

    # Локатор общий для радиокнопки, положение неактивен (выделен белым)
    LOCATOR_OLYMPIAD_FALSE = (By.CSS_SELECTOR, '[class*="ui-schema-auth-form__enum-input-radio"')

    # Локатор общий для радиокнопки, положение активен (выделен синим)
    LOCATOR_OLYMPIAD_TRUE = (
        By.CSS_SELECTOR,
        'span.ui-schema-auth-form__enum-input-radio ui-schema-auth-form__enum-input-radio-checked-true')

    # Локатор общий для всех чекбоксов на главной странице регистрации
    LOCATOR_CHECKBOX_RULES = (By.CSS_SELECTOR, 'input.ui-checkbox__input.has-outline')

    # Локатор чекбокса в положение активен, галочка стоит
    LOCATOR_CHECKBOX_TRUE = (By.XPATH, '//label[@class="ui-checkbox  ui-schema-auth-form__checkbox  "]')

    # Локатор сообшения с текстом ошибки под полем
    LOCATOR_WRROR_MESSAGE = (By.CSS_SELECTOR, '[class*="ui-schema-auth-form__error"]')

    # Локатор поля "Имя"
    LOCATOR_NAME = (By.CSS_SELECTOR, 'div.test-locator-sf-firstName input.ui-textinput__input')

    # Локатор поля "Фамилия"
    LOCATOR_LAST_NAME = (By.CSS_SELECTOR, 'div.test-locator-sf-lastName input.ui-textinput__input')

    # Локатор поля "Отчество"
    LOCATOR_PATRONYMIC = (By.CSS_SELECTOR, 'div.test-locator-sf-patronymic input.ui-textinput__input')

    # Локатор поля "Дата рождения"
    LOCATOR_BIRTH_DATE = (By.CSS_SELECTOR, 'input.ui-date-time-input-reset')

    # Локатор поля "Электорнная почта"
    LOCATOR_EMAIL = (By.CSS_SELECTOR, 'div.test-locator-sf-email input.ui-textinput__input')

    # Локатор поля "Профессия"
    LOCATOR_PROFESSION = (By.CSS_SELECTOR, 'div.test-locator-sf-profession input.ui-textinput__input')

    # Локатор поля "Страна"
    LOCATOR_COUNTRY = (By.CSS_SELECTOR, 'div.test-locator-sf-school-country')

    # Локатор выбора страны Австрия
    LOCATOR_COUNTRY_TRUE = (By.XPATH, '//option[contains(text(),\'Австрия\')]')

    # Локатор поля "Город"
    LOCATOR_CITY = (By.CSS_SELECTOR, 'div.test-locator-sf-school-city input.ui-textinput__input')

    # Локатор поля "Название организации"
    LOCATOR_ORGANIZATION = (By.CSS_SELECTOR, 'div.test-locator-sf-school-organization input.ui-textinput__input')

    # Локатор поля "Школа"
    LOCATOR_SCHOOL = (By.CSS_SELECTOR, 'div.test-locator-sf-school-school input.ui-textinput__input')

    # Локатор поля "Класс"
    LOCATOR_GRADE = (By.CSS_SELECTOR, 'div.test-locator-sf-school-grade input.ui-textinput__input')

    # Локатор поля "ВОШ-логин"
    LOCATOR_VOSH_LOGIN = (By.CSS_SELECTOR, 'div.test-locator-sf-vosh-login-optional input.ui-textinput__input')

    # Локатор поля "Телефон"
    LOCATOR_PHONE = (By.CSS_SELECTOR, 'div.test-locator-sf-phone input.ui-textinput__input')

    # Локатор поля СНИЛС
    LOCATOR_SNILS_TEXT = (By.CSS_SELECTOR, 'div.test-locator-sf-snils-opt input.ui-textinput__input')

    LOCATOR_REGISTER_BUTTON = (By.CSS_SELECTOR, 'span.ui-button__content ')

    LOCATOR_SUCCES_MESSAGE = (By.CSS_SELECTOR, 'div.text-l.smt-auth-registration-panel__success-message')

    LOCATOR_BUTTON_BACK = (By.CSS_SELECTOR, 'span.ui-button__content ')

    LOCATOR_REGISTER_PAGE = (By.CSS_SELECTOR, 'div.smt-auth-register-page__content')
