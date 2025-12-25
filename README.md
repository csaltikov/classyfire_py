# Introduction:
Python API to interface with Classyfire, for classifying metabolomics data.

Use pubchem.py script for converting chemical names into InchIkey

Use classyfire.py script to submit InchIKey and returing possible classifications

# Usage:
## For single compounds or lists:
```aiignore
from classyfire import classyfire, pubchem

compound = "pyruvate"
inchikey = get_inchikey(compound)
print(inchikey)
>>> ['LCTONWCANYUPML-UHFFFAOYSA-M']


compounds = ["pyruvate", "fumarate", "succinate", "foobar"]
results = batch_get(compounds_)
print(res)
>>> ['LCTONWCANYUPML-UHFFFAOYSA-M', 'VZCYOOQTPOCHFL-OWOJBTEDSA-L', 'KDYFGRWQOYBRFD-UHFFFAOYSA-L', None]
```
