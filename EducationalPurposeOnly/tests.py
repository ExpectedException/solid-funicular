import requests
import json
import traceback


host_url = 'https://intense-savannah-92593.herokuapp.com'
basic_auth = 'postgres3', '12345678'
try:
    bankUsers = json.loads(requests.get(host_url + '/api/user/util/allBankUsers', auth=(basic_auth)).text)
    print(bankUsers)
    for 
    accountId = bankUsers["id"]
except:
    traceback.print_exc()
    accountId = 0
try:
    balance = requests.get(host_url + "/api/bankUser/atm/balance{}".format(accountId), auth=(basic_auth)).text
    print(balance)
except:
    traceback.print_exc()

r = requests.post(host_url + '/api/bankUser/accounts/newAccount', auth=(basic_auth))
print(r.status_code)
print(requests.get(host_url + '/api/bankUser/accounts/allId', auth=(basic_auth)).text)
