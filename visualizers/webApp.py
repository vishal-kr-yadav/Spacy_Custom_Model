import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')

def displacy_service(text):
    doc = nlp(text)
    return displacy.parse_deps(doc)

text = """But Google is starting from behind. The company made a late push
into hardware, and Apple’s Siri, available on iPhones, and Amazon’s Alexa
software, which runs on its Echo and Dot devices, have clear leads in
consumer adoption."""
displacy_service(text)