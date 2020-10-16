#!/usr/bin/env python
import click
import sys

@click.command()
@click.option("--s")
def hello(s):
    print("Word length:"+len(s))
    
if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    hello()
