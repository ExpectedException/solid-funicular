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
from datetime import datetime, time
from time import sleep




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


def act(x):
    return x+10


def wait_start(runTime, action):
    startTime = time(*(map(int, runTime.split(':'))))
    while startTime > datetime.today().time(): # you can add here any additional variable to break loop if necessary
        sleep(10)# you can change 1 sec interval to any other
    return action


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

login = 'kogevnikov_i'
password = 'Cfyzghjdthztnfrrfeynsbcnfdbngk.cs!225'


def posetil(wait, driver, tvar):
    wait.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Посещаемость')))
    try:
        driver.execute_script("""
        var xpath = "//a[text()='Отправить посещаемость']";
        var matchingElement = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        if (matchingElement !== null) {
        matchingElement.scrollIntoView();
        }""")
        driver.find_element_by_link_text('Отправить посещаемость').click()
    except NoSuchElementException:
        sleep(0)
    wait.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Посещаемость')))
    try:
        driver.find_element_by_css_selector('.fgrouplabel > label')
        driver.execute_script("""
                            var xpath = "//a[text()='Присутствовал']";
                            var matchingElement = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                            if (matchingElement !== null) {
                            matchingElement.checked = true;
                            }""")
    except NoSuchElementException:
        sleep(0)
        tvar = 1
    if tvar != 1:
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.fgrouplabel')))
        try:
            sleep(5)
            driver.execute_script("""
                    var xpath = "//a[text()='Сохранить']";
                    var matchingElement = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                    if (matchingElement !== null) {
                    matchingElement.click();
                    }""")
        except NoSuchElementException:
            sleep(0)


def main():
    options = Options()
    options.headless = True
    binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    #profile = FirefoxProfile("C:\\Users\\USER\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\8its4eb6.default")
    profile = FirefoxProfile("C:\\Users\\PussyDestroyer\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\7dvs7u3f.default")
    driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary)
    wait = WebDriverWait(driver, 600)
    tvar = 0
    driver.delete_all_cookies()
    driver.get('https://testmoodle.sevsu.ru/login/index.php')
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#username'))).send_keys(login)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#password'))).send_keys(password)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#loginbtn'))).click()
    driver.get('https://testmoodle.sevsu.ru/mod/attendance/view.php?id=18646&view=5')  #ПВС
    posetil(wait, driver, tvar)
    driver.get('https://testmoodle.sevsu.ru/mod/attendance/view.php?id=7812&view=5')  #агентное моделирование
    posetil(wait, driver, tvar)
    driver.get('https://testmoodle.sevsu.ru/mod/attendance/view.php?id=18405&view=5')  #Вычислительные системы
    posetil(wait, driver, tvar)
    driver.get('https://testmoodle.sevsu.ru/mod/attendance/view.php?id=70612&view=5')  #Основы теории экспертных систем
    posetil(wait, driver, tvar)
    driver.get('https://testmoodle.sevsu.ru/mod/attendance/view.php?id=71790&view=5')  # оср
    posetil(wait, driver, tvar)
    driver.get('https://testmoodle.sevsu.ru/mod/attendance/view.php?id=18421&view=5')  # Проектирование микропроцессорных и компьютерных систем
    posetil(wait, driver, tvar)
    driver.get('https://testmoodle.sevsu.ru/mod/attendance/view.php?id=18389&view=5')  # Сети и телекоммуникации
    driver.close()


if __name__ == '__main__':
    main()

