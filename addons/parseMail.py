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
import time


def shit(driver):
    time.sleep(3)
    #nastroit
    try:
        driver.find_element_by_css_selector('.sc-bdVaJa').click()
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
    #avatar
    try:
        driver.find_element_by_css_selector('.close-0-2-10').click()
    except:
        pass


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
    time.sleep(6)
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


def delContent(driver):
    driver.get('https://e.mail.ru/inbox/')
    try:
        driver.find_element_by_css_selector('.b-checkbox_transparent > div:nth-child(1)')
        pochtaIsNew = 0
    except :
        pochtaIsNew = 1
    wait = WebDriverWait(driver, 1800)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#PH_logoutLink')))
    if pochtaIsNew == 1:
        shit(driver)
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.button2__explanation'))).click()
        shit(driver)
        wait.until(ec.element_to_be_clickable(
            (By.CSS_SELECTOR, '.button2_delete > span:nth-child(1) > span:nth-child(2)'))).click()
        shit(driver)
        wait.until(ec.element_to_be_clickable(
            (By.CSS_SELECTOR, '.button2_primary > span:nth-child(1) > span:nth-child(1)'))).click()
        shit(driver)
    else:
        shit(driver)
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.b-checkbox_transparent > div:nth-child(1)'))).click()
        shit(driver)
        wait.until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, '.b-toolbar__btn_grouped_first > span:nth-child(2)'))).click()
        shit(driver)


def findSteamCode(driver, TIME):
    wait = WebDriverWait(driver, 1800)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#PH_logoutLink')))
    steamCodeString = '/html/body/div[5]/div/div[1]/div[1]/div/div[2]/span/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div/div/div/div/div/div/center[1]/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table[3]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td'
    steamCodeStringOld = '/html/body/div[2]/div/div[5]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[6]/div[2]/div[2]/div[10]/div/div/div/div[4]/div/div[2]/div/div/div/div/center[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table[3]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td'
    driver.get('https://e.mail.ru/inbox/')
    shit(driver)
    pochtaIsNew = 0
    try:
        driver.find_element_by_css_selector('.b-checkbox_transparent > div:nth-child(1)')
    except NoSuchElementException:
        pochtaIsNew = 1
    if pochtaIsNew == 0:
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#PH_logoutLink')))
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".portal-octavius-widget__button"))).click()
        wait.until(ec.element_to_be_clickable(
            (By.XPATH, "//div[@id='tooltip-octavius']/div/div/div/form/div[2]/div[2]/button/span"))).click()
    steam(wait, driver, TIME)
    time.sleep(0.5)
    cont = wait.until(ec.element_to_be_clickable((By.XPATH, steamCodeString))).text
    return cont


def findSteamCodeGuard(driver, TIME):
    wait = WebDriverWait(driver, 1800)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#PH_logoutLink')))
    steamCodeString = '/html/body/div[5]/div/div[1]/div[1]/div/div[2]/span/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div/div/div/div/div/div/center[1]/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table[3]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td'
    driver.get('https://e.mail.ru/inbox/')
    shit(driver)
    pochtaIsNew = 0
    try:
        driver.find_element_by_css_selector('.b-checkbox_transparent > div:nth-child(1)')

    except NoSuchElementException:
        pochtaIsNew = 1
    if pochtaIsNew == 0:
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#PH_logoutLink')))
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".portal-octavius-widget__button"))).click()
        wait.until(ec.element_to_be_clickable(
            (By.XPATH, "//div[@id='tooltip-octavius']/div/div/div/form/div[2]/div[2]/button/span"))).click()
    steam(wait, driver, TIME)
    time.sleep(0.5)
    cont = wait.until(ec.element_to_be_clickable((By.XPATH, steamCodeString))).text
    return cont


def getLockLink(driver):
    TIME = datetime.now() - timedelta(0, 60)
    TIME = TIME.strftime("%H:%M")
    wait = WebDriverWait(driver, 1800)
    steam(wait, driver, TIME)
    return  wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,
    '.p-80_mr_css_attr > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(5) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(4)'))).get_attribute('href')
