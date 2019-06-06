import spacy
nlp = spacy.load('customModel_complete_test')
# text = 'Every year, around the 1st of January through April 15th every individual and or business is expected to file an income tax return with the IRS.'
text = '         IRS'
doc = nlp(text)
print("Entities->", [(ent.text, ent.label_) for ent in doc.ents])
