import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class TimeoutException(Exception):
    pass

def check_element_exists_by_xpath(driver, xpath):
    try:
        driver.find_element(by=By.XPATH, value=xpath)
    except NoSuchElementException:
        return False
    return True
    

def wait_for_element_by_xpath(driver, xpath, timeout=10):
    time_started = time.time()
    while not check_element_exists_by_xpath(driver, xpath):
        if time_started + timeout >= time_started:
            raise TimeoutException(f"Timeout {timeout}s passed")
        time.sleep(0.1)
    return driver.find_element(by=By.XPATH, value=xpath)