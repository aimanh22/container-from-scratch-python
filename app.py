#!/usr/bin/env python
import click
import sys
import spacy

@click.command()
@click.option("--sentence ")
def hello(sentence):
    nlp = spacy.load('en')
    doc=nlp(sentence)
    for ent in doc.ents:
        print(ent.text, ent.label_)
    
if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    hello()
