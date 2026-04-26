import subprocess

file_obj = open('hello.txt', 'w')
file_obj.write('Hello nazeeh hi hello')
file_obj.close()

# xdg linux style, start windows, open macos
subprocess.run(['xdg-open', 'hello.txt'])