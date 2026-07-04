from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):
    def click_constructor_link(self):
        self.click(FeedPageLocators.CONSTRUCTOR_LINK)

    def is_order_feed_title_visible(self):
        return self.is_visible(FeedPageLocators.ORDER_FEED_TITLE)

    def get_total_counter_value(self):
        return int(self.get_text(FeedPageLocators.TOTAL_COUNTER))

    def get_today_counter_value(self):
        return int(self.get_text(FeedPageLocators.TODAY_COUNTER))

    def get_orders_in_progress_numbers(self):
        elements = self.find_elements(FeedPageLocators.ORDERS_IN_PROGRESS)
        return [element.text for element in elements if element.text]

    def wait_order_number_in_progress(self, order_number):
        self.wait_text_in_page_source(order_number)

    def wait_today_counter_increased(self, old_value):
        self.wait.until(
            lambda driver: self.get_today_counter_value() > old_value
        )