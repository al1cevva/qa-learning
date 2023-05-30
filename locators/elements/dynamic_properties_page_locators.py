from selenium.webdriver.common.by import By


class DynamicPropertiesLocators:
    enables_in_five_seconds_btn = (By.ID, 'enableAfter')
    changes_color_btn = (By.XPATH, '//button[@class="mt-4 text-danger btn btn-primary"]')
    appears_in_five_seconds_btn = (By.ID, 'visibleAfter')
    label_with_rand_id = (By.XPATH, '//div/p')
