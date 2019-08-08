import re
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import random

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)
slider_template = env.get_template("slider.html")

with open("vocab.txt") as f:
    lines = f.readlines()
    random.shuffle(lines)
    vocab = {}
    file_id = 1
    for line in lines:
        try:
            lemma, definition = re.split("\s\s+", line, maxsplit=1)
            vocab[lemma] = definition
            if len(vocab) == 100:
                with open(f'docs/{file_id}.html', 'w') as vocab_file:
                    print(slider_template.render(vocab=vocab), file=vocab_file)                 
                file_id = file_id + 1
                vocab = {}
        except:
            print("Problem: " + line)
            
