from time import sleep

from .buttons import ButtonsXpath
from framework.login_page import LoginPage


def test_user_login_negative_case(driver):
    login_page = LoginPage(driver)
    login_page.login('qa.ajax.app.automation@gmail.com', 'definitely_wrong_password')
    sleep(3)

    assert driver.find_element_by_xpath(ButtonsXpath['Invalid_email_format']).is_enabled()


def test_user_login_positive_case(driver):
    login_page = LoginPage(driver)
    login_page.login('qa.ajax.app.automation@gmail.com', 'qa_automation_password')
    sleep(3)

    assert driver.find_element_by_xpath(ButtonsXpath['AddHub']).is_enabled()

