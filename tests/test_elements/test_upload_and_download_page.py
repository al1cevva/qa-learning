import time
from pages.elements.upload_and_download_page import UploadAndDownloadPage


class TestUploadAndDownloadPage:
    def test_download(self, driver):
        form_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
        form_page.open()
        form_page.download()
        result = form_page.result_download()
        time.sleep(2)
        assert result == True

    def test_upload(self, driver):
        form_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
        form_page.open()
        file_path = "C:\\fakepath\\" + form_page.upload()
        result_path = form_page.result_upload()
        time.sleep(2)
        assert file_path == result_path
