import requests
from pathlib import Path

p = Path(__file__).resolve().parent
(p / 'rj').mkdir(exist_ok=True)

response = requests.get('https://automatetheboringstuff.com/files/rj.txt')

try:
    response.raise_for_status()
except Exception as exc:
    print(f'there was a problem: {exc}\n')

# wb = write binary
# 100,000 is good size for getting chunks
with open(p / 'rj/RomeoAndJuliet.txt', 'wb') as play_file:
    for chunk in response.iter_content(100000): 
        print(play_file.write(chunk))
        # 100000
        # 74126


