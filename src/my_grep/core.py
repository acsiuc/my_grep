import sys
import os

arguments = []
flags = []
for x in sys.argv[1:]:
    if x[0] == '-' and x[1].isalpha():
        flags.append(x)
    else:
        arguments.append(x)

print(flags)
print(arguments)

if arguments:
    if len(arguments)>1:
        user_path = arguments[-1]
    elif len(arguments) == 1:
        user_path = '.'
    for root, dirs, files in os.walk(user_path):
        for x in files:
            to_read = os.path.join(root, x)
            try:
                with open(to_read, "r") as f:
                    for line_number, line in enumerate(f):
                        if '-i' in flags:
                            if arguments[0].lower() in line.lower():
                                if '-n' in flags:
                                    print(line_number,line,f'found in {to_read}')
                                elif arguments[0].lower() in line.lower():
                                    print(line,f'found in {to_read}')
                        else:
                            if arguments[0] in line :
                                if '-n' in flags:
                                    print(line_number,line,f'found in {to_read}')
                                elif arguments[0] in line:
                                    print(line,f'found in {to_read}')
            except UnicodeDecodeError:
                continue

