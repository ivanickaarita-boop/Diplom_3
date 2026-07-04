from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_LINK = (By.CSS_SELECTOR, 'a[href="/"]')
    ORDER_FEED_LINK = (By.CSS_SELECTOR, 'a[href="/feed"]')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти в аккаунт"]')

    CONSTRUCTOR_TITLE = (By.XPATH, '//h1[text()="Соберите бургер"]')

    INGREDIENT_CARD = (
        By.XPATH,
        '//p[text()="Флюоресцентная булка R2-D3"]/ancestor::a'
    )

    INGREDIENT_COUNTER = (
        By.XPATH,
        '//p[text()="Флюоресцентная булка R2-D3"]/ancestor::a'
        '//p[contains(@class,"counter_counter__num")]'
    )

    MODAL_TITLE = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, 'button[class*="Modal_modal__close"]')

    TOP_BUN_DROP_AREA = (
        By.XPATH,
        '//span[contains(text(),"Перетяните булочку сюда")]'
    )

    CREATE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')

    ORDER_NUMBER = (
        By.CSS_SELECTOR,
        'h2[class*="text_type_digits-large"]'
    )

    ORDER_ACCEPTED_TEXT = (
        By.XPATH,
        '//p[text()="Ваш заказ начали готовить"]'
    )

    ORDER_MODAL_CLOSE = (
        By.CSS_SELECTOR,
        'button[class*="Modal_modal__close"]'
    )