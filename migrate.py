import os
import sys
import json


def find_pytorch():
    for p in sys.path:
        candidate = os.path.join(p, 'torch')
        if os.path.exists(candidate):
            return candidate
    print('site-packages not found!')
    exit(1)

out_path = find_pytorch()

print('pytorch root is', out_path)

backup = json.load(open('pyi.json'))
print('read', len(backup), 'pyi files.')

for p, content in reversed(backup):
    print('trying to place', p, '... ')
    new_path = os.path.join(out_path, p)
    if os.path.exists(new_path):
        print('file', new_path, 'exists')
    else:
        print('dump to', new_path)
        with open(new_path, 'w') as fp:
            fp.write(content)

print('done')
