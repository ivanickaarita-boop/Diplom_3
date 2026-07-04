from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def click_constructor_link(self):
        self.click(MainPageLocators.CONSTRUCTOR_LINK)

    def click_order_feed_link(self):
        self.click(MainPageLocators.ORDER_FEED_LINK)

    def is_constructor_title_visible(self):
        return self.is_visible(MainPageLocators.CONSTRUCTOR_TITLE)

    def open_ingredient_details(self):
        self.click(MainPageLocators.INGREDIENT_CARD)

    def is_ingredient_modal_opened(self):
        return self.is_visible(MainPageLocators.MODAL_TITLE)

    def close_ingredient_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_until_invisible(MainPageLocators.MODAL_TITLE)

    def get_ingredient_counter_value(self):
        return self.get_text(MainPageLocators.INGREDIENT_COUNTER)

    def drag_ingredient_to_basket(self):
        self.drag_and_drop(
            MainPageLocators.INGREDIENT_CARD,
            MainPageLocators.TOP_BUN_DROP_AREA,
        )

    def create_order(self):
        self.click(MainPageLocators.CREATE_ORDER_BUTTON)

    def get_order_number(self):
        return self.get_text(MainPageLocators.ORDER_NUMBER)

    def wait_order_modal_opened(self):
        return self.is_visible(MainPageLocators.ORDER_ACCEPTED_TEXT)

    def close_order_modal(self):
        self.click(MainPageLocators.ORDER_MODAL_CLOSE)
        self.wait_until_invisible(MainPageLocators.ORDER_ACCEPTED_TEXT)