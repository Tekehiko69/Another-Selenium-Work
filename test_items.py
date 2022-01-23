import time
from selenium.webdriver.common.by import By

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_check_add_to_cart_button(browser):

    browser.get(LINK)
    time.sleep(30)
    btn = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert btn is not None, 'Button add to basket not exist'
