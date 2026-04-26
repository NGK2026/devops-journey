import csv

output_file = open('output.csv', 'w+', newline='') # w+ = write + read
output_writer = csv.writer(output_file)

output_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
output_writer.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
output_writer.writerow([1, 2, 3.141592, 4])

# rewind pointer back to 0
output_file.seek(0)

# read csv
reader = csv.reader(output_file)
for row in reader:
    print('ROW #' + str(reader.line_num) + ' ' + str(row))

output_file.close()