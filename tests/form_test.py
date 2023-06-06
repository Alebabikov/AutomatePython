from pages.form_page import FormPage

class TestFormPage:

    def test_form(self, driver):
        form_page = FormPage(driver, 'https://selenium-python.readthedocs.io/getting-started.html')
        form_page.open()
        form_page.fill_fields_and_submit()




