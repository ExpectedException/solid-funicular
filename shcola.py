from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from datetime import datetime, time
from time import sleep
from threading import Thread
import logging


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


def Convert(stri):
    li = list(stri.split(":"))
    return li


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


def posetil(wait, driver, tvar, user):
    logging.info(user + ' ' + str(datetime.now())+' '+driver.title+" visited")
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
        wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@id='fgroup_id_statusarray']/fieldset/span/label/span")))
        logging.info(user + ' ' + str(datetime.now())+' '+driver.title+" checked")
    except NoSuchElementException:
        sleep(0)
        tvar = 1
    if tvar != 1:
        wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@id='id_status_375")))
        logging.info(user + ' ' + str(datetime.now())+' '+driver.title+" sent")

def main(login, password):
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
    posetil(wait, driver, tvar, login)
    driver.get('https://testmoodle.sevsu.ru/mod/attendance/view.php?id=7812&view=5')  #агентное моделирование
    posetil(wait, driver, tvar, login)
    driver.get('https://testmoodle.sevsu.ru/mod/attendance/view.php?id=18405&view=5')  #Вычислительные системы
    posetil(wait, driver, tvar, login)
    driver.get('https://testmoodle.sevsu.ru/mod/attendance/view.php?id=70612&view=5')  #Основы теории экспертных систем
    posetil(wait, driver, tvar, login)
    driver.get('https://testmoodle.sevsu.ru/mod/attendance/view.php?id=71790&view=5')  # оср
    posetil(wait, driver, tvar, login)
    driver.get('https://testmoodle.sevsu.ru/mod/attendance/view.php?id=18421&view=5')  # Проектирование микропроцессорных и компьютерных систем
    posetil(wait, driver, tvar, login)
    driver.get('https://testmoodle.sevsu.ru/mod/attendance/view.php?id=18389&view=5')  # Сети и телекоммуникации
    posetil(wait, driver, tvar, login)
    driver.close()


if __name__ == '__main__':
    LOG_FILENAME = 'WKOLA.log'
    logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)
    file = open("schol_DATA", "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()
    file1 = open('schol_DATA', 'r')
    Lines = file1.readlines()
    arr = []
    for line in Lines:
        tarr = Convert(line.strip())
        arr.append(tarr)
    threads = []
    for n in range(line_count):
        t = Thread(target=main, args=(arr[n][0], arr[n][1]))
        t.start()
        logging.info(t)
        threads.append(t)
    for t in threads:
        t.join()



