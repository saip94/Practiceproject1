import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=['chrome','firefox'],scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "firefox":
        firefox_path="E:/Chrome downloads/geckodriver-v0.31.0-win64/geckodriver.exe"
        web_driver = webdriver.Firefox(executable_path=firefox_path)
    request.cls.driver=web_driver
    yield
    web_driver.close()

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class Test_Google(BaseTest):

    def test_google_title(self):
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google","test failed"
