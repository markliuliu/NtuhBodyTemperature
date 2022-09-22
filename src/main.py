import time

import yaml
import pytz
from yaml import BaseLoader as Loader
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import date, datetime, timezone

import DriverFactory

TIME_ZONE = pytz.timezone('Asia/Taipei')
FILL_FORM_XPATH = '//*[contains(text(), "再次填寫症狀問卷")]'
FLOOR_XPATH = '//*[@id="duty-tr"]/td[3]/span/div/div[1]/label'
FEVER_XPATH = '//*[@id="fever-tr"]/td[3]/span/div/div[2]/label'
SYMPTOMS_XPATH = '//*[@id="symptoms-tr"]/td[3]/span/div/div[2]/label'
SUBMIT_BUTTON_XPATH = '//*[@id="questiontable"]/tbody/tr[14]/td/table/tbody/tr/td/button'


def load_settings():
    with open("../resource/settings.yaml") as stream:
        _settings = yaml.load(stream, Loader)
    return _settings


def main():
    now = datetime.now(TIME_ZONE)  # UTC time
    print("{} - start to fill the form of body temperature".format(now.strftime("%Y-%m-%d %H:%M:%S")))
    base_url = SETTINGS["base_url"]
    queues = SETTINGS["queue"]
    driver = DriverFactory.get_chrome_driver()
    wait = WebDriverWait(driver, 10)
    for queue in queues:
        driver.get(base_url+queue)
        if not already_fill_the_from(driver):
            goes_to_the_form(driver)
            fill_form(wait)
        else:
            print("already fill the form today for queue")
    driver.close()
    return


def already_fill_the_from(driver):
    # TODO: need to check all the form we already submit
    element = driver.find_element(By.CLASS_NAME, "bDiv")
    today = datetime.now(TIME_ZONE)
    return today.strftime("%Y-%m-%d") in element.text


def goes_to_the_form(driver):
    element = driver.find_element(By.XPATH, FILL_FORM_XPATH)
    element.click()


def fill_form(wait):
    wait.until(EC.element_to_be_clickable((By.XPATH, FLOOR_XPATH))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, FEVER_XPATH))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, SYMPTOMS_XPATH))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, SUBMIT_BUTTON_XPATH))).click()
    print("fill and submit the form successfully")


if __name__ == '__main__':
    SETTINGS = load_settings()
    main()

