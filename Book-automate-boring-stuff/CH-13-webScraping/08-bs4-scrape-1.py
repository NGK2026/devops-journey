import bs4

example_file = open('example3.html')
example_soup = bs4.BeautifulSoup(example_file.read(), 'html.parser')

# element selector author selected
print('\nelement selector #author:\n')
elems = example_soup.select('#author')
print(f'\n{type(elems)}\n')
print(f'{len(elems)}\n')
print(f'typle element[0]:\n{type(elems[0])}\n')
# get element string
print(f'str of element[0]:\n{str(elems[0])}\n')
# get element inner text
print(f'get text in element[0]:\n{elems[0].get_text()}\n')
# get attributes
print(f'attributes of element[0]:\n{elems[0].attrs}\n')

print('element = <p>\n')
p_elems = example_soup.select('p')
print(f'str of p[0]:\n{str(p_elems[0])}\n')

print(f'get text of p[0]:\n{p_elems[0].get_text()}\n')

print(f'str of p[1]:\n{str(p_elems[1])}\n')

print(f'get text of p[1]:\n{p_elems[1].get_text()}\n')

print(f'str of p[2]:\n{str(p_elems[2])}\n')

print(f'get text of p[2]:\n{p_elems[2].get_text()}\n')

# Getting Data from an Element’s Attributes