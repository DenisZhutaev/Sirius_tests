import pytest
from config import *
from time import sleep


def test_code_two_hundred(auth):
    assert auth.status_code() == 200


def test_secure_connection(auth):
    auth.go_to_site()
    assert auth.base_url.startswith("https://"), "Соединение не защищено HTTPS"


def test_language_switching(auth):
    auth.go_to_site()
    if auth.find_element(auth.LOCATOR_LANG).text == 'Рус':
        auth.click_element(auth.LOCATOR_LANG)
        auth.click_element(auth.LOCATOR_LANG_ENG)
        assert auth.find_element(auth.LOCATOR_LANG_ENG_TEXT)
    elif auth.find_element(auth.LOCATOR_LANG).text == 'Eng':
        auth.click_element(auth.LOCATOR_LANG)
        auth.click_element(auth.LOCATOR_LANG_RU)
        assert auth.find_element(auth.LOCATOR_LANG_RU_TEXT)


def test_behavior_rules_link(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BEHAVIOR_RULES)
    auth.switch_tab()
    assert auth.find_element(auth.LOCATOR_BEHAVIOR_RULES_TITLE)


def test_personal_data_link(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_PERSONAL_DATA)
    auth.switch_tab()
    assert auth.status_code() == 200


def test_term_of_use(auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_TERMS_OF_USE)
    auth.switch_tab()
    assert auth.status_code() == 200


def test_radio_button(auth):
    auth.go_to_site()
    if auth.find_element(auth.LOCATOR_MAIN_OLYMPIAD) == auth.LOCATOR_OLYMPIAD_TRUE:
        auth.click_element(auth.LOCATOR_ADDITIONAL_OLYMPIAD)
        assert auth.find_element(auth.LOCATOR_ADDITIONAL_OLYMPIAD) == auth.LOCATOR_OLYMPIAD_FALSE
        assert auth.find_element(auth.LOCATOR_MAIN_OLYMPIAD_OLYMPIAD) == auth.LOCATOR_OLYMPIAD_TRUE
    elif auth.find_element(auth.LOCATOR_MAIN_OLYMPIAD) == auth.LOCATOR_OLYMPIAD_FALSE:
        auth.click_element(auth.LOCATOR_MAIN_OLYMPIAD)
        assert auth.find_element(auth.LOCATOR_ADDITIONAL_OLYMPIAD) == auth.LOCATOR_OLYMPIAD_FALSE
        assert auth.find_element(auth.LOCATOR_MAIN_OLYMPIAD) == auth.LOCATOR_OLYMPIAD_TRUE


def test_checbox_button(auth):
    auth.go_to_site()
    checkboxes = auth.find_elements(auth.LOCATOR_CHECKBOX_RULES)
    for checkbox in checkboxes:
        checkbox.click()
        assert auth.find_element(auth.LOCATOR_CHECKBOX_TRUE)


@pytest.mark.parametrize('snils_num', [SNILS_11_FALSE, SNILS_CHECK_SUM_FALSE, SNILS_LESS_11, SNILS_ONLY_NUM],
                         ids=['SNILS must consist of exactly 11 digits', 'SNILS checksum does not match',
                              'SNILS cannot be less than 11 digits', 'SNILS must contain only numbers'])
def test_auth_empty_phone(auth, snils_num):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_SNILS_TEXT)
    auth.input_data(auth.LOCATOR_SNILS_TEXT, snils_num)
    assert auth.find_element(auth.LOCATOR_WRROR_MESSAGE)


def test_valid_authorization_and_return(auth):
    """
    Валидный тест регистрации участника олимпиады

    :param auth:
    :return: None
    """
    auth.go_to_site()

    # Словар основных локаторов
    data_dict = {
        auth.LOCATOR_NAME: VALID_NAME,
        auth.LOCATOR_LAST_NAME: VALID_LAST_NAME,
        auth.LOCATOR_PATRONYMIC: VALID_PATRONYMIC,
        auth.LOCATOR_EMAIL: EMAIL,
        auth.LOCATOR_PROFESSION: VALID_PROFESSION,
        auth.LOCATOR_CITY: VALID_CITY,
        auth.LOCATOR_ORGANIZATION: VALID_ORGANIZATION,
        auth.LOCATOR_SCHOOL: VALID_SCHOOL,
        auth.LOCATOR_GRADE: VALID_GRADE,
        auth.LOCATOR_VOSH_LOGIN: VOCH_NUM,
        auth.LOCATOR_PHONE: VALID_TEL,
        auth.LOCATOR_SNILS_TEXT: VALID_SNILS
    }

    # Обработка сложного поля, дата с ожиданием
    auth.input_data(auth.LOCATOR_BIRTH_DATE, VALID_DOB)
    sleep(1)

    # Обработка сложного поля, Страна с ожиданием
    auth.find_element(auth.LOCATOR_COUNTRY)
    sleep(3)
    auth.click_element(auth.LOCATOR_COUNTRY_TRUE)

    # Прожод по словарю с локаторами основных полей
    auth.input_data_dict(data_dict)

    # Проставление галочек в чекбоксах
    checkboxes = auth.find_elements(auth.LOCATOR_CHECKBOX_RULES)
    for checkbox in checkboxes:
        checkbox.click()

    # Клик на поле регистрации
    auth.click_element(auth.LOCATOR_REGISTER_BUTTON)

    # Проверка, что попали на страницу с сообщением об отправке письма
    assert auth.find_element(auth.LOCATOR_SUCCES_MESSAGE)

    # Проверка, существования смены языка на странице подтверждения регистрации
    assert auth.find_element(auth.LOCATOR_LANG)

    # Нажимаем на кнопку "Назад"
    auth.click_element(auth.LOCATOR_BUTTON_BACK)

    # Проверка, что вернудись на страницу регистрации
    assert auth.find_element(auth.LOCATOR_REGISTER_PAGE)

