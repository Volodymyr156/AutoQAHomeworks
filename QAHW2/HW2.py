from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

options = Options()
driver = webdriver.Firefox(options=options)


driver.get("https://itcareerhub.de/ru")
driver.maximize_window()
time.sleep(3)

payment_section = driver.find_element(By.XPATH, "//*[contains(text(),'Способы оплаты')]")
driver.execute_script("arguments[0].scrollIntoView();", payment_section)
time.sleep(2)

payment_section.screenshot("payment_methods.png")

driver.quit()