import time
from pages.elements.buttons_page import ButtonsPage


class TestButtonsPage:
    def test_press_all_buttons(self, driver):
        # клик на все поля
        form_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
        form_page.open()
        form_page.press_all_buttons()
        double_click_res, right_click_res, click_res = form_page.result()
        time.sleep(2)
        assert double_click_res == "You have done a double click"
        assert right_click_res == "You have done a right click"
        assert click_res == "You have done a dynamic click"
