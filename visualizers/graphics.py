from pathlib import Path

import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')
doc1 = nlp(u'This is a sentence.')
doc2 = nlp(u'This is another sentence.')
html = displacy.render([doc1, doc2], style='dep', page=True)

svg = displacy.render(doc1, style='dep')
output_path = Path('/images/sentence.svg')
output_path.open('w', encoding='utf-8').write(svg)