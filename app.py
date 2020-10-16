#!/usr/bin/env python
import click
import sys
import spacy

@click.command()
@click.option("--name ")
def hello(name):
    nlp = spacy.load('en')
    doc=nlp(name)
    for ent in doc.ents:
        print(ent.text, ent.label_)
    
if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    hello()
