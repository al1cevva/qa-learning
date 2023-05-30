from selenium.webdriver.common.by import By


class CheckboxPageLocators:
    home_checkbox = (By.XPATH, '//label[@for="tree-node-home"]')
    home_btn = (By.XPATH, '//button[@Title="Toggle"]')
    result = (By.XPATH, '//div[@id="result"]')
    collapse_btn = (By.XPATH, '//button[@title="Collapse all"]')
    expand_btn = (By.XPATH, '//button[@title="Expand all"]')
    desktop_btn = (By.XPATH, "//div[@id='tree-node']//li[1]//li//button")

    documents_checkbox = (By.XPATH, "//label[@for='tree-node-documents']")
    notes_node = (By.XPATH, "//label[@for='tree-node-notes']")
    