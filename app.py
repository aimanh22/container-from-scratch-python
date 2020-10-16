#!/usr/bin/env python
import click
import sys
import spacy

@click.command()
@click.option("--s")
def hello(s):
    nlp = spacy.load('en')
    doc=nlp(s)
    for ent in doc.ents:
        print(ent.text, ent.label_)
    
if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    hello()
