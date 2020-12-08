import requests
import json
import traceback


def showAllBankUsers(expCode):
    try:
        print('\n/api/bankUser/accounts/allId\n')
        print('args = ' + str(basic_auth))
        print('expected :\nusers and status code {}'.format(expCode))
        r = requests.get(host_url + '/api/user/util/allBankUsers', auth=(basic_auth))
        txt = r.text
        bankUsers = json.loads(txt)
        print('response : ')
        print(bankUsers)
        print('show showAllBankUsers status code ' + str(r.status_code))
        for i in bankUsers:
            if i['username'] == username:
                return int(i["id"])
    except:
        traceback.print_exc()

def showBalance(accountId, expCode):
    try:
        print('/api/bankUser/atm/balance{}\n')
        print('args = ' + str(basic_auth) + ' accID= ' + str(accountId))
        print('expected :\nbalance and status code {}'.format(expCode))
        r = requests.get(host_url + "/api/bankUser/atm/balance{}".format(accountId), auth=(basic_auth))
        balance = requests.get(host_url + "/api/bankUser/atm/balance{}".format(accountId), auth=(basic_auth)).text
        print('response : ')
        print('balance ' + balance)
        print('show balance status code ' + str(r.status_code))
    except:
        traceback.print_exc()


def depo(accountId, deposit, expCode):
    try:
        dto = {
            "accountId": accountId,
            "atmId": 1,
            "toAdd": deposit
        }
        print('/api/bankUser/atm/deposit\n')
        print('args = ' + str(basic_auth) + 'accID= ' + str(accountId) + str(dto))
        print('expected :\nstatus code {}'.format(expCode))
        r = requests.post(host_url + '/api/bankUser/atm/deposit', json=dto, auth=(basic_auth))
        print('response : ')
        print('deposit status code ' + str(r.status_code))
        if int(deposit) < 0:
            showBalance(accountId, expCode=400)
        else:
            showBalance(accountId, expCode=200)
    except:
        traceback.print_exc()


def transf(accountId, transfer, expCode):
    try:
        dto = {
                "amount": transfer,
                "fromAccountId": accountId,
                "toAccountId": 2
                }
        print('/api/bankUser/atm/transfer\n')
        print('args = ' + str(basic_auth) + 'accID= ' + str(accountId) + str(dto))
        print('expected :\nstatus code {}'.format(expCode))
        r = requests.post(host_url + '/api/bankUser/atm/transfer', json=dto, auth=(basic_auth))
        print('transfer status code ' + str(r.status_code))
        if int(transfer) < 0:
            showBalance(accountId, expCode=400)
        else:
            showBalance(accountId, expCode=200)
    except:
        traceback.print_exc()


def withdrw(accountId, withdraw, expCode):
    try:
        dto = {
                "accountId": accountId,
                "atmId": 1,
                "toSub": withdraw
                }
        print('/api/bankUser/atm/withdraw\n')
        print('args = ' + str(basic_auth) + 'accID= ' + str(accountId) + str(dto))
        print('expected :\nstatus code {}'.format(expCode))
        r = requests.post(host_url + '/api/bankUser/atm/withdraw', json=dto, auth=(basic_auth))
        print('withdrw status code ' + str(r.status_code))
        if int(withdraw) < 0:
            showBalance(accountId, expCode=400)
        else:
            showBalance(accountId, expCode=200)
    except:
        traceback.print_exc()


def addcash(addcsh, expCode):
    try:
        dto = {
                "atmId": 1,
                "toAdd": addcsh
                }
        print('/api/collector/atmCash/add\n')
        print('args = ' + str(notbasic_auth) + ' ' + str(dto))
        print('expected :\nstatus code {}'.format(expCode))
        r = requests.post(host_url + '/api/collector/atmCash/add', json=dto, auth=(notbasic_auth))
        print('add status code ' + str(r.status_code))
    except:
        traceback.print_exc()


def createAtm(expCode):
    try:
        print('/api/collector/atmCash/add\n')
        print('args = ' + str(notbasic_auth))
        print('expected :\nstatus code {}'.format(expCode))
        r = requests.post(host_url + '/api/collector/atm', auth=(notbasic_auth))
        print('create status code ' + str(r.status_code))
    except:
        traceback.print_exc()


def deleteAtm(id,expCode):
    try:
        print('/api/collector/atm/{}\n')
        print('args = ' + str(notbasic_auth) + 'id- ' + str(id))
        print('expected :\nstatus code {}'.format(expCode))
        r = requests.delete(host_url + '/api/collector/atm/{}'.format(id), auth=(notbasic_auth))
        print('delete status code ' + str(r.status_code))
    except:
        traceback.print_exc()


