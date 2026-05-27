import csv
import pprint

example_file = open('example3.csv')
example_reader = csv.reader(example_file)
example_data = list(example_reader)

pprint.pprint(example_data)

print(f'\n{example_data[0][1]}') # Apples

print(f'\n{example_data[6][1]}\n') # Strawberries

example_file.close()

# READ LARGE CSV FILES

example_file = open('example3.csv')
example_reader = csv.reader(example_file)

for row in example_reader:
    print('ROW #' + str(example_reader.line_num) + ' ' + str(row))
"""
ROW #1 ['4/5/2035 13:34', 'Apples', '73']
ROW #2 ['4/5/2035 3:41', 'Cherries', '85']
ROW #3 ['4/6/2035 12:46', 'Pears', '14']
ROW #4 ['4/8/2035 8:59', 'Oranges', '52']
ROW #5 ['4/10/2035 2:07', 'Apples', '152']
ROW #6 ['4/10/2035 18:10', 'Bananas', '23']
ROW #7 ['4/10/2035 2:40', 'Strawberries', '98']
"""


example_file.close()
