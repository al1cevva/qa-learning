import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver_service = Service(ChromeDriverManager().install())
    #options.add_argument('ignore-certificate-errors')
    prefs = {"download.default_directory":"C:\\Users\\alisa\\PycharmProjects\\DEMOQA"}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=driver_service, chrome_options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
