import allure

from helpers import urls
from pages.main_page import MainPage
from pages.feed_page import FeedPage


class TestConstructor:
    @allure.title("Переход по клику на Конструктор")
    def test_click_constructor_link_opens_constructor_page(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open(urls.FEED_PAGE)

        feed_page.click_constructor_link()

        main_page = MainPage(driver)
        assert main_page.is_constructor_title_visible()

    @allure.title("Переход по клику на Лента заказов")
    def test_click_order_feed_link_opens_order_feed_page(self, driver):
        main_page = MainPage(driver)
        main_page.open(urls.MAIN_PAGE)

        main_page.click_order_feed_link()

        feed_page = FeedPage(driver)
        assert feed_page.is_order_feed_title_visible()

    @allure.title("Открытие всплывающего окна с деталями ингредиента")
    def test_click_ingredient_opens_ingredient_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open(urls.MAIN_PAGE)

        main_page.open_ingredient_details()

        assert main_page.is_ingredient_modal_opened()

    @allure.title("Закрытие всплывающего окна с деталями ингредиента")
    def test_close_ingredient_details_modal_by_close_button(self, driver):
        main_page = MainPage(driver)
        main_page.open(urls.MAIN_PAGE)
        main_page.open_ingredient_details()

        main_page.close_ingredient_modal()

        assert not main_page.is_ingredient_modal_opened()

    @allure.title("Увеличение счётчика ингредиента после добавления в заказ")
    def test_ingredient_counter_increases_after_adding_to_order(self, driver):
        main_page = MainPage(driver)
        main_page.open(urls.MAIN_PAGE)
        counter_before = main_page.get_ingredient_counter_value()

        main_page.drag_ingredient_to_basket()

        counter_after = main_page.get_ingredient_counter_value()

        assert int(counter_after) > int(counter_before)