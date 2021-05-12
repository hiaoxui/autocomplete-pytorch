import os
import sys
import json

in_path = sys.argv[1]
print('read from', in_path)

backup = list()

for root, dirs, files in os.walk(in_path):
    for f in files:
        if f == '__init__.pyi':
            p = os.path.join(root, f)
            print('found', p.replace(in_path+'/', ''))
            backup.append([p.replace(in_path+'/', ''), open(p).read()])

json.dump(backup, open('pyi.json', 'w'))

