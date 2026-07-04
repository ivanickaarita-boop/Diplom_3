import allure

from helpers import urls
from pages.main_page import MainPage
from pages.feed_page import FeedPage


class TestOrderFeed:
    def create_order_and_get_number(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        main_page.open(urls.MAIN_PAGE)
        main_page.drag_ingredient_to_basket()
        main_page.create_order()
        main_page.wait_order_modal_opened()

        return main_page.get_order_number()

    @allure.title("Счётчик Выполнено за всё время увеличивается после создания заказа")
    def test_total_counter_increases_after_order_created(self, authorized_driver):
        feed_page = FeedPage(authorized_driver)
        feed_page.open(urls.FEED_PAGE)
        total_before = feed_page.get_total_counter_value()

        self.create_order_and_get_number(authorized_driver)

        feed_page.open(urls.FEED_PAGE)
        total_after = feed_page.get_total_counter_value()

        assert total_after > total_before

    @allure.title("Счётчик Выполнено за сегодня увеличивается после создания заказа")
    def test_today_counter_increases_after_order_created(self, authorized_driver):
        feed_page = FeedPage(authorized_driver)
        feed_page.open(urls.FEED_PAGE)
        today_before = feed_page.get_today_counter_value()

        self.create_order_and_get_number(authorized_driver)

        feed_page.open(urls.FEED_PAGE)
        feed_page.wait_today_counter_increased(today_before)

        assert feed_page.get_today_counter_value() > today_before

    @allure.title("Номер заказа появляется в разделе В работе")
    def test_order_number_appears_in_progress_section(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        main_page.open(urls.MAIN_PAGE)
        main_page.drag_ingredient_to_basket()
        main_page.create_order()
        main_page.wait_order_modal_opened()

        order_number = main_page.get_order_number()
        main_page.click_order_feed_link()

        feed_page = FeedPage(authorized_driver)
        feed_page.wait_order_number_in_progress(order_number)

        assert order_number in authorized_driver.page_source