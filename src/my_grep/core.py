import sys
import os
import click

@click.command()
@click.option('-i', is_flag=True, help ='Case insensitive searching of keyword')
# @click.option('-v', is_flag=True, help ='All words in the line, except the user input keyword')
@click.option('-r', is_flag=True, help ='Iteratively searching through all subdirectories of root_path')
@click.option('-n', is_flag=True, help ='Gives the number of the line')
@click.argument('word')
@click.argument('user_path')

def split_and_search(user_path, word,i,n,r):
    for root, dirs, files in os.walk(user_path):
        for x in files:
            to_read = os.path.join(root, x)
            search(to_read, word,i,n)
    
        if not r: 
            break

def search(to_read,word,i,n):
    try:        
        with open(to_read, "r") as f:
            for line_number, line in enumerate(f):
                if i:
                    if word.lower() in line.lower():
                        if n:
                            click.echo(f"{line_number} {line} found in {to_read}")
                        else:
                            click.echo(f"{line} found in {to_read}")
                else:
                    if word in line :
                        if n:
                            click.echo(f"{line_number} {line} found in {to_read}")
                        else:
                            click.echo(f"{line} found in {to_read}")
    except UnicodeDecodeError:
                continue


     
if __name__ == '__main__':
    split_and_search()
