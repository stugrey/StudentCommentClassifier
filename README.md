# Student Comment Classifier

Classifier of student free text comments from class evaluations. The classifier has been trained on mdoule evaluation data from the University of Strathclyde and the University of Warwick. The classifier is available as a stand alone Python package for you to use, just follow the attached instructions.

If you find this classifier useful, pleae let me know at stuart.grey@strath.ac.uk

For more information on the Student Voice class evaluation system from which this classifer comes, please email stuart@studentvoice.app or visit www.studentvoice.app

# Usage Instructions

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