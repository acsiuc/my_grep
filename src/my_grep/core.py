import sys
import os
import click

@click.command()
@click.option('-i', is_flag=True, help ='Case insensitive searching of keyword')
@click.option('-n', is_flag=True, help ='Gives the number of the line')
@click.argument('word')
@click.argument('user_path')

def search(word, user_path,i,n):
    for root, dirs, files in os.walk(user_path):
        for x in files:
            to_read = os.path.join(root, x)
            try:
                with open(to_read, "r") as f:
                    for line_number, line in enumerate(f):
                        if i is True:
                            if word.lower() in line.lower():
                                if n is True:
                                    print(line_number,line,f'found in {to_read}')
                                else:
                                    print(line,f'found in {to_read}')
                        else:
                            if word in line :
                                if n is True:
                                    print(line_number,line,f'found in {to_read}')
                                else:
                                    print(line,f'found in {to_read}')
            except UnicodeDecodeError:
                continue

