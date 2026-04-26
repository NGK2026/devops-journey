import requests, bs4

res = requests.get('https://autbor.com/example3.html')
print(res.raise_for_status())
example_soup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(example_soup))

with open('example3.html') as example_file:
    example_soup = bs4.BeautifulSoup(example_file, 'html.parser')

print(type(example_soup))

