# StudentCommentClassifier
Classifier of student free text comments from class evaluations

1. Clone the repository

2. In terminal,

```
pip install ./dist/en_model-0.0.0.tar.gz
```

3. Use in python script


```
import spacy

nlp = spacy.load('en_model')
doc = nlp(u"The exam was far too hard")

# Text classification
print(doc.cats)
```

4. Results

```
user$ python3 example.py 
{'ASSESSMENT': 0.9972975850105286, 'ESTATES': 0.004103934392333031, 'TUTORIALS': 0.007041135337203741}
```