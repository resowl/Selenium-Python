import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager
from selenium.webdriver.chrome.options import Options


opt = Options()
opt.add_argument("--headless")
@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):

    if request.param == 'chrome':
        s = Service(executable_path="libs/chromedriver.exe")
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(service=s)
    elif request.param == 'firefox':
        s = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=s)
    elif request.param == "edge":
        s = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Ie(service=s)
    # elif request.param == "opera":
    #     s = Service(executable_path=OperaDriver().install())
    #     driver = webdriver.Opera(service_args=s)
    else:
        s = Service(IEDriverManager().install())
        driver = webdriver.Chrome(service=s)

    request.cls.driver = driver
    yield
    driver.close()