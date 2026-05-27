import csv
import pprint

example_file = open('exampleWithHeader3.csv')
example_dict_reader = csv.DictReader(example_file)
example_dict_data = list(example_dict_reader)

pprint.pprint(example_dict_data)
print()

example_file.close()

# with loop
example_file = open('exampleWithHeader3.csv')
example_dict_reader = csv.DictReader(example_file)

for row in example_dict_reader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])
print()
example_file.close()

# with csv that has no headers
example_file = open('example3.csv')
example_dict_reader = csv.DictReader(example_file, ['time', 'name', 'amount'])

for row in example_dict_reader:
    print(row['time'], row['name'], row['amount'])