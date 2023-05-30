import time

from pages.forms.practice_form_page import PracticeFormPage


class TestPracticeFormPage:
    def test_page(self, driver):
        form_page = PracticeFormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        person = form_page.fill_in_and_submit()
        result = form_page.form_result()
        time.sleep(2)
        assert f'{person.first_name} {person.last_name}' == result[0]
        assert person.email == result[1]

