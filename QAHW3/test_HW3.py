import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_itcareerhub_ui_elements(driver):
    driver.get("https://itcareerhub.de/ru")

    wait = WebDriverWait(driver, 10)

    # 🔹 Проверка логотипа
    logo = wait.until(EC.presence_of_element_located((By.XPATH, "//img[contains(@alt,'logo')]")))
    assert logo.is_displayed()

    # 🔹 Проверка ссылок меню
    menu_items = [
        "Программы",
        "Способы оплаты",
        "Новости",
        "О нас",
        "Отзывы"
    ]

    for item in menu_items:
        element = wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//a[contains(text(),'{item}')]")
        ))
        assert element.is_displayed()

    # 🔹 Проверка переключателя языков
    ru = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'ru')]")))
    de = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'de')]")))

    assert ru.is_displayed()
    assert de.is_displayed()

    # 🔹 Клик по иконке телефона
    phone_icon = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(@href,'tel')]")
    ))
    phone_icon.click()

    # 🔹 Проверка текста
    expected_text = "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами"

    message = wait.until(EC.presence_of_element_located(
        (By.XPATH, f"//*[contains(text(),'{expected_text}')]")
    ))

    assert message.is_displayed()