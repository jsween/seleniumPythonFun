from platform import system, architecture
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

CHROME_LINUX_DRIVER_32 = './drivers/chrome_2_27/linux_32/chromedriver'
CHROME_LINUX_DRIVER_64 = './drivers/chrome_2_27/linux_64/chromedriver'
CHROME_MAC_DRIVER = './drivers/chrome_2_27/mac/chromedriver'
CHROME_WINDOWS_DRIVER = './drivers/chrome_2_27/win/chromedriver.exe'

PHANTOM_LINUX_DRIVER_32 = './drivers/phantom_2_1_1/linux_32/phantomjs'
PHANTOM_LINUX_DRIVER_64 = './drivers/phantom_2_1_1/linux_64/phantomjs'
PHANTOM_MAC_DRIVER = './drivers/phantom_2_1_1/mac/phantomjs'
PHANTOM_WINDOWS_DRIVER = './drivers/phantom_2_1_1/win/phantomjs.exe'

GECKO_LINUX_DRIVER_32 = './drivers/gecko_0_14_0/linux_32/geckodriver'
GECKO_LINUX_DRIVER_64 = './drivers/gecko_0_14_0/linux_64/geckodriver'
GECKO_MAC_DRIVER = './drivers/gecko_0_14_0/mac/geckodriver'
GECKO_WINDOWS_DRIVER_32 = './drivers/gecko_0_14_0/win_32/geckodriver.exe'
GECKO_WINDOWS_DRIVER_64 = './drivers/gecko_0_14_0/win_64/geckodriver.exe'


def get_chrome_driver():
    """Return a Chrome driver"""
    return webdriver.Chrome(get_chrome_driver_location())


def get_phantom_driver():
    """Return a PhantomJS headless driver"""
    return webdriver.PhantomJS(get_phantom_driver_location())


def get_firefox_driver():
    """Return a Firefox driver ** NOT WORKING"""
    firefox_capabilities = DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True
    ff_profile_path = './profile/firefox'
    profile = webdriver.FirefoxProfile(profile_directory=ff_profile_path)
    return webdriver.Firefox(firefox_profile=profile,
                             capabilities=firefox_capabilities,
                             executable_path=get_gecko_driver_location())


def get_chrome_driver_location():
    """Detect the os version & architecture. Return the correct chrome driver string location."""
    s = system().lower()
    if s == 'windows':
        return CHROME_WINDOWS_DRIVER
    elif s == 'darwin':
        return CHROME_MAC_DRIVER
    elif s == 'linux' or s == 'linux2':
        if architecture()[0].lower() == '64bit':
            return CHROME_LINUX_DRIVER_64
        else:
            return CHROME_LINUX_DRIVER_32
    else:
        print ('Your OS version "' + s + '" is not supported')
        return ''


def get_phantom_driver_location():
    """Detect the os version & architecture. Return the correct phantom driver string location."""
    s = system().lower()
    if s == 'windows':
        return PHANTOM_WINDOWS_DRIVER
    elif s == 'darwin':
        return PHANTOM_MAC_DRIVER
    elif s == 'linux' or s == 'linux2':
        if architecture()[0].lower() == '64bit':
            return PHANTOM_LINUX_DRIVER_64
        else:
            return PHANTOM_LINUX_DRIVER_32
    else:
        print ('Your OS version "' + s + '" is not supported')
        return ''


def get_gecko_driver_location():
    """Detect the os version & architecture. Return the correct firefox driver string location."""
    s = system().lower()
    if s == 'windows':
        if architecture()[0].lower() == '64bit':
            return GECKO_WINDOWS_DRIVER_64
        else:
            return GECKO_WINDOWS_DRIVER_32
    elif s == 'darwin':
        return GECKO_MAC_DRIVER
    elif s == 'linux' or s == 'linux2':
        if architecture()[0].lower() == '64bit':
            return GECKO_LINUX_DRIVER_64
        else:
            return GECKO_LINUX_DRIVER_32
    else:
        print ('Your OS version "' + s + '" is not supported')
        return ''
