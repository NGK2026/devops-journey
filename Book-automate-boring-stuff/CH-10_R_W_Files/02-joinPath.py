from pathlib import Path

print(Path('spam') / 'beef' / 'eggs')
# spam/beef/eggs

print(Path('spam') / Path('beef/eggs'))
# spam/beef/eggs

print(Path('spam') / Path('beef', 'eggs'))
# spam/beef/eggs