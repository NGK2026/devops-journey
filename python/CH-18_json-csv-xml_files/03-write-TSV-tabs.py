import csv

output_file = open('output.tsv', 'w+', newline='')
output_writer = csv.writer(output_file, delimiter='\t', lineterminator='\n\n')

output_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
output_writer.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
output_writer.writerow([1, 2, 3.141592, 4])

output_file.seek(0)

reader = csv.reader(output_file)

for row in reader:
    print('ROW #' + str(reader.line_num) + ' ' + str(row))

output_file.close()