from selenium.webdriver import Keys
from pages.base_page import BasePage
from locators.elements.radiobutton_page_locators import RadiobuttonLocators as locators


class RadiobuttonPage(BasePage):
    def select_yes(self):
        self.element_is_visible(locators.yes_btn).click()

    def select_impressive(self):
        self.element_is_visible(locators.impressive_btn).click()

    def select_no(self):
        self.element_is_visible(locators.no_btn).click()

    def result(self):
        return self.element_is_visible(locators.result).text
