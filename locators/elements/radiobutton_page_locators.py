from selenium.webdriver.common.by import By


class RadiobuttonLocators:
    yes_btn = (By.XPATH, "//label[@for='yesRadio']")
    impressive_btn = (By.XPATH, "//label[@for='impressiveRadio']")
    no_btn = (By.XPATH, "//label[@for='noRadio']")
    result = (By.XPATH, "//span[@class='text-success']")
