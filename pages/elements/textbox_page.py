from selenium.common import NoSuchElementException
from selenium.webdriver import Keys

import data.data
from generator.generator import generate_person
from pages.base_page import BasePage
from locators.elements.textbox_page_locators import TextboxPageLocators as locators


class TextboxPage(BasePage):
    def fill_in_and_submit(self):
        person = generate_person()
        self.element_is_visible(locators.username).send_keys(person.first_name)
        self.element_is_visible(locators.email).send_keys(person.email)
        self.element_is_visible(locators.currentAddress).send_keys(person.address)
        self.element_is_visible(locators.permanentAddress).send_keys(person.permanentAddress)

        self.element_is_visible(locators.submit_btn).click()
        return person

    def result(self):
        person = data.data.Person
        person.first_name = self.element_is_visible(locators.result_username).text
        person.email = self.element_is_visible(locators.result_email).text
        person.address = self.element_is_visible(locators.result_currentAddress).text
        person.permanentAddress = self.element_is_visible(locators.result_permanentAddress).text
        return person

    def clear(self):
        self.element_is_visible(locators.username).clear()
        self.element_is_visible(locators.email).clear()
        self.element_is_visible(locators.currentAddress).clear()
        self.element_is_visible(locators.permanentAddress).clear()

    def wrong_email(self):
        self.element_is_visible(locators.email).send_keys('wrong_email')
        self.element_is_visible(locators.submit_btn).click()
        try:
            self.element_is_visible(locators.email_error)
        except NoSuchElementException:
            return False
        return True
