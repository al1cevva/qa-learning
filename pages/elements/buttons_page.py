from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from locators.elements.buttons_page_locators import ButtonsPageLocators as locators


class ButtonsPage(BasePage):
    def press_all_buttons(self):
        double_click_btn = self.element_is_visible(locators.double_click_btn)
        right_click_btn = self.element_is_visible(locators.right_click_btn)
        action = ActionChains(self.driver)
        action.double_click(double_click_btn).perform()
        action.context_click(right_click_btn).perform()
        self.element_is_visible(locators.click_btn).click()

    def result(self):
        double_click = self.element_is_visible(locators.double_click_res).text
        right_click = self.element_is_visible(locators.right_click_res).text
        click_res = self.element_is_visible(locators.click_res).text
        return double_click, right_click, click_res
