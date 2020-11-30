from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import time, os, traceback
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.common.keys
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


def Convert(string, delim):
    li = list(string.split(delim))
    return li


def clickUntill(css, driver):
    wait = WebDriverWait(driver, 1800)
    cycle = 1
    while cycle == 1:
        time.sleep(0.15)
        try:
            wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, css))).click()
            cycle = 0
        except:
            traceback.print_exc()
            pass


def descr(supp, pRank, url):
    arr = Convert(supp, ']')
    txt = str(
        'MM Rank : ' + arr[2] + '\n' + 'Competitive Wins: ' + arr[1] + '\n' + 'Private Rank: '
        + pRank + '\n' + arr[3] + ' hours\n' + url + '\n' + '-----------------------------------------------\n\n'
        + "If you have any question just write us in G2G CHAT, we're online almost 24/7. All trades goes only through G2G.com!")
    return txt


def listCS(driver, game, url, numintable, supp, title, image, price):
    arr = Convert(supp, ']')
    rank = arr[2][0:4]
    tArr = Convert(title, '|')
    pRank = re.findall("\d+", tArr[1])[0]
    title = str(title + ' ' + numintable)
    if arr[0] == 'PRIME':
        prime = 'Yes'
    else:
        prime = 'No'
    wait = WebDriverWait(driver, 1800)
    description = descr(supp, pRank, url)
    clickUntill('#select2-service-container', driver)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.select2-search__field'))).send_keys('ACCOUNTS',
                                                                                                  Keys.ENTER)
    clickUntill('#select2-game-container', driver)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.select2-search__field'))).send_keys(game, Keys.ENTER)
    clickUntill('#select2-level_8-container', driver)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                           'body > span > span > span.select2-search.select2-search--dropdown > input'))).send_keys(
        prime, Keys.ENTER)
    clickUntill('#select2-level_9-container', driver)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                           'body > span > span > span.select2-search.select2-search--dropdown > input'))).send_keys(
        rank, Keys.ENTER)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                           'input#C2cProductsListing_products_title'))).send_keys(title)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                           'textarea#C2cProductsListing_products_description'))).send_keys(description)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.ext_listingimage_url'))).send_keys(image)
    clickUntill('.upload-img__action-btn > span:nth-child(2)', driver)
    clickUntill('.ext_listingimage_label', driver)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                           '#select2-C2cProductsListing_products_base_currency-container'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.select2-search__field'))).send_keys('USD', Keys.ENTER)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#C2cProductsListing_products_price'))).send_keys(price)
    clickUntill('#select2-C2cProductsListing_online_hr-container', driver)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.select2-search__field'))).send_keys('1', Keys.ENTER)
    clickUntill('.create__btn', driver)


def main(newLine, profile):
    arr = Convert(newLine, "	")
    url = arr[5]
    title = arr[6]
    numintable = arr[7]
    supp = arr[9]
    game = arr[12]
    image = arr[13]
    price = arr[14]
    # level = '1'
    # rank = 'Herald'
    # mmr = '100'
    # title = 'DOTA 2 XD'
    # description = 'this is description'
    # image = 'https://i.imgur.com/m3xBCTT.png'
    # price = '2.99'
    # game = 'Counter Strike'
    # prime = "Yes"
    # rank = 'Supreme'
    # title = 'CS TITLE'
    # description = 'this is description'
    print(datetime.now())
    options = Options()
    options.headless = True
    binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary)
    wait = WebDriverWait(driver, 1800)
    # retoggleAllTheAddons(driver)
    driver.get('https://www.g2g.com/sell/index')
    if game == 'Counter Strike':
        listCS(driver, game, url, numintable, supp, title, image, price)
    time.sleep(1)


if __name__ == '__main__':
    LOG_FILENAME = 'Loh.log'
    logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)
    ya = 1
    if ya == 1:
        frep = open('c!replace.txt', 'r')
        profile = FirefoxProfile(
            "C:\\Users\\PussyDestroyer\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\pir3gl70.g2gchecker")
    elif ya == 0:
        frep = open('c!replace.txt', 'r')
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
