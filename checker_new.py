from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import time
import datetime
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


def Convert(string):
    li = list(string.split(":"))
    return li


steamCodeString = '/html/body/div[5]/div/div[1]/div[1]/div/div[2]/span/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div/div/div/div/div/div/center[1]/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table[3]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td'
steamCodeStringOld = '/html/body/div[2]/div/div[5]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[6]/div[2]/div[2]/div[10]/div/div/div/div[4]/div/div[2]/div/div/div/div/center[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table[3]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td'


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
    except NoSuchElementException:
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


def passgen(x):
    characters = string.ascii_letters + string.digits
    password = "".join(choice(characters) for x in range(randint(10, 12)))
    return password


def LetsDeleteEverything(driver, url):
    CommentsShouldDie(driver, url)
    LeaveGroups(driver, url)
    PengingInvites(driver, url)
    Following(driver, url)
    Blocked(driver, url)
    PengingFriends(driver, url)
    FuckFriends(driver, url)
    ChatShit(driver)


def jSonParse(driver, wait):
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#global_actions > a')))
    jsnstr = driver.find_element_by_id('webui_config').get_attribute('data-userinfo')
    y = json.loads(jsnstr)
    url = str('https://steamcommunity.com/profiles/' + y['steamid'] + '/')
    return url


def CommentsShouldDie(driver, url):
    wait = WebDriverWait(driver, 5)
    driver.get(url)
    GoNext = 0
    wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[7]/div[3]/div[1]/div[2]/div/div[2]/div[4]/div/div[1]/div[2]/span[1]')))
    while GoNext == 0:
        try:
            wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'commentthread_comment_content')))
            id = driver.execute_script("return document.querySelector('.commentthread_comment_text').id")
            idNumbers = re.findall("\d+", id)[0]
            urlNumbers = re.findall("\d+", url)[0]
            DELETE = str('javascript:CCommentThread.DeleteComment( "Profile_' + urlNumbers + '", "' + idNumbers + '"  );')
            driver.execute_script(DELETE)
            time.sleep(1)
        except TimeoutException:
            GoNext = 1


def ChatShit(driver):
    #will fix
    GoNext = 0
    wait = WebDriverWait(driver, 10)
    driver.get('https://steamcommunity.com/chat/')
    while GoNext == 0:
        try:
            wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'ContextMenuButton')))
            time.sleep(0.5)
            el = driver.find_element_by_class_name('chatRoomListContainer')
            el.find_element_by_class_name('ContextMenuButton').click()
            wait.until(ec.element_to_be_clickable((By.XPATH, "//body/div[5]/div/div/div[2]"))).click()
            wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
        except :
            GoNext = 1
    DeclineChat(driver)


def DeclineChat(driver):
    action = ActionChains(driver)
    cyka = "//div[@id='friendslist-container']/div/div[3]/div/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div/div"
    cyka2 ="//div[@id='friendslist-container']/div/div[3]/div/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div[2]/div"
    cyka3 = "//div[@id='friendslist-container']/div/div[3]/div/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div[3]/div"
    cyka4 = "//div[@id='friendslist-container']/div/div[3]/div/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div[4]/div"
    cyka5 = "//div[@id='friendslist-container']/div/div[3]/div/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div[5]/div"
    cyka6 = "//div[@id='friendslist-container']/div/div[3]/div/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div[6]/div"
    cyka7 = "//div[@id='friendslist-container']/div/div[3]/div/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div[7]/div"
    cyka8 = "//div[@id='friendslist-container']/div/div[3]/div/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div[8]/div"
    cyka9 = "//div[@id='friendslist-container']/div/div[3]/div/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div[9]/div"
    cyka10 = "//div[@id='friendslist-container']/div/div[3]/div/div/div[2]/div[3]/div/div/div/div[2]/div/div/div[2]/div[10]/div"
    GoNext = 0
    wait = WebDriverWait(driver, 10)
    while GoNext == 0:
        try:
            wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'ContextMenuButton')))
            el = wait.until(ec.element_to_be_clickable((By.XPATH, cyka)))
            action.double_click(el).perform()
            el = wait.until(ec.element_to_be_clickable((By.XPATH, cyka2)))
            action.double_click(el).perform()
            el = wait.until(ec.element_to_be_clickable((By.XPATH, cyka3)))
            action.double_click(el).perform()
            el = wait.until(ec.element_to_be_clickable((By.XPATH, cyka4)))
            action.double_click(el).perform()
            el = wait.until(ec.element_to_be_clickable((By.XPATH, cyka5)))
            action.double_click(el).perform()
            el = wait.until(ec.element_to_be_clickable((By.XPATH, cyka6)))
            action.double_click(el).perform()
            el = wait.until(ec.element_to_be_clickable((By.XPATH, cyka7)))
            action.double_click(el).perform()
            el = wait.until(ec.element_to_be_clickable((By.XPATH, cyka8)))
            action.double_click(el).perform()
            el = wait.until(ec.element_to_be_clickable((By.XPATH, cyka9)))
            action.double_click(el).perform()
            el = wait.until(ec.element_to_be_clickable((By.XPATH, cyka10)))
            action.double_click(el).perform()
        except TimeoutException:
            GoNext = 1


