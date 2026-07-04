from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        element = self.find_clickable_element(locator)
        try:
            element.click()
        except Exception:
            self.click_with_js(element)

    def click_with_js(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def get_text(self, locator):
        return self.find_element(locator).text

    def is_visible(self, locator):
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False

    def wait_until_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def is_firefox(self):
        return self.driver.capabilities["browserName"] == "firefox"

    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)

        if self.is_firefox():
            self.drag_and_drop_with_js(source, target)
        else:
            ActionChains(self.driver)\
                .click_and_hold(source)\
                .move_to_element(target)\
                .release()\
                .perform()

    def drag_and_drop_with_js(self, source, target):
        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();

            source.dispatchEvent(new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer
            }));

            target.dispatchEvent(new DragEvent('dragenter', {
                bubbles: true,
                cancelable: true,
                dataTransfer
            }));

            target.dispatchEvent(new DragEvent('dragover', {
                bubbles: true,
                cancelable: true,
                dataTransfer
            }));

            target.dispatchEvent(new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer
            }));

            source.dispatchEvent(new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer
            }));
            """,
            source,
            target,
        )

    def wait_text_in_page_source(self, text):
        self.wait.until(
            lambda driver: text in driver.page_source
        )