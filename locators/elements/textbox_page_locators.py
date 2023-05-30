from selenium.webdriver.common.by import By


class TextboxPageLocators:
    username = (By.XPATH,"//input[@id='userName']")
    email = (By.XPATH,"//input[@id='userEmail']")
    email_error = (By.XPATH,"//input[@class='mr-sm-2 field-error form-control']")
    currentAddress = (By.XPATH,"//textarea[@id='currentAddress']")
    permanentAddress = (By.XPATH,"//textarea[@id='permanentAddress']")
    submit_btn = (By.XPATH,"//button[@id='submit']")

    result_username = (By.XPATH,"//p[@id='name']")
    result_email = (By.XPATH,"//p[@id='email']")
    result_currentAddress = (By.XPATH,"//p[@id='currentAddress']")
    result_permanentAddress = (By.XPATH,"//p[@id='permanentAddress']")
