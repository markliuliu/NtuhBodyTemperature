from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from sys import platform


def get_chrome_driver():
    if platform == "win32":
        options = Options()
        options.add_argument("--headless")
        options.add_experimental_option("detach", True)
        return webdriver.Chrome(executable_path="../resource/chromedriver.exe", chrome_options=options)
    else:
        return webdriver.Remote("http://selenium-standalone:4444/wd/hub", DesiredCapabilities.CHROME)
