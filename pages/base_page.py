from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_page(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    def click(self, locator):
        self.find_element(locator).click()

    def get_current_url(self):
        return self.driver.current_url

    def is_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    def element_is_not_displayed(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def element_text(self, locator):
        return self.find_element(locator).text







