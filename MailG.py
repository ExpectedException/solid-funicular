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


def passgen(x):
    characters = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(characters) for x in range(randint(14, 16)))
    return password


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


accname =(generate() + generate() + str(randint(100, 9000)))
accemail =(accname + "@mail.ru")
MyPass = passgen(randint(1, 200))


def main():
    print(accemail)
    print(MyPass)
    options = Options()
    options.headless = True
    binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    profile = FirefoxProfile("C:\\Users\\PussyDestroyer\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\7dvs7u3f.default")
    driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary)
    wait = WebDriverWait(driver, 600)
    retoggleAllTheAddons(driver)
    driver.delete_all_cookies()
    driver.get('https://account.mail.ru/signup?from=navi&lang=ru_RU')
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="firstname"]'))).send_keys('qwe')
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="lastname"]'))).send_keys('qwe')
    wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'b-date__day'))).click()
    wait.until(ec.element_to_be_clickable((By.LINK_TEXT, '1'))).click()
    wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'b-date__month'))).click()
    wait.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Январь'))).click()
    wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'b-date__year'))).click()
    wait.until(ec.element_to_be_clickable((By.LINK_TEXT, '2020'))).click()
    wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'b-radiogroup__input-wrapper'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.b-email__name [data-bem]'))).send_keys(accname)
    wait.until(ec.element_to_be_clickable((By.NAME, 'password'))).send_keys(MyPass)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'input#passwordRetry'))).send_keys(MyPass)
    #wait.until(ec.element_to_be_clickable((By.NAME, 'phone.phone'))).send_keys('9789601886') #1
    wait.until(ec.element_to_be_clickable((By.NAME, 'phone.phone'))).send_keys('9787393986') #2
    #wait.until(ec.element_to_be_clickable((By.NAME, 'phone.phone'))).send_keys('9785751897') #3
    #wait.until(ec.element_to_be_clickable((By.NAME, 'phone.phone'))).send_keys('9785813536') #4
    time.sleep(0.5)
    wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div[1]/div[3]/form/div[12]/div[1]/button'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.c0180'))).click()
    #wait.until(ec.element_to_be_clickable((By.ID, 'PH_user-email'))).click()
    #wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[1]/table/tbody/tr/td[2]/div[1]/table/tbody/tr/td[1]/div/div/div/div/div/div/div[4]/a[3]/span'))).click()
    window_before = driver.window_handles[0]
    driver.switch_to.window(window_before)
    driver.execute_script("window.open('https://account.mail.ru/security/recovery', 'new window')")
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    time.sleep(0.5)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'div:nth-of-type(5) > .RecoveryItem__base--34PyZ  .c0133'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.c01160'))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/button/span'))).click()
    driver.close()
    driver.switch_to.window(window_before)
    #wait.until(ec.element_to_be_clickable((By.ID, 'folderLink_0'))).click()
    driver.execute_script("window.open('https://store.steampowered.com/join/', 'new window')")
    driver.switch_to.window(driver.window_handles[1])
    wait.until(ec.element_to_be_clickable((By.ID, 'email'))).send_keys(accemail)
    wait.until(ec.element_to_be_clickable((By.ID, 'reenter_email'))).send_keys(accemail)
    wait.until(ec.element_to_be_clickable((By.ID, 'overAgeButton'))).click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@title="Steam <noreply@steampowered.com>"]')))
    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath('//*[@title="Steam <noreply@steampowered.com>"]'))
    wait.until(ec.element_to_be_clickable((By.LINK_TEXT, 'Создать аккаунт'))).click()
    #/html/body/div[6]/div/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/table/tbody/tr[2]/td/table/tbody/tr[4]/td/table/tbody/tr/td/a
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[2])
    wait.until(ec.element_to_be_clickable((By.ID, 'accountname'))).send_keys(accname)
    wait.until(ec.element_to_be_clickable((By.ID, 'password'))).send_keys(MyPass)
    wait.until(ec.element_to_be_clickable((By.ID, 'reenter_password'))).send_keys(MyPass)
    wait.until(ec.element_to_be_clickable((By.ID, 'createAccountButton'))).click()


main()
