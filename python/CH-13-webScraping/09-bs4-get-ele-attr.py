import bs4

soup = bs4.BeautifulSoup(open('example3.html'), 'html.parser')
span_elem = soup.select('span')[0]

# element str
print('span[0] str:')
print(str(span_elem))

# get id
print('span[0] id:')
print(span_elem.get('id'))

# some non existing addr?
print('some_nonexistent_addr?:')
print(span_elem.get('some_nonexistent_addr') == None)

# print elem attr
print('span[0] element attributes:')
print(span_elem.attrs)