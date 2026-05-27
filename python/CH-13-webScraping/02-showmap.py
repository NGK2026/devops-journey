# showmap.py - Launches a map in the browser using an address from the
# command line or clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

# Open browser.
# webbrowser.open('https://www.openstreetmap.org/' + address) # node/6586747428
webbrowser.open('https://www.google.com/maps/place/' + address) # 18 hassan assem zamalek cairo

