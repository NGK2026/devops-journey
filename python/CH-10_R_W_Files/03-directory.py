from pathlib import Path
import os

print(Path.cwd())
# /home/student/Projects/automate-boring-stuff

os.chdir('/home/student/Documents')
print(Path.cwd())
# /home/student/Documents

print(Path.home())
# /home/student

