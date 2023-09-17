from time import sleep

from framework.login_page import LoginPage
from .buttons import SideBarButtonsXpath, ButtonsXpath


def test_sidebar_interaction(driver):
    login_page = LoginPage(driver)
    login_page.login('qa.ajax.app.automation@gmail.com', 'qa_automation_password')
    sleep(5)

    driver.swipe(
        start_x=0,
        start_y=1000,
        end_x=800,
        end_y=1000,
        duration=800
    )

    for xpath in SideBarButtonsXpath.values():
        assert driver.find_element_by_xpath(xpath).is_enabled()

    driver.swipe(
        start_x=800,
        start_y=1000,
        end_x=0,
        end_y=1000,
        duration=800
    )

    assert driver.find_element_by_xpath(ButtonsXpath['AddHub']).is_enabled()




