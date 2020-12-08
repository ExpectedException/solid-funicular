from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import string
from random import *
import json
from nickname_generator import generate
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from threading import Thread
from selenium.common.exceptions import TimeoutException
from datetime import datetime


def passgen(x):
    characters = string.ascii_letters + string.digits
    password = "".join(choice(characters) for x in range(randint(14, 16)))
    return password


def sav(Email, Passwd):
    f = open("data_done100percent.txt", "a")
    data = str(Email + ' ' + Passwd + '' + '\n')
    f.write(data)
    f.close()


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


def DriverDie(driver):
    try:
        driver.close()
    except:
        pass


def checkCaptchaControl(driver):
    wait = WebDriverWait(driver, 0.2)
    GoNext = 0
    while GoNext == 0:
        try:
            # numReqWhileCaptcha
            wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[3]/div/div/div/form/div[3]/p')))
            DriverDie(driver)
        except TimeoutException:
            pass
        try:
            wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.c2182')))
            return 1
        except TimeoutException:
            pass


def numberReq(driver):
    wait = WebDriverWait(driver, 0.2)
    GoNext = 0
    while GoNext == 0:
        try:
            #numReq
            wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'small.c0128:nth-child(1)')))
            DriverDie(driver)
        except TimeoutException:
            pass
        try:
            #nastroit
            wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.c2182')))
            GoNext = checkCaptchaControl(driver)
        except TimeoutException:
            pass
        try:
            #ok captcha
            wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.c011382')))
            GoNext = checkCaptchaControl(driver)
        except TimeoutException:
            pass
        try:
            #numReqWhileCaptcha
            wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[3]/div/div/div/form/div[3]/p')))
            DriverDie(driver)
        except TimeoutException:
            pass


def degenerate_ru():
    accname =(generate() + generate() + str(randint(100, 9000)))
    Email =(accname + "@mail.ru")
    Passwd= passgen(randint(1, 23243400))
    return accname, Email, Passwd


def degenerate_ua():
    accname =(generate() + generate() + str(randint(100, 9000)))
    Email =(accname + "@mail.ua")
    Passwd= passgen(randint(1, 23243400))
    return accname, Email, Passwd


def main(accname, Email, Passwd):
    f = open("data.txt", "a")
    data = str(Email + ' ' + Passwd + '' + '\n')
    f.write(data)
    f.close()
    print(Email)
    print(Passwd)
    options = Options()
    options.headless = True
    binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    #profile = FirefoxProfile("C:\\Users\\PussyDestroyer\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\7dvs7u3f.default")
    profile = FirefoxProfile("C:\\Users\\qweqweqwe\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\bmiwtt76.default")
    driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary)
    wait = WebDriverWait(driver, 1800)
    # retoggleAllTheAddons(driver)
    driver.delete_all_cookies()
    driver.get('https://account.mail.ru/signup?from=navi&lang=ru_RU')
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#fname'))).send_keys('qwe')
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#lname'))).send_keys('qwe')
    wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[3]/div/div/div/form/div[5]/div[2]/div/div[1]/div/div/div/div/div[1]/span'))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, '//div/div/div[2]/div/div/div/div/div/div/div'))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[3]/div/div/div/form/div[5]/div[2]/div/div[3]/div/div/div/div[1]'))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, '//div/div/div/div/div[2]/span'))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[3]/div/div/div/form/div[5]/div[2]/div/div[5]/div/div/div/div'))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, '//div/div/div/div/div[2]/span'))).click()
    driver.find_element_by_xpath("//*[contains(text(), 'Мужской')]").click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#aaa__input'))).send_keys(accname)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#password'))).send_keys('Lol123456qwe')
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#repeatPassword'))).send_keys('Lol123456qwe')
    #wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#phone-number__phone-input'))).send_keys('9789601886') #1
    #wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#phone-number__phone-input'))).send_keys('9787393986') #2
    time.sleep(0.5)
    wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div[3]/div/div/div/form/button'))).click()
    numberReq(driver)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#PH_logoutLink')))
    driver.get('https://id.mail.ru/security')
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.innerText-0-2-85'))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/form/div[5]/div[2]/div/div/input'))).send_keys('Lol123456qwe')
    wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/form/div[8]/div[2]/div[1]/div/div/div/input'))).send_keys(Passwd)
    wait.until(ec.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/form/div[12]/div[2]/div/div/input'))).send_keys(
        Passwd)
    wait.until(ec.element_to_be_clickable(
        (By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/form/button[1]/span'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.cross-0-2-97.mobileCross-0-2-104'))).click()
    sav(Email, Passwd)
    #wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'button.base-0-2-77:nth-child(1) > div:nth-child(1) > svg:nth-child(1)'))).click()
    #wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/form/div[4]/button[1]/span'))).click()
    #wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/button/span'))).click()
    DriverDie(driver)


if __name__ == '__main__':
    f = open("data_done100percent.txt", "a")
    data = str(datetime.now()) + '\n'
    f.write(data)
    f.close()
    threads = []
    for n in range(10):
        time.sleep(0.1)
        t = Thread(target=main, args=degenerate_ua())
        time.sleep(0.1)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
