from selenium.webdriver.common.by import By


class UploadAndDownloadPageLocators:
    input_file = (By.XPATH, "//form//input")
    output_file = (By.ID, "downloadButton")
    uploaded_file_path = (By.ID, "uploadedFilePath")

