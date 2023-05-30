import time
from pages.elements.radiobutton_page import RadiobuttonPage


class TestRadiobutton:
    def test_yes_and_impressive(self, driver):
        form_page = RadiobuttonPage(driver, 'https://demoqa.com/radio-button')
        form_page.open()
        form_page.select_yes()
        result = form_page.result()
        time.sleep(1)
        assert result == 'Yes'
        form_page.select_impressive()
        result = form_page.result()
        time.sleep(1)
        assert result == 'Impressive'

# тест с ошибкой
    def test_no(self, driver):
        form_page = RadiobuttonPage(driver, 'https://demoqa.com/radio-button')
        form_page.open()
        form_page.select_no()
        result = form_page.result()
        time.sleep(1)
        assert result == 'No'
