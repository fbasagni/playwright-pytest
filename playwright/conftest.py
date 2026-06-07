import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.planos_page import PlanosPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page)

@pytest.fixture
def planos_page(page: Page) -> PlanosPage:
    return PlanosPage(page)

@pytest.fixture
def checkout_page(page: Page) -> CheckoutPage:
    return CheckoutPage(page)
