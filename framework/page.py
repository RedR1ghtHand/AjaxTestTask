from appium.webdriver.common.mobileby import MobileBy


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value):
        if by == 'xpath':
            return self.driver.find_element(MobileBy.XPATH, value)
        elif by == 'id':
            return self.driver.find_element(MobileBy.ID, value)
        elif by == 'name':
            return self.driver.find_element(MobileBy.NAME, value)

    def click_element(self, by, value):
        element = self.find_element(by, value)
        element.click()
