# This program has bugs, however. Rewrite the code to fix the errors. You may assume the user always enters valid inputs and not, say, X for the scale or hello for the number of degrees.

print('Enter C or F to indicate Celsius or Fahrenheit:')
scale = input()
print('Enter the number of degrees:')
degrees = float(input())
if scale == 'C':
    if degrees >= 16 and degrees <= 38:
        print('Safe')
    else:
        print('Dangerous')
elif scale == 'F':
    if degrees > 60.8 and degrees <= 100.4:
        print('Safe')
    else:
        print('Dangerous')