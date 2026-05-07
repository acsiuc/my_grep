import sys
import os
import click

@click.command()
@click.option('-i', is_flag=True, help ='Case insensitive searching of keyword')
# @click.option('-v', is_flag=True, help ='All words in the line, except the user input keyword')
@click.option('-c', is_flag=True, help ='How many times the word has been encountered in the files')
@click.option('-r', is_flag=True, help ='Iteratively searching through all subdirectories of root_path')
@click.option('-n', is_flag=True, help ='Gives the number of the line')
@click.argument('word')
@click.argument('user_path')

def split_and_search(user_path, word,i,n,r,c):
    counter = 0
    for root, dirs, files in os.walk(user_path):
        try:
            for x in files:
                to_read = os.path.join(root, x)
                counter+=search(to_read, word,i,n,c)
            if not r: 
                break
        except UnicodeDecodeError:
            continue
    if c:
        click.echo(f"{word} was found {counter} times")

def search(to_read,word,i,n,c):   
    counter = 0  
    with open(to_read, "r") as f:
        for line_number, line in enumerate(f):
            if i:
                if word.lower() in line.lower():
                    counter+=1
                    if not c:
                        if n:
                            click.echo(f"{line_number} {line} found in {to_read}")
                        else:
                            click.echo(f"{line} found in {to_read}")
            else:
                if word in line :
                    counter+=1
                    if not c:
                        if n:
                            click.echo(f"{line_number} {line} found in {to_read}")
                        else:
                            click.echo(f"{line} found in {to_read}")
    return counter




     
if __name__ == '__main__':
    split_and_search()
