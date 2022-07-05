import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from configuration.config import TestData
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import softest



class BasePg():
    """This is base page constructor which will be parent of all pages constructor"""
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, TestData.WAIT)

    """This method will look for the title provided and will return current title"""
    def get_title(self, title:str):
        self.wait.until(EC.title_is(title))
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    """This method will check if the element is visible to perform certain 
    task/action on it and will return boolean value"""
    def ele_visible(self, by_locator):
        element = self.driver.find_element(*by_locator)
        return element.is_displayed()

    """This method will keep on scrolling the page until its is loaded completely"""
    def page_scroll(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:  # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Wait to load page
            time.sleep(5)
            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break

            last_height = new_height
        time.sleep(5)

    """This method will wait for the list of elements we provide and return the list"""
    def wait_until_all_elements_present(self, by_locator):
        list_of_elements = self.wait.until(EC.presence_of_all_elements_located(by_locator))
        return list_of_elements

    def wait_until_an_element_present(self, by_locator):
        element = self.wait.until(EC.presence_of_element_located(by_locator))
        if element == "":
            self.driver.refresh()
            element = self.wait.until(EC.presence_of_element_located(by_locator))
        return element


    """This method will wait for an element until it is enabled to click"""
    def wait_until_an_element_clickable(self, by_locator):
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        if element == "":
            self.driver.refresh()
            element = self.wait.until(EC.element_to_be_clickable(by_locator))
        return element

    """This method will perform click action on the element given"""
    def do_click(self, by_locator):
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        if element == "":
            self.driver.refresh()
            element = self.wait.until(EC.element_to_be_clickable(by_locator))
        element.click()

    """This method will check if the text box is enable to send keys and return boolean value"""
    def is_text_box_enable(self, by_locator):
        value = self.wait.until(EC.presence_of_element_located(by_locator))
        return value.is_enabled()

    """This method will send keys at the location provided"""
    def do_send_Keys(self, by_locator, text):
        self.wait.until(EC.presence_of_element_located(by_locator)).send_keys(text)

    """This method will return the text value of the element provided"""
    def get_element_text(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located((by_locator)))
        if element == "":
            element = self.wait.until(EC.visibility_of_element_located((by_locator)))
        return element.text

    """This method will scroll the page up/down as provided while calling"""
    def web_scroll(self, direction="up"):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -5000);")

        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 3000);")

    def sleep_time(self):
        return time.sleep(TestData.SLEEP_TIME)

    def move_to_element_using_mouse_hover(self, move_to):
        action = ActionChains(self.driver)
        action.move_to_element(move_to).pause(1).perform()

    def element_displayed(self, element):
        value = self.driver.find_element(element)
        return value.is_displayed()

    def press_enter_key(self, by_locator):
        self.driver.find_element(*by_locator).send_keys(Keys.ENTER)










