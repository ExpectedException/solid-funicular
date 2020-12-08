from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time, traceback
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from datetime import datetime
import logging
from selenium.common.exceptions import TimeoutException
import re
from selenium.webdriver import ActionChains
import urllib.parse
import json
from addons.list_search import ListSearch


def Convert(string):
    li = list(string.split(":"))
    return li

def checkPrime(driver, wait, pRank):
    if pRank >= 21:
        return 1
    else:
        medal = driver.find_element_by_css_selector('div.generic_kv_line:nth-child(2)').text
        if medal == 'Получена медаль за службу: Да' or medal == 'Earned a Service Medal: Yes':
            return 1
        else:
            prime = 0
        try:
             wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[7]/div[2]/div/div[2]/div/div[3]/div[2]/div/a'))).click()
             wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[7]/div[2]/div/div[2]/div/div[5]')))
             prime = 0
        except:
            if prime == 0:
                return 0
            else:
                return 1


def CreateHeader(driver, EmailNew, EmailNewPass, Steam, SteamPassNew, ID64, EmailOld, EmailPassNew, primeStatus, pRank):
    driver.get("https://help.steampowered.com/en/")
    wait = WebDriverWait(driver, 15)
    url = str('https://steamcommunity.com/profiles/' + ID64)
    try:
        wait.until(ec.element_to_be_clickable((By.ID, 'wizard_contents')))
        help_event_limiteduser = driver.find_element_by_css_selector(".help_event_limiteduser")
        if "limited" in help_event_limiteduser.text:
            limit = 1
        else:
            limit = 0
    except:
        limit = 0
    try:
        pRank = str(pRank)
        game_ids = parseGames(driver, url)
        if (len(game_ids) > 0):
            key = ListSearch("730", "s", game_ids)
            header = "NOT CS GO"
            if key != None:
                rank = checkRankInCs(driver, url)
                wrArray = Convert(rank)
                hrs = game_ids[key]
                hrs = hrs['h']
                if limit == 0:
                    header = str('[' + primeStatus + '] ' + wrArray[1] + ' | Private Rank ' + pRank + ' | ' + 'No Limit | ' + hrs + ' hrs | ')
                elif limit == 1:
                    header = str('[' + primeStatus + '] ' + wrArray[1] + ' | Private Rank ' + pRank + ' | ' + hrs + ' hrs | ')
                techStr = str(primeStatus + ']' + wrArray[0]+']' + wrArray[1] + ']' + hrs)
                f = open('checkerWithHeader.txt', "a")
                data = str(
                    EmailNew + ';' + EmailNewPass + ';' + Steam + ';' + SteamPassNew + ';' + '' + ';' + url + ';' + header +';;;'+ techStr + ';' + EmailOld + ';' + EmailPassNew + '\n')
                print(data)
                f.write(data)
                f.close()
                logging.info(str(datetime.now()) + ' ' + data)
    except:
        traceback.print_exc()


def checkRankInCs(driver, url):
    ID64 = re.findall("\d+", url)[0]
    wait = WebDriverWait(driver, 10)
    url = str('https://steamcommunity.com/profiles/' + ID64 + '/gcpd/730/?tab=matchmaking')
    driver.get(url)
    wins = '0'
    rank = 'UnRanked'
    try:
        wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="tabid_accountmain"]')))
        tr = driver.find_elements_by_tag_name('tr')
        for i in tr:
            if "Competitive" in i.text:
                i = i.find_elements_by_tag_name('td')
                break
        wins = i[1].text
        rank = int(i[4].text)
        if rank == 1:
            rank = 'Silver 1'
        elif rank == 2:
            rank = 'Silver 2'
        elif rank == 3:
            rank = 'Silver 3'
        elif rank == 4:
            rank = 'Silver 4'
        elif rank == 5:
            rank = 'Silver Elite'
        elif rank == 6:
            rank = 'Silver Elite Master'
        elif rank == 7:
            rank = 'Gold Nova 1'
        elif rank == 8:
            rank = 'Gold Nova 2'
        elif rank == 9:
            rank = 'Gold Nova 3'
        elif rank == 10:
            rank = 'Gold Nova Master'
        elif rank == 11:
            rank = 'Master Guardian 1'
        elif rank == 12:
            rank = 'Master Guardian 2'
        elif rank == 13:
            rank = 'Master Guardian Elite'
        elif rank == 14:
            rank = 'Distinguished Master Guardian'
        elif rank == 15:
            rank = 'Legendary Eagle'
        elif rank == 16:
            rank = 'Legendary Eagle Master'
        elif rank == 17:
            rank = 'Supreme Master First Class'
        elif rank == 18:
            rank = 'Global Elite'
        else:
            rank = 'UnRanked'
        return str(wins + ':' + rank)
    except:
        traceback.print_exc()
        return str(wins + ':' + rank)


