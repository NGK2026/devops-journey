from pathlib import Path
import os

print(Path.cwd())
# /home/student/Projects/automate-boring-stuff
print(Path.cwd().is_absolute())
# True
print(Path('spam/beef/eggs').is_absolute())
# False

os.chdir('/home/student')
print(Path.cwd())
print(Path('my/relative/path'))
# absolute path object
print(Path.cwd() / 'my/relative/path')
print(Path('my/relative/path').absolute())
print(Path.home() / Path('my/relative/new/path'))
print(Path.home() / 'my/relative/new/path')
