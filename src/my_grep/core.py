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

user_path = arguments[-1]

for root, dirs, files in os.walk(user_path):
    for x in files:
        to_read = os.path.join(root, x)
        try:
            with open(to_read, "r") as f:
                for line_number, line in enumerate(f):
                    if arguments[0] in line:
                        print(line_number, line)
        except UnicodeDecodeError:
            continue

