from pathlib import Path

bfp = Path(__file__).resolve().parent 

beef_file = open(bfp / 'beef.txt', 'w', encoding='utf-8')
beef_file.write('Hello, beef!\n')
beef_file.close()

beef_file = open(bfp / 'beef.txt', 'a', encoding='utf-8')
beef_file.write('beef is not feeb.')
beef_file.close()

beef_file = open(bfp / 'beef.txt', encoding='utf-8')
content = beef_file.read()
beef_file.close()

print(content)

