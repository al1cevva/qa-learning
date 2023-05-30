import time

from pages.elements.textbox_page import TextboxPage


class TestTextboxPage:
    def test_page_all_fields(self, driver):
        #заполнение всех полей
        form_page = TextboxPage(driver, 'https://demoqa.com/text-box')
        form_page.open()
        person = form_page.fill_in_and_submit()
        result = form_page.result()
        time.sleep(2)
        assert f'Name:{person.first_name}' == result.first_name
        assert f'Email:{person.email}' == result.email
        assert f'Current Address :{person.address}' == result.address
        #в тексте ошибка
        assert f'Permananet Address :{person.permanentAddress}' == result.permanentAddress
        form_page.clear()
        #неправильный ввод имейла
        result_error = form_page.wrong_email()
        assert result_error == True
