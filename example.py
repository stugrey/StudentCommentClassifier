import spacy

nlp = spacy.load('en_model')
doc = nlp(u"The exam was far too hard")

# Text classification
print(doc.cats)