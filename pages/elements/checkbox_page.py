from selenium.common import NoSuchElementException
from pages.base_page import BasePage
from locators.elements.checkbox_page_locators import CheckboxPageLocators as locators


class CheckboxPage(BasePage):
    def submit_all_elements(self):
        self.element_is_visible(locators.home_checkbox).click()

    def result(self):
        return self.element_is_visible(locators.result).text

    def submit_some_elements(self):
        self.element_is_visible(locators.home_btn).click()
        self.element_is_visible(locators.desktop_btn).click()
        self.element_is_visible(locators.notes_node).click()
        self.element_is_visible(locators.documents_checkbox).click()

    def submit_one_element(self):
        self.element_is_visible(locators.documents_checkbox).click()