def FuckFriends(driver, url):
    wait = WebDriverWait(driver, 5)
    groups_url = str(url + 'friends')
    driver.get(groups_url)
    try:
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#search_results_empty')))
        GoNext = 1
    except TimeoutException:
        GoNext = 0
    if GoNext == 0:
        try:
            wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[7]/div[3]/div/div[2]/div[2]/div/div[1]/button[1]/span'))).click()
            wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'span.selection_type:nth-child(2)'))).click()
            wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.manage_action > span:nth-child(1)'))).click()
        except TimeoutException:
            pass


def LeaveGroups(driver, url):
    wait = WebDriverWait(driver, 5)
    groups_url = str(url + 'groups/')
    driver.get(groups_url)
    try:
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#search_results_empty')))
        GoNext = 1
    except TimeoutException:
        GoNext = 0
    while GoNext == 0:
        try:
            elems = driver.find_elements_by_class_name('actions')
            for i in elems:
                try:
                    time.sleep(0.1)
                    i.click()
                except:
                    pass
            wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.btn_green_steamui'))).click()
        except TimeoutException:
            GoNext = 1


def PengingInvites(driver, url):
    wait = WebDriverWait(driver, 5)
    groups_url = str(url + 'groups/pending')
    driver.get(groups_url)
    ignore = []
    try:
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#search_results_empty')))
        GoNext = 1
    except TimeoutException:
        GoNext = 0
    while GoNext == 0:
        try:
            lnks = driver.find_elements_by_tag_name('a')
            for lnk in lnks:
                tmp_href = lnk.get_attribute('href')
                tmp_href = urllib.parse.unquote(tmp_href)
                if tmp_href.find("group_ignore") != -1:
                    ignore.append(tmp_href)
            for i in ignore:
                try:
                    time.sleep(0.1)
                    driver.execute_script(i)
                except:
                    pass
            wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#search_results_empty')))
        except TimeoutException:
            GoNext = 1


def Following(driver, url):
    wait = WebDriverWait(driver, 5)
    groups_url = str(url + 'following/')
    driver.get(groups_url)
    try:
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#search_results_empty')))
        GoNext = 1
    except TimeoutException:
        GoNext = 0
    if GoNext == 0:
        try:
            wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[7]/div[3]/div/div[2]/div[2]/div/div[1]/button/span'))).click()
            wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'span.selection_type:nth-child(2)'))).click()
            wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.manage_action > span:nth-child(1)'))).click()
        except TimeoutException:
            pass


def Blocked(driver, url):
    wait = WebDriverWait(driver, 5)
    groups_url = str(url + 'friends/blocked')
    driver.get(groups_url)
    try:
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#search_results_empty')))
        GoNext = 1
    except TimeoutException:
        GoNext = 0
    if GoNext == 0:
        try:
            wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[7]/div[3]/div/div[2]/div[2]/div/div[1]/button/span'))).click()
            wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'span.selection_type:nth-child(2)'))).click()
            wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.manage_action > span:nth-child(1)'))).click()
        except TimeoutException:
            pass


