from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import string
from random import *
import json
from nickname_generator import generate
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys





class AnyEc:
    """ Use with WebDriverWait to combine expected_conditions
        in an OR.
    """
    def __init__(self, *args):
        self.ecs = args

    def __call__(self, driver):
        for fn in self.ecs:
            try:
                if fn(driver): return True
            except:
                pass


def retoggleAllTheAddons(driver):
    driver.get("about:addons")
    driver.find_element_by_id("category-extension").click()
    driver.execute_script("""
        let hb = document.getElementById("html-view-browser");
        let al = hb.contentWindow.window.document.getElementsByTagName("addon-list")[0];
        let cards = al.getElementsByTagName("addon-card");
        for(let card of cards){
            card.addon.disable();
            card.addon.enable();
        }
    """)


def main():
    options = Options()
    options.headless = True
    binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    profile = FirefoxProfile("C:\\Users\\PussyDestroyer\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\7dvs7u3f.default")
    driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary)
    wait = WebDriverWait(driver, 600)
    #retoggleAllTheAddons(driver)
    driver.delete_all_cookies()
    driver.get('https://temp-mail.org/')
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a.logo')))
    tempm = driver.window_handles[0]
    driver.execute_script("window.open('https://detsad128.edusev.ru/')")
    detsad = driver.window_handles[1]
    for i in range (1, 9, 1):
        driver.switch_to.window(tempm)
        mail = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#click-to-copy'))).click()
        time.sleep(1)
        driver.switch_to.window(detsad)
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".auth_mail-input")))
        driver.execute_script("window.scrollTo(0, 400)")
        item = driver.find_element_by_css_selector('.auth_mail-input')
        item.clear()
        item.send_keys(Keys.CONTROL, 'v')
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "a[title='Подписаться'] > .material-icons"))).click()
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".subscriberesultsblock > div:nth-of-type(1)")))
        driver.switch_to.window(tempm)
        action = webdriver.ActionChains(driver)
        while True:
            try:
                driver.find_element_by_css_selector('li:nth-of-type(2) > div:nth-of-type(3) > .m-link-view > .link.viewLink > .arrow-link-ico')
                break
            except NoSuchElementException:
                action.move_by_offset(1, 1).perform()
                action.move_by_offset(-1, -1).perform()
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "li:nth-of-type(2) > div:nth-of-type(3) > .m-link-view > .link.viewLink > .arrow-link-ico"))).click()
        driver.execute_script("window.scrollTo(0, 200)")
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".inbox-data-content-intro > a"))).click()
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "a[title='Подписаться'] > .material-icons")))
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".auth_mail-input"))).clear()
        driver.get('https://temp-mail.org/')
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button#click-to-delete"))).click()
        driver.execute_script("window.scrollTo(0, 0)")
        print(i)


if __name__ == '__main__':
    main()
