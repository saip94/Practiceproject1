import pytest
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

def test_google():
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.google.com")
    assert driver.title=='Google','title failed'
    driver.quit()
