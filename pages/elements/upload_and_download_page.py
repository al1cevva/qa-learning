import time
from pages.base_page import BasePage
from locators.elements.upload_and_download_page_locators import UploadAndDownloadPageLocators as locators
from generator.generator import generate_file
import os


class UploadAndDownloadPage(BasePage):
    def upload(self):
        path = generate_file()
        self.element_is_visible(locators.input_file).send_keys(path)
        file_name = os.path.basename(path)
        os.remove(path)
        return file_name

    def result_upload(self):
        return self.element_is_visible(locators.uploaded_file_path).text

    def download(self):
        self.element_is_visible(locators.output_file).click()

    def result_download(self):
        file_path = "C:\\Users\\alisa\PycharmProjects\DEMOQA\sampleFile.jpeg"
        time.sleep(2)
        res = os.path.exists(file_path)
        if res:
            os.remove(file_path)
        return res
