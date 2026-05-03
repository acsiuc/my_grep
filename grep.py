import sys
import os

for root, dirs, files in os.walk(u'C:\\Users\\Axiuc\\Downloads'):
    for x in files:
        to_read = os.path.join(root, x)
        try:
            with open(to_read, "r") as f:
                for line in f:
                    if sys.argv[1] in line:
                        print(line)
        except UnicodeDecodeError:
            continue

# for root,dirs, files in in files:
#     with open(os.path.join(f'C:\\Users\\Axiuc\\Downloads\\{dirs}', x), 'r') as f:
#         data = f.read()
#     if sys.argv[1] in data:
#         print('ceva')
