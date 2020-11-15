import requests


r = requests.get('https://api.mail.ru/user', auth=('user', 'pass'))
print(r.status_code)