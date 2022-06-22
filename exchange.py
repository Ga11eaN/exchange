import fileinput
from pathlib import Path


str_to_find = input('Enter the text to replace: ')
str_to_change = input('Enter the new text: ')
extensions = []
while True:
    extension = input('Enter extension or type "stop" to finish: ')
    if extension == 'stop':
        break
    else:
        extensions.append(f'*.{extension}')

files = [Path().glob(e) for e in extensions]
for file in files:
    with fileinput.FileInput(file, inplace=True, backup='.bak') as f:
        for line in f:
            print(line.replace(str_to_find, str_to_change), end='')
