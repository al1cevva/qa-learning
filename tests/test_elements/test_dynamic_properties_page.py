from pages.elements.dynamic_properties_page import DynamicPropertiesPage


class TestDynamicPropertiesPage:
    def test_appears_in_five_btn(self, driver):
        form_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
        form_page.open()
        appears_in_five_btn = form_page.button_appears_in_five()
        assert appears_in_five_btn == True

    def test_changes_color_btn(self, driver):
        form_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
        form_page.open()
        changes_color_btn = form_page.button_changes_color()
        assert changes_color_btn == True

    def test_clickable_in_five_btn(self, driver):
        form_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
        form_page.open()
        clickable_in_five_btn = form_page.button_unlocks_in_five()
        assert clickable_in_five_btn == True

    def test_rand_id_label(self, driver):
        form_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
        form_page.open()
        rand_id_label = form_page.rand_id_label()
        assert rand_id_label in driver.page_source
