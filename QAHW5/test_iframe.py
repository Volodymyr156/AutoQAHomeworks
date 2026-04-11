import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://bonigarcia.dev/selenium-webdriver-java/iframes.html"
NEEDED_TEXT = "semper posuere integer et senectus justo curabitur."


@pytest.fixture
def driver():
    d = webdriver.Firefox()
    d.maximize_window()
    yield d
    d.quit()


def test_text_in_iframe(driver):
    wait = WebDriverWait(driver, 20)
    driver.get(URL)

    frames = driver.find_elements(By.CSS_SELECTOR, "#my-iframe")
    assert frames, "No frames found"

    driver.switch_to.frame(frames[0])

    body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content")))
    assert NEEDED_TEXT in body.text