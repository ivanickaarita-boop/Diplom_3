from selenium.webdriver.common.by import By


class FeedPageLocators:
    ORDER_FEED_TITLE = (By.XPATH, '//h1[text()="Лента заказов"]')
    CONSTRUCTOR_LINK = (By.CSS_SELECTOR, 'a[href="/"]')

    TOTAL_COUNTER = (
        By.XPATH,
        '//p[text()="Выполнено за все время:"]/following-sibling::p'
    )

    TODAY_COUNTER = (
        By.XPATH,
        '//p[text()="Выполнено за сегодня:"]/following-sibling::p'
    )

    ORDERS_IN_PROGRESS = (
        By.XPATH,
        '//p[text()="В работе:"]/following-sibling::ul/li'
    )