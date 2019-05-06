# StudentCommentClassifier
Classifier of student free text comments from class evaluations

1. Clone the repository

2. In terminal,

pip install ./dist/en_model-1.0.0.tar.gz

3. Use in python script


`import spacy

nlp = spacy.load('en_model')
doc = nlp(u"As New Zealand Courts Tech Talent, Isolation Becomes a Draw")

# Named entities
print([(ent.text, ent.label_) for ent in doc.ents])

# Text classification
print(doc.cats)`