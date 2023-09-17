def get_my_custom_capabilities():
    return {
        "platformName": "Android",
        "appium:deviceName": "6926d9cb",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": "com.ajaxsystems",
        "appium:appActivity": "com.ajaxsystems.ui.activity.LauncherActivity",
        "appium:autoGrantPermissions": True
    }


def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'deviceName': '6926d9cb',
        'platformName': 'Android',
        'platformVersion': '10',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
    }
