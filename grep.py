import sys
import os

for root, dirs, files in os.walk(u'C:\\Users\\Axiuc\\Downloads'):
    print('Current Directory: ', root)
    print('Subidrectories: ', dirs)
    print('Files:', files)

# for root,dirs, files in in files:
#     with open(os.path.join(f'C:\\Users\\Axiuc\\Downloads\\{dirs}', x), 'r') as f:
#         data = f.read()
#     if sys.argv[1] in data:
#         print('ceva')
