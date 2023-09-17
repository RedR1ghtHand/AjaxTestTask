from .buttons import ButtonsXpath


def test_find_element_log_in(driver):
    element = driver.find_element_by_xpath(ButtonsXpath["LogIn"])

    assert element.is_enabled()


def test_find_element_create_acc(driver):
    element = driver.find_element_by_xpath(ButtonsXpath["CreateAcc"])

    assert element.is_enabled()


