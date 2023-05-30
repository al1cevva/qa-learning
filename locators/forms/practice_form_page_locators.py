
from selenium.webdriver.common.by import By
from random import randint


class PracticeFormLocators:
    last_name = (By.XPATH, '//input[@id="lastName"]')
    first_name = (By.XPATH, '//input[@id="firstName"]')
    gender = (By.XPATH, f'//label[@for="gender-radio-{randint(1, 3)}"]')
    number = (By.XPATH, '//input[@id="userNumber"]')
    hobbies = (By.XPATH, f'//label[@for="hobbies-checkbox-{randint(1, 3)}"]')
    subject = (By.XPATH, '//input[@id="subjectsInput"]')
    email = (By.XPATH, '//input[@id="userEmail"]')
    picture = (By.XPATH, '//input[@id="uploadPicture"]')
    address = (By.XPATH, '//textarea[@id="currentAddress"]')
    submit = (By.XPATH, '//button[@id="submit"]')

    result_table = (By.XPATH, '//div[@class="table-responsive"]//td[2]')
