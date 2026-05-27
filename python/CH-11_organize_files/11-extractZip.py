import zipfile

example_zip = zipfile.ZipFile('example.zip')

# extract all to 'unzipped' folder
example_zip.extractall('unzipped')
example_zip.close()

# extract just 'file1.txt'
example_zip.extract('file1.txt')
# extract just 'file1.txt' to 'unzipped' folder
example_zip.extract('file1.txt', 'unzipped')
example_zip.close()