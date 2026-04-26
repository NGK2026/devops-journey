import requests

response = requests.get('https://inventwithpython.com/page_that_does_not_exist')

try:
    response.raise_for_status()
except Exception as exc:
    print(f'There was a problem: {exc}')

print('hello')