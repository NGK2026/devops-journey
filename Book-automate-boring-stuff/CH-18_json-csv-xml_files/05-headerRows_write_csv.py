import csv
import pprint

output_file = open('outputWheader.csv', 'w+', newline='')
output_dict_writer = csv.DictWriter(output_file, ['Name', 'Pet', 'Phone'])

output_dict_writer.writeheader()

output_dict_writer.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
output_dict_writer.writerow({'Name': 'Bob', 'Phone': '555-9999'})
output_dict_writer.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})

output_file.seek(0)

reader = csv.DictReader(output_file)
output_data = list(reader)

pprint.pprint(output_data)
"""
[{'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'},
 {'Name': 'Bob', 'Pet': '', 'Phone': '555-9999'},
 {'Name': 'Carol', 'Pet': 'dog', 'Phone': '555-5555'}]
"""

output_file.close()