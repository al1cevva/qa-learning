import time
from pages.elements.checkbox_page import CheckboxPage


class TestTextboxPage:
    def test_select_all(self, driver):
        # заполнение всех полей
        form_page = CheckboxPage(driver, 'https://demoqa.com/checkbox')
        form_page.open()
        form_page.submit_all_elements()
        result = form_page.result()
        time.sleep(2)
        assert result == "You have selected :\nhome\ndesktop\nnotes\ncommands\ndocuments\nworkspace\nreact\nangular\n" \
                         "veu\noffice\npublic\nprivate\nclassified\ngeneral\ndownloads\nwordFile\nexcelFile"

    def test_some(self, driver):
        # выбрать только notes и documents
        form_page = CheckboxPage(driver, 'https://demoqa.com/checkbox')
        form_page.open()
        form_page.submit_some_elements()
        result = form_page.result()
        time.sleep(2)
        assert result == "You have selected :\nnotes\ndocuments\nworkspace\nreact\nangular\nveu\noffice\n" \
                         "public\nprivate\nclassified\ngeneral"
        form_page.submit_one_element()
        result = form_page.result()
        assert result == 'You have selected :\nnotes'
