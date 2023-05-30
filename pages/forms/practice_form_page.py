import os

from selenium.webdriver import Keys

from generator.generator import generate_person, generate_file
from pages.base_page import BasePage
from locators.forms.practice_form_page_locators import PracticeFormLocators as locators


class PracticeFormPage(BasePage):
    def fill_in_and_submit(self):
        person = generate_person()
        path = generate_file()
        self.element_is_visible(locators.first_name).send_keys(person.first_name)
        self.element_is_visible(locators.last_name).send_keys(person.last_name)
        self.element_is_visible(locators.email).send_keys(person.email)
        self.element_is_visible(locators.address).send_keys(person.address)
        self.element_is_visible(locators.number).send_keys(person.number)
        self.element_is_visible(locators.picture).send_keys(path)
        os.remove(path)
        self.element_is_visible(locators.gender).click()
        self.element_is_visible(locators.hobbies).click()
        enter = self.element_is_visible(locators.subject)
        enter.send_keys(person.subject)
        enter.send_keys(Keys.ENTER)
        self.element_is_visible(locators.submit).click()
        return person

    def form_result(self):
        result_list = self.elements_are_visible(locators.result_table)
        result_text = [i.text for i in result_list]
        return result_text
