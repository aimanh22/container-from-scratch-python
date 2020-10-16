#!/usr/bin/env python
import click
import sys
import spacy

@click.command()
@click.option("--name")
def hello(name):
    click.echo(f'Hello {name}!')

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    input = sys.argv[1:] 
    str = "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in tokens]).strip()
    nlp = spacy.load('en')
    doc=nlp(str)
    for ent in doc.ents:
        print(ent.text, ent.label_)
    hello()
