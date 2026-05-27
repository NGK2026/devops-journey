import requests

response = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(type(response))
# <class 'requests.models.Response'>

print(response.status_code == requests.codes.ok)
# 200 == 200 ?
# True

print(len(response.text))
# 174126

print(response.text[:210])
"""
The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-
"""

