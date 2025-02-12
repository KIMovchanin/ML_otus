# import logging

import requests
from pprint import pprint

# sync requests
# async httpx, aiohttp

url = 'https://otus.ru'  # 443
# session = requests.Session()
# SLA
response = requests.get(
    url=url,
    timeout=5,
    # data=..,
    # json=...,
    # verify=None,
    # headers={'Auth': 'Bearer 651sd65f1f65f1ds'}
)
# print(dir(response))
# if response.status_code >= 500:
#     print('Server error')
#
# if response.status_code >= 400:
#     print('Client error')

response.raise_for_status()
print(response.status_code)
pprint(dict(response.headers))
print(response.text)
try:
    print(response.json())
except Exception:
    print(response.text)