def showallAtm(expCode):
    try:
        print('/api/collector/atm/allId\n')
        print('args = ' + str(notbasic_auth))
        print('expected :\nshow atms and status code {}'.format(expCode))
        r = requests.get(host_url + '/api/collector/atm/allId', auth=(notbasic_auth))
        print('show all status code ' + str(r.status_code))
        print('atms ' + str(r.text))
    except:
        traceback.print_exc()


def registr(new_acc_pass, new_acc_usrnm, expCode):
    try:
        dto = {
                "password": new_acc_pass,
                "username": new_acc_usrnm
                }
        print('/api/reg/bankUser\n')
        print('args = ' + str(dto))
        print('expected :\nstatus code {}'.format(expCode))
        r = requests.post(host_url + '/api/reg/bankUser', json=dto)
        print('registration status code ' + str(r.status_code))
    except:
        traceback.print_exc()


def showallBankIds():
    try:
        print('/api/bankUser/accounts/allId\n')
        print('args = ' + str(basic_auth))
        print('expected :\nids and status code 200')
        r = requests.get(host_url + '/api/bankUser/accounts/allId', auth=(basic_auth))
        print('response : ')
        print('show bankAccountsOfCurrentUser status code ' + str(r.status_code))
        print('ids ' + str(r.text))
    except:
        traceback.print_exc()


host_url = 'https://intense-savannah-92593.herokuapp.com'
username = 'postgres3'
passwd = '12345678'
collector_username = 'collector'
collector_passwd = '12345678'
basic_auth = username, passwd
notbasic_auth = collector_username, collector_passwd

print('Адекватные параметры')
accountId = showAllBankUsers(expCode=200)
print('Адекватные параметры')
showBalance(accountId, expCode=200)
showBalance(accountId=100000, expCode=403)
print('Неадекватные параметры')
showBalance(accountId=-1000, expCode=400)
showBalance(accountId=-0.5, expCode=400)
print('Адекватные параметры')
depo(accountId, deposit=10000, expCode=200)
depo(accountId, deposit=1000000000000000000000000000000000000000000000000000000000000000000000000000000000, expCode=200)
depo(accountId=1000000, deposit=10000000000000000000000000000000000000000000000000000000000000000000000000, expCode=403)
print('Неадекватные параметры')
depo(accountId, deposit=-10000000000000000000000000000000000000000000, expCode=400)
depo(accountId=-1000000, deposit=10000000000000000000000000000000000000000000000000000000, expCode=400)
print('Адекватные параметры')
transf(accountId=1, transfer=10000, expCode=200)
transf(accountId=1, transfer=1000000000000000000000000000000000000000000000000000000000000000000000000000000000, expCode=200)
transf(accountId=1000000, transfer=10000000000000000000000000000000000000000000000000000000000000000000000000, expCode=403)
print('Неадекватные параметры')
transf(accountId=1, transfer=-10000000000000000000000000000000000000000000, expCode=400)
transf(accountId=-1000000, transfer=10000000000000000000000000000000000000000000000000000000, expCode=400)
print('Адекватные параметры')
withdrw(accountId=1,withdraw=10000, expCode=200)
withdrw(accountId=1, withdraw=1000000000000000000000000000000000000000000000000000000000000000000000000000000, expCode=200)
withdrw(accountId=1000000, withdraw=10000000000000000000000000000000000000000000000000000000000000000000000000, expCode=403)
print('Неадекватные параметры')
withdrw(accountId=1, withdraw=-10000000000000000000000000000000000000000000, expCode=400)
withdrw(accountId=-1000000, withdraw=10000000000000000000000000000000000000000000000000000000, expCode=400)
print('Адекватные параметры')
addcash(addcsh=10000, expCode=200)
addcash(addcsh=1000000000000000000000000000000000000000000000000000000000000000000000000000000, expCode=200)
addcash(addcsh=pow(100, 100), expCode=400)
print('Неадекватные параметры')
addcash(addcsh=-10000000000000000000000000000000000000000000, expCode=400)
print('Аадекватные параметры')
createAtm(expCode=201)
print('Аадекватные параметры')
deleteAtm(id=1, expCode=200)
deleteAtm(id=1000123, expCode=204)
print('Неадекватные параметры')
deleteAtm(id=-1, expCode=400)
deleteAtm(id=-1000, expCode=400)
print('Аадекватные параметры')
showallAtm(expCode=200)
print('Аадекватные параметры')
registr(new_acc_usrnm='qwe231', new_acc_pass='qwe123qwe', expCode=201)
registr(new_acc_usrnm='qwe1', new_acc_pass='qwe123qwe', expCode=409)
print('Неадекватные параметры')
registr(new_acc_usrnm='-436543624632080931254авпвыарвапы09324=-324=324=-0325-0=fdsf$#@$%#@qwe1',
        new_acc_pass='qwe21-308r0-23idxr-m23фывпавыфп-irmm-c03euirn-0e31uirx-0ewmur-za081,2=832=-18r2193078r21123qwe', expCode=400)
showallBankIds()