import subprocess

# will launch and pause
# subprocess.run(['/usr/bin/gnome-calculator'])

# launch and continue
calc_proc = subprocess.Popen(['/usr/bin/gnome-calculator'])

print('hello')

# kill running process
calc_proc.kill()

# launch prog and add cmd argument
# subprocess.run(['example app', 'example argument'])
proc = subprocess.run(['ping', '-c', '4', 'archlinux.org'], capture_output=True, text=True)

print('&&&&&&%$$$$$$#####&&&&&&&*************')
# print the proc output stored in 'proc'
print(proc)