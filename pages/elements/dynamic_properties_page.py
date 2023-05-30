from selenium.common import TimeoutException, WebDriverException

from pages.base_page import BasePage
from locators.elements.dynamic_properties_page_locators import DynamicPropertiesLocators as locators


class DynamicPropertiesPage(BasePage):
    def button_appears_in_five(self):
        try:
            self.element_is_present(locators.appears_in_five_seconds_btn)
            return True
        except TimeoutException:
            return False

    def button_changes_color(self):
        try:
            self.element_is_present(locators.changes_color_btn)
            return True
        except TimeoutException:
            return False

    def button_unlocks_in_five(self):
        try:
            self.element_to_be_clickable(locators.enables_in_five_seconds_btn).click()
            return True
        except WebDriverException:
            print("Element is not clickable")
            return False

    def rand_id_label(self):
        return self.element_is_visible(locators.label_with_rand_id).text
