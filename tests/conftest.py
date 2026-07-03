import pytest
from selenium import webdriver

from helpers.api_client import StellarBurgersApi
from helpers.data import UserData
from helpers import urls
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()

    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def created_user():
    user_data = UserData.get_unique_user()
    response = StellarBurgersApi.create_user(user_data)
    access_token = response.json().get("accessToken")

    yield user_data, access_token

    if access_token:
        StellarBurgersApi.delete_user(access_token)


@pytest.fixture
def authorized_driver(driver, created_user):
    user_data, _ = created_user

    driver.get(urls.LOGIN_PAGE)

    login_page = LoginPage(driver)
    login_page.login(user_data["email"], user_data["password"])

    main_page = MainPage(driver)
    main_page.is_constructor_title_visible()

    return driver