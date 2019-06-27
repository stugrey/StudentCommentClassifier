# Student Comment Classifier

Classifier of student free text comments from class evaluations. The classifier has been trained on mdoule evaluation data from the University of Strathclyde and the University of Warwick. The classifier is available as a stand alone Python package for you to use, just follow the attached instructions.

If you find this classifier useful, pleae let me know at stuart.grey@strath.ac.uk

For more information on the Student Voice class evaluation system from which this classifer comes, please email stuart@studentvoice.app or visit www.studentvoice.app

# Usage Instructions

1. Clone the repository

2. In terminal,

```
pip install ./dist/en_model-0.0.1.tar.gz
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

## Usage with data in a text file

To apply the model to a set of comments in a text file, the following code can be used:

```
import spacy

spacy.info('en_model')
nlp = spacy.load('en_model')

text_file = open("input.txt", "r")
TEXTS = text_file.readlines()
text_file.close()

f = open("output.txt", "w+")
for text in TEXTS:
        doc = nlp(text)
        f.write(text + " " + str(doc.cats)+"\n")
        
f.close()
```

This will read in a file from the working directory, which needs to be formatted as follows:

```
"This is my first comment",
"This is the last comment",
```

The output would then be:

```
"This is my first comment",
 {'ASSESSMENT': 0.029826432466506958, 'ESTATES': 0.0039027987513691187, 'TUTORIALS': 4.539787187241018e-05}
"This is the last comment", {'ASSESSMENT': 0.14680345356464386, 'ESTATES': 0.015312162227928638, 'TUTORIALS': 0.000509649864397943}
```
# Model Training Logs

en-model-0.0.1

```
Using 20% of examples (600) for evaluation
Using 100% of remaining examples (2400) for training
Dropout: 0.2  Batch size: 10  Iterations: 10  

#            LOSS         F-SCORE      ACCURACY  
01           0.323        0.000        0.873                                                                                               
02           0.265        0.051        0.875                                                                                               
03           0.240        0.365        0.890                                                                                               
04           0.214        0.491        0.903                                                                                               
05           0.170        0.656        0.927                                                                                               
06           0.139        0.732        0.937                                                                                               
07           0.113        0.765        0.947                                                                                               
08           0.096        0.789        0.950                                                                                               
09           0.102        0.761        0.943                                                                                               
10           0.089        0.766        0.945                                                                                               

accept   accept   56 
accept   reject   10 
reject   reject   514
reject   accept   20 

Correct     570
Incorrect   30

Baseline    0.29              
Precision   0.85              
Recall      0.74              
F-score     0.79              
Accuracy    0.95
```

