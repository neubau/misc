import re
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import random

vocab = {}
with open("vocab.txt") as f:
    lines = f.readlines()
    random.shuffle(lines)
    for line in lines:
        try:
            lemma, definition = re.split("\s\s+", line, maxsplit=1)
            vocab[lemma] = definition
            if len(vocab) > 100:
                break
        except:
            print("Problem: " + line)
            
env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)
slider_template = env.get_template("slider.html")
with open('docs/vocab.html', 'w') as vocab_file:
    print(slider_template.render(vocab=vocab), file=vocab_file)
