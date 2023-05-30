from selenium.webdriver.common.by import By


class ButtonsPageLocators:
    double_click_btn = (By.XPATH, "//button[text()='Double Click Me']")
    right_click_btn = (By.XPATH, "//button[text()='Right Click Me']")
    click_btn = (By.XPATH, "//button[text()='Click Me']")

    double_click_res = (By.XPATH, "//p[@id='doubleClickMessage']")
    right_click_res = (By.XPATH, "//p[@id='rightClickMessage']")
    click_res = (By.XPATH, "//p[@id='dynamicClickMessage']")