def parseGames(driver, url):
    wait = WebDriverWait(driver, 5)
    game_ids =[]
    ID64 = re.findall("\d+", url)[0]
    url = str('https://steamcommunity.com/profiles/' + ID64 + '/games/?tab=all')
    driver.get(url)
    try:
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.user_avatar')))
    except:
        traceback.print_exc()
    try:
        all_games = driver.find_elements_by_css_selector(".gameListRow")

        for game in all_games:
            game_css_id = game.get_attribute("id")
            game_id = game_css_id.replace("game_", "")
            game_name = game.find_element_by_css_selector(".gameListRowItem .gameListRowItemName").text
            hours = game.find_element_by_css_selector(".gameListRowItem .hours_played").text.replace(" hrs on record",
                                                                                                     "")
            game_ids.append({"s": game_id, "n": game_name, "h": hours})

        return game_ids
    except:
        traceback.print_exc()
        #driver.get_screenshot_as_file(config.paths["chrome_screenshots_dir"] + "\\parse_" + Account.username + ".png")
        # os.system("pause")


def checkGames(driver, EmailNew, EmailNewPass, Steam, SteamPassNew, url, EmailOld, EmailPassNew):
    wait = WebDriverWait(driver, 5)
    ID64 = re.findall("\d+", url)[0]
    url = str('https://steamcommunity.com/profiles/' + ID64 + '/gcpd/730/')
    driver.get(url)
    primeStatus = 'NO PRIME'
    pRank = 0
    try:
        wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="tabid_accountmain"]')))
        lines = driver.find_elements_by_class_name('generic_kv_line')
        for iter in lines:
            if "CS:GO Profile Rank" in iter.text:
                pRank = int(re.findall("\d+", iter.text)[0])
        prime = checkPrime(driver, wait, pRank)
        if prime == 1:
            primeStatus = 'PRIME'
        elif prime == 0:
            primeStatus = 'NO PRIME'
    except:
        pass
    CreateHeader(driver, EmailNew, EmailNewPass, Steam, SteamPassNew, ID64, EmailOld, EmailPassNew, primeStatus, pRank)


def jSonParse(driver, wait):
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#global_actions > a'))).click()
    jsnstr = driver.find_element_by_id('webui_config').get_attribute('data-userinfo')
    y = json.loads(jsnstr)
    url = str('https://steamcommunity.com/profiles/' + y['steamid'] + '/')
    return url


def CommentsShouldDie(driver, url):
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    GoNext = 0
    #wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#account_pulldown'))).click()
    #wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#account_language_pulldown'))).click()
    #wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '#account_language_pulldown'))).click()
    try:
        wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.playerAvatarAutoSizeInner')))
    except:
        pass

    while GoNext == 0:
        try:
            wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'commentthread_comment_content')))
            id = driver.execute_script("return document.querySelector('.commentthread_comment_text').id")
            idNumbers = re.findall("\d+", id)[0]
            urlNumbers = re.findall("\d+", url)[0]
            DELETE = str('javascript:CCommentThread.DeleteComment( "Profile_' + urlNumbers + '", "' + idNumbers + '"  );')
            driver.execute_script(DELETE)
            time.sleep(1)
        except:
            GoNext = 1


def ChatShit(driver):
    GoNext = 0
    wait = WebDriverWait(driver, 10)
    driver.get('https://steamcommunity.com/chat/')
    while GoNext == 0:
        try:
            wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'ContextMenuButton')))
            time.sleep(0.5)
            el = driver.find_element_by_class_name('chatRoomListContainer')
            el.find_element_by_class_name('ContextMenuButton').click()
            #if custom group
            try:
                driver.find_element_by_xpath('//body/div[5]/div/div/div[4]')
                wait.until(ec.element_to_be_clickable((By.XPATH, "//body/div[5]/div/div/div[3]"))).click()
            except NoSuchElementException:
                pass
            try:
                driver.find_element_by_xpath('//body/div[5]/div/div/div[3]')
                wait.until(ec.element_to_be_clickable((By.XPATH, "//body/div[5]/div/div/div[2]"))).click()
            except NoSuchElementException:
                pass
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
        except:
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


def LetsDeleteEverything(driver, EmailNew, EmailNewPass, Steam, SteamPassNew, url, EmailOld, EmailPassNew):
    checkGames(driver, EmailNew, EmailNewPass, Steam, SteamPassNew, url, EmailOld, EmailPassNew)
    CommentsShouldDie(driver, url)
    LeaveGroups(driver, url)
    PengingInvites(driver, url)
    Following(driver, url)
    Blocked(driver, url)
    PengingFriends(driver, url)
    FuckFriends(driver, url)
    ChatShit(driver)
