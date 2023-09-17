from.buttons import ButtonsXpath


def test_click_element_log_in(driver):
    element = driver.find_element_by_xpath(ButtonsXpath["LogIn"])
    element.click()

    element_back = driver.find_element_by_xpath(ButtonsXpath["Back_from_LogIn"])
    element_back.click()

    assert element.is_enabled()


def test_click_element_create_acc(driver):
    element = driver.find_element_by_xpath(ButtonsXpath["CreateAcc"])
    element.click()

    element_back = driver.find_element_by_xpath(ButtonsXpath["Back_from_CreateAcc"])
    element_back.click()

    assert element.is_enabled()
