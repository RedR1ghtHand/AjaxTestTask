import subprocess


def get_android_udid():
    result = subprocess.check_output(["adb", "devices"]).decode("utf-8")
    lines = result.strip().split("\n")
    devices = [line.split("\t")[0] for line in lines[1:] if "device" in line]
    if devices:
        return devices[0]
    else:
        return None


def android_get_desired_capabilities():
    udid = get_android_udid()
    if udid:
        return {
            'autoGrantPermissions': True,
            'automationName': 'uiautomator2',
            'newCommandTimeout': 500,
            'noSign': True,
            'platformName': 'Android',
            'platformVersion': '10',
            'resetKeyboard': True,
            'systemPort': 8301,
            'takesScreenshot': True,
            'udid': udid,
            'appPackage': 'com.ajaxsystems',
            'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
        }
    else:
        return {
            'autoGrantPermissions': True,
            'automationName': 'uiautomator2',
            'newCommandTimeout': 500,
            'noSign': True,
            'platformName': 'Android',
            'platformVersion': '10',
            'resetKeyboard': True,
            'systemPort': 8301,
            'takesScreenshot': True,
            'appPackage': 'com.ajaxsystems',
            'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
        }