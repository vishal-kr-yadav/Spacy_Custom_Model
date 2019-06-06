import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')
text = """But Google is starting from behind. The company made a late push
into hardware, and Apple’s Siri, available on iPhones, and Amazon’s Alexa
software, which runs on its Echo and Dot devices, have clear leads in
consumer adoption."""
doc = nlp(text)
html = displacy.render([doc], style='ent', page=True)
print(html)