def PengingFriends(driver, url):
    wait = WebDriverWait(driver, 5)
    groups_url = str(url + 'friends/pending')
    driver.get(groups_url)
    try:
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#search_results_empty')))
        GoNext = 0.5
    except TimeoutException:
        GoNext = 0
    try:
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#search_results_sentinvites_empty')))
        Gpls = 1
        GoNext = 0.5
    except TimeoutException:
        Gpls = 0
        GoNext = 0
    if GoNext != 1:
        try:
            wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#manage_friends_control > span:nth-child(1)'))).click()
        except TimeoutException:
            pass
        while Gpls == 0:
            try:
                elems = driver.find_elements_by_class_name('actions')
                for i in elems:
                    try:
                        i.click()
                        time.sleep(0.1)
                    except:
                        pass
                wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.btn_green_steamui > span:nth-child(1)'))).click()
            except TimeoutException:
                Gpls = 1


def findSteamCode(driver, wait):
    driver.get('https://e.mail.ru/inbox/')
    pochtaIsNew = 0
    steam(wait)
    try:
        driver.find_element_by_css_selector('.b-checkbox_transparent > div:nth-child(1)')

    except NoSuchElementException:
        pochtaIsNew = 1

    print(pochtaIsNew)
    steam(wait)
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();",
                          driver.find_element_by_xpath('//*[@title="Steam Support <noreply@steampowered.com>"]'))
    if pochtaIsNew == 1:
        cont = wait.until(ec.element_to_be_clickable((By.XPATH, steamCodeString))).text
    else:
        cont = wait.until(ec.element_to_be_clickable((By.XPATH, steamCodeStringOld))).text
    return cont


def findSteamCodeGuard(driver, wait):
    driver.get('https://e.mail.ru/inbox/')
    shit(driver)
    steamCode = '/html/body/div[5]/div/div[1]/div[1]/div/div[2]/span/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div/div/div/div/div/div/center[1]/div/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table[3]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td'
    time.sleep(5)
    pochtaIsNew = 0
    steam(wait)
    try:
        driver.find_element_by_css_selector('.b-checkbox_transparent > div:nth-child(1)')

    except NoSuchElementException:
        pochtaIsNew = 1

    print(pochtaIsNew)
    steam(wait)
    time.sleep(0.5)
    shit(driver)
    driver.execute_script("arguments[0].click();",
                          driver.find_element_by_xpath('//*[@title="Steam Support <noreply@steampowered.com>"]'))
    if pochtaIsNew == 1:
        cont = wait.until(ec.element_to_be_clickable((By.XPATH, steamCode))).text
    else:
        cont = wait.until(ec.element_to_be_clickable((By.XPATH, steamCode))).text
    return cont


def changeEmail(driver, wait):
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


def steam(wait):
    wait.until(AnyEc(
        ec.presence_of_element_located(
            (By.XPATH, '//*[@title="Steam Support <noreply@steampowered.com>"]')),
        ec.presence_of_element_located(
            (By.XPATH, '//*[@title="Поддержка Steam <noreply@steampowered.com>"]'))))


def shit(driver):
    wTime = 0.3
    time.sleep(wTime)
    try:
        time.sleep(wTime)
        driver.find_element_by_css_selector('.c2182').click()
    except NoSuchElementException:
        pass

    try:
        time.sleep(wTime)
        driver.find_element_by_css_selector('.c01180').click()

    except NoSuchElementException:
        pass

    try:
        time.sleep(wTime)
        driver.find_element_by_css_selector('.c01159').click()

    except NoSuchElementException:
        pass

    try:
        time.sleep(wTime)
        driver.find_element_by_css_selector('.c01156').click()

    except NoSuchElementException:
        pass

    try:
        time.sleep(wTime)
        driver.find_element_by_css_selector('.c01177').click()

    except NoSuchElementException:
        pass

    try:
        time.sleep(wTime)
        driver.find_element_by_css_selector('.cross-0-2-70 > svg:nth-child(1)').click()

    except NoSuchElementException:
        pass

    try:
        time.sleep(wTime)
        driver.find_element_by_css_selector('.cross-0-2-23 > svg:nth-child(1) > path:nth-child(1)').click()

    except NoSuchElementException:
        pass

    try:
        time.sleep(wTime)
        driver.find_element_by_css_selector('.c2117 > svg:nth-child(1)').click()

    except NoSuchElementException:
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


def main(newLine, profile):
    arr = Convert(newLine)
    EmailNew = arr[0]
    EmailNewPass = arr[1]
    Steam = arr[2]
    SteamPass = arr[3]
    EmailOld = arr[4]
    EmailOldPass = arr[5]
    print(datetime.now())
    print(EmailOld)
    print(EmailOldPass)
    options = Options()
    options.headless = True
    binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    driver = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary)
    wait = WebDriverWait(driver, 1800)
    # retoggleAllTheAddons(driver)
    driver.delete_all_cookies()
    driver.get('https://mail.ru/')
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#mailbox\:login-input'))).send_keys(EmailOld)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#mailbox\:submit-button'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#mailbox\:password-input'))).send_keys(EmailOldPass)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#mailbox\:submit-button'))).click()
    window_before = driver.window_handles[0]
    driver.switch_to.window(window_before)
    driver.execute_script("window.open('https://store.steampowered.com/login/', 'new window')")
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="input_username"]'))).send_keys(Steam)
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="input_password"]'))).send_keys(SteamPass)
    loginIntoSteam(driver, wait, EmailNew, EmailNewPass, EmailOld, EmailOldPass)
    url = jSonParse(driver, wait)
    #testingPlace
    print(url)
    driver.get('https://store.steampowered.com/account/')
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                           'div.account_setting_block:nth-child(6) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > a:nth-child(1)'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                           'html.responsive body.v6.responsive_page div.responsive_page_frame.with_header div.responsive_page_content div.responsive_page_template_content div.page_body_ctn div#page_content.page_content.page_loaded div#wizard_contents div.wizard_content_wrapper a.help_wizard_button.help_wizard_arrow_right'))).click()
    driver.switch_to.window(driver.window_handles[0])
    try:
        driver.find_element_by_css_selector('a.btn > span: nth - child(1)')
        steam(wait)

    except NoSuchElementException:
        steam(wait)
    driver.get('https://id.mail.ru/security')
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.base-0-2-82'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                           'div.field-0-2-146:nth-child(7) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)'))).send_keys(
        EmailOldPass)
    EmailPassNew = passgen(randint(1, 200))
    # print('new email pass')
    print(EmailPassNew)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                           '.tooltip-0-2-167 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)'))).send_keys(
        EmailPassNew)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                           'div.field-0-2-146:nth-child(14) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)'))).send_keys(
        EmailPassNew)
    wait.until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, 'button.base-0-2-82:nth-child(20) > span:nth-child(1)'))).click()
    wait.until(
        ec.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/button/span'))).click()
    logging.info(
        str(datetime.now()) + ' changed ' + EmailOld + ':' + EmailOldPass + ' TO ' + EmailOld + ':' + EmailPassNew)
    print(EmailOld + ':' + EmailPassNew)
    driver.get('https://e.mail.ru/inbox/')
    shit(driver)
    pochtaIsNew = 0
    shit(driver)
    steam(wait)
    try:
        driver.find_element_by_css_selector('.b-checkbox_transparent > div:nth-child(1)')

    except NoSuchElementException:
        pochtaIsNew = 1

    print(pochtaIsNew)
    shit(driver)
    steam(wait)
    shit(driver)
    driver.execute_script("arguments[0].click();",
                          driver.find_element_by_xpath('//*[@title="Steam Support <noreply@steampowered.com>"]'))
    if pochtaIsNew == 1:
        cont = wait.until(ec.element_to_be_clickable((By.XPATH, steamCodeString))).text
    else:
        cont = wait.until(ec.element_to_be_clickable((By.XPATH, steamCodeStringOld))).text
    # if pochtaIsNew == 1:
    #   cont = wait.until(ec.element_to_be_clickable((By.XPATH,
    #                                                  '/html/body/div[5]/div/div[1]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div/div/div/table/tbody/tr[2]/td/table/tbody/tr[3]/td/div/span'))).text
    # else:
    #    cont = wait.until(ec.element_to_be_clickable((By.XPATH,
    #                                                  '/html/body/div[2]/div/div[5]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[6]/div[2]/div[2]/div[10]/div/div/div/div[4]/div/div[2]/div/div/div/div/table/tbody/tr[2]/td/table/tbody/tr[3]/td/div/span'))).text

    driver.get('https://e.mail.ru/inbox/')
    shit(driver)
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

    driver.switch_to.window(driver.window_handles[1])
    SteamPassNew = passgen(randint(1, 200))
    print(SteamPassNew)
    f = open("checker.txt", "a")
    data = str(
        EmailNew + ' ' + EmailNewPass + ' ' + Steam + ' ' + SteamPassNew + '  ' + url + '     ' + EmailOld + ' ' + EmailPassNew + '\n')
    logging.info(str(datetime.now()) + ' ' + data)
    f.write(data)
    f.close()
    print(EmailNew + ':' + EmailNewPass + ':' + Steam + ':' + SteamPassNew + ':' + EmailOld + ':' + EmailPassNew)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#forgot_login_code'))).send_keys(cont)
    wait.until(ec.element_to_be_clickable(
        (By.XPATH, '/html/body/div/div[7]/div[2]/div[2]/div/div[2]/div/div[4]/form/div[3]/input'))).click()
    wait.until(ec.element_to_be_clickable((By.ID, 'password_reset'))).send_keys(SteamPassNew)
    wait.until(ec.element_to_be_clickable((By.ID, 'password_reset_confirm'))).send_keys(SteamPassNew)
    time.sleep(5)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.account_recovery_submit > input:nth-child(1)'))).click()
    logging.info(
        str(datetime.now()) + ' changed ' + Steam + ':' + SteamPass + ' TO ' + Steam + ':' + SteamPassNew)
    driver.switch_to.window(driver.window_handles[0])
    steam(wait)
    shit(driver)
    driver.execute_script("arguments[0].click();",
                          driver.find_element_by_xpath('//*[@title="Steam Support <noreply@steampowered.com>"]'))
    linkTlock = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.p-80_mr_css_attr > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(5) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > a:nth-child(4)'))).get_attribute('href')
    logging.info(
        str(datetime.now()) + ' got lock link ' + Steam + ":" + linkTlock)
    print(Steam + ":" + linkTlock)
    driver.get('https://e.mail.ru/inbox/')
    if pochtaIsNew == 1:
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.button2__explanation'))).click()
        shit(driver)
        wait.until(ec.element_to_be_clickable(
            (By.CSS_SELECTOR, '.button2_delete > span:nth-child(1) > span:nth-child(2)'))).click()
        shit(driver)
        wait.until(ec.element_to_be_clickable(
            (By.CSS_SELECTOR, '.button2_primary > span:nth-child(1) > span:nth-child(1)'))).click()
        shit(driver)
    else:
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.b-checkbox_transparent > div:nth-child(1)'))).click()
        shit(driver)
        wait.until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, '.b-toolbar__btn_grouped_first > span:nth-child(2)'))).click()
        shit(driver)

    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://store.steampowered.com/login/')
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="input_username"]'))).send_keys(Steam)
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="input_password"]'))).send_keys(SteamPassNew)
    loginIntoSteam(driver, wait, EmailNew, EmailNewPass, EmailOld, EmailOldPass)
    driver.get('https://store.steampowered.com/account/')
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                           'div.account_setting_block:nth-child(4) > div:nth-child(1) > div:nth-child(3) > a:nth-child(1)'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a.help_wizard_button:nth-child(4)'))).click()
    driver.switch_to.window(driver.window_handles[0])
    steam(wait)
    driver.execute_script("arguments[0].click();",
                          driver.find_element_by_xpath('//*[@title="Steam Support <noreply@steampowered.com>"]'))
    if pochtaIsNew == 1:
        cont = wait.until(ec.element_to_be_clickable((By.XPATH, steamCodeString))).text
    else:
        cont = wait.until(ec.element_to_be_clickable((By.XPATH, steamCodeStringOld))).text
    driver.get('https://e.mail.ru/inbox/')
    shit(driver)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#PH_logoutLink')))
    if pochtaIsNew == 1:
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.button2__explanation'))).click()
        shit(driver)
        wait.until(ec.element_to_be_clickable(
            (By.CSS_SELECTOR, '.button2_delete > span:nth-child(1) > span:nth-child(2)'))).click()
        shit(driver)
        wait.until(ec.element_to_be_clickable(
            (By.CSS_SELECTOR, '.button2_primary > span:nth-child(1) > span:nth-child(1)'))).click()
        shit(driver)
    else:
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.b-checkbox_transparent > div:nth-child(1)'))).click()
        shit(driver)
        wait.until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, '.b-toolbar__btn_grouped_first > span:nth-child(2)'))).click()
        shit(driver)

    driver.get('https://e.mail.ru/inbox/')
    driver.switch_to.window(driver.window_handles[1])
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#forgot_login_code'))).send_keys(cont)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.account_recovery_submit > input:nth-child(1)'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#email_reset'))).send_keys(EmailNew)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#change_email_area > input:nth-child(1)'))).click()
    driver.switch_to.window(driver.window_handles[0])
    driver.get('https://e.mail.ru/inbox/')
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#PH_logoutLink'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#mailbox\:login-input'))).clear()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#mailbox\:login-input'))).send_keys(EmailNew)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#mailbox\:submit-button'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#mailbox\:password-input'))).send_keys(EmailNewPass)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#mailbox\:submit-button'))).click()
    try:
        driver.find_element_by_css_selector('a.btn > span: nth - child(1)')
        steam(wait)

    except NoSuchElementException:
        steam(wait)

    # wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.portal-octavius-widget__button'))).click()
    # wait.until(ec.element_to_be_clickable((By.CLASS_NAME, '.c01643 c0167 c01641 c0165'))).click()
    # wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.c0197'))).click()
    # wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.c01125'))).click()
    # wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.c0124 > svg:nth-child(1)'))).click()
    cont = findSteamCode(driver, wait)
    # driver.get('https://e.mail.ru/inbox/')
    driver.switch_to.window(driver.window_handles[1])
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#email_change_code'))).send_keys(cont)
    wait.until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, 'div.account_recovery_submit:nth-child(2) > input:nth-child(1)'))).click()
    logging.info(
        str(datetime.now()) + ' email changed ' + EmailOld + ' TO ' + EmailNew)
    wait.until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR,
         'div.account_setting_block:nth-child(6) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1)'))).click()
    wait.until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR,
         '#email_authenticator_form > div:nth-child(3) > div:nth-child(2) > label:nth-child(1)'))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="input_username"]'))).send_keys(Steam)
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="input_password"]'))).send_keys(SteamPassNew)
    try:
        driver.find_element_by_partial_link_text('rendercap')

    except NoSuchElementException:
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.btn_blue_steamui'))).click()
    driver.switch_to.window(driver.window_handles[0])
    driver.get('https://e.mail.ru/inbox/')
    shit(driver)
    cont = findSteamCodeGuard(driver, wait)
    driver.switch_to.window(driver.window_handles[1])
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="authcode"]'))).send_keys(cont)
    wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div/div/form/div[4]/div[1]/div[1]/div[1]'))).click()
    wait.until(ec.element_to_be_clickable(
        (By.XPATH, '//*[@id="success_continue_btn"]'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.user_avatar'))).click()
    LetsDeleteEverything(driver, url)
    driver.get(linkTlock)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.help_wizard_button > span:nth-child(1)'))).click()
    time.sleep(1)
    wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[7]/div[2]/div[2]/div/div[2]/div/div/div[3]/a/span'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a.help_wizard_button:nth-child(5) > span:nth-child(1)'))).click()
    code = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.code_text'))).text
    unlockurl = str('https://help.steampowered.com/en/wizard/HelpSelfUnlock?code=' + code + '&account=' + Steam)
    print(unlockurl)
    f = open("checker_withURL.txt", "a")
    data = str(
        EmailNew + ' ' + EmailNewPass + ' ' + Steam + ' ' + SteamPassNew + '  ' + url + '    ' + unlockurl + ' ' + EmailOld + ' ' + EmailPassNew + '\n')
    logging.info(
        str(datetime.now()) + ' DONE!\n ' + data)
    f.write(data)
    f.close()
    #driver.close()


if __name__ == '__main__':
    LOG_FILENAME = 'Loh.log'
    logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)
    ya = 1
    if ya == 1:
        frep = open(r'C:\Users\PussyDestroyer\PycharmProjects\chezahernya\c!replace.txt', 'r')
        profile = FirefoxProfile("C:\\Users\\PussyDestroyer\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\7dvs7u3f.default")
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
