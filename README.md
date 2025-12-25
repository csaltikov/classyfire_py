# Introduction:
Python API to interface with Classyfire, for classifying metabolomics data.

Use pubchem.py script for converting chemical names into InchIkey

Use classyfire.py script to submit InchIKey and returing possible classifications

# Usage:
## Get InchIKey for single compounds or lists:
```aiignore
from classyfire import pubchem

compound = "pyruvate"
inchikey = pubchem.get_inchikey(compound)
print(inchikey)
```
returns in list form
```
>>> ['LCTONWCANYUPML-UHFFFAOYSA-M']
```
```
compounds = ["pyruvate", "fumarate", "succinate", "foobar"]
results = pubchem.batch_get(compounds_)
print(res)
```

```
>>> ['LCTONWCANYUPML-UHFFFAOYSA-M', 'VZCYOOQTPOCHFL-OWOJBTEDSA-L', 'KDYFGRWQOYBRFD-UHFFFAOYSA-L', None]
```
## Classifying compounds
```aiignore
from classyfire import classyfire
from collections import defaultdict
import pandas as pd

cf = classyfire.ClassyFire()

saved_inchi = defaultdict(list)

inchi_list = [
        "LCTONWCANYUPML-UHFFFAOYSA-M", 
        "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
        "RYYVLZVUVIJVGH-UHFFFAOYSA-N",
        "BSYNRYMUTXBXSQ-UHFFFAOYSA-N",
        "INVALIDKEY-UHFFFAOYSA-N"
        ]

for inchi in inchi_list:
    res = cf.get_entity_classification(inchi)
    if res is not None:
        print(res["class"])
        
        for k, v in res["class"].items():
            saved_inchi[k].append(v)
    
    if res is None:
        print(f"can't classify {inchi}")

classified = pd.DataFrame(saved_inchi)

print(classified.iloc[0])
```
```aiignore
>>> name                                                         Keto acids and derivatives
    description    Organic compounds containing a ketone group and a carboxylic acid group.
    chemont_id                                                            CHEMONTID:0000389
    url                                 http://classyfire.wishartlab.com/tax_nodes/C0000389
    Name: 0, dtype: object
```
### Detailed output for classyfire.Classification()
Save each res to a list and print one item


```aiignore
# pyruvate
res = cf.get_entity_classification("LCTONWCANYUPML-UHFFFAOYSA-M")
print(res)
```
The raw output is a dictionary. Notice the keys, 'kingdom', 'superclass', 'class', 'subclass'
These have the classifications at different levels of classification.
```aiignore
>>>
{'smiles': 'CC(=O)C([O-])=O',
 'inchikey': 'InChIKey=LCTONWCANYUPML-UHFFFAOYSA-M',
 'kingdom': {'name': 'Organic compounds',
  'description': 'Compounds that contain at least one carbon atom, excluding isocyanide/cyanide and their non-hydrocarbyl derivatives, thiophosgene, carbon diselenide, carbon monosulfide, carbon disulfide, carbon subsulfide, carbon monoxide, carbon dioxide, Carbon suboxide, and dicarbon monoxide.',
  'chemont_id': 'CHEMONTID:0000000',
  'url': 'http://classyfire.wishartlab.com/tax_nodes/C0000000'},
 'superclass': {'name': 'Organic acids and derivatives',
  'description': 'Compounds an organic acid or a derivative thereof.',
  'chemont_id': 'CHEMONTID:0000264',
  'url': 'http://classyfire.wishartlab.com/tax_nodes/C0000264'},
 'class': {'name': 'Keto acids and derivatives',
  'description': 'Organic compounds containing a ketone group and a carboxylic acid group.',
  'chemont_id': 'CHEMONTID:0000389',
  'url': 'http://classyfire.wishartlab.com/tax_nodes/C0000389'},
 'subclass': {'name': 'Alpha-keto acids and derivatives',
  'description': 'Organic compounds containing an aldehyde substituted with a keto group on the adjacent carbon.',
  'chemont_id': 'CHEMONTID:0001113',
  'url': 'http://classyfire.wishartlab.com/tax_nodes/C0001113'},
 'intermediate_nodes': [],
 'direct_parent': {'name': 'Alpha-keto acids and derivatives',
  'description': 'Organic compounds containing an aldehyde substituted with a keto group on the adjacent carbon.',
  'chemont_id': 'CHEMONTID:0001113',
  'url': 'http://classyfire.wishartlab.com/tax_nodes/C0001113'},
 'alternative_parents': [{'name': 'Ketones',
   'description': 'Organic compounds  in which a carbonyl group is bonded to two carbon atoms R2C=O (neither R may be a hydrogen atom). Ketones that have one or more alpha-hydrogen atoms undergo keto-enol tautomerization, the tautomer being an enol.',
   'chemont_id': 'CHEMONTID:0000118',
   'url': 'http://classyfire.wishartlab.com/tax_nodes/C0000118'},
  {'name': 'Monocarboxylic acids and derivatives',
   'description': 'Carboxylic acids containing exactly one carboxyl groups.',
   'chemont_id': 'CHEMONTID:0001137',
   'url': 'http://classyfire.wishartlab.com/tax_nodes/C0001137'},
  {'name': 'Carboxylic acids',
   'description': 'Compounds containing a carboxylic acid group with the formula -C(=O)OH.',
   'chemont_id': 'CHEMONTID:0001205',
   'url': 'http://classyfire.wishartlab.com/tax_nodes/C0001205'},
  {'name': 'Organic oxides',
   'description': 'Organic compounds containing an oxide group.',
   'chemont_id': 'CHEMONTID:0003940',
   'url': 'http://classyfire.wishartlab.com/tax_nodes/C0003940'},
  {'name': 'Hydrocarbon derivatives',
   'description': 'Derivatives of hydrocarbons obtained by substituting one or more carbon atoms by an heteroatom. They contain at least one carbon atom and heteroatom.',
   'chemont_id': 'CHEMONTID:0004150',
   'url': 'http://classyfire.wishartlab.com/tax_nodes/C0004150'},
  {'name': 'Organic anions',
   'description': 'Organic compounds that have a negative electric charge.',
   'chemont_id': 'CHEMONTID:0003608',
   'url': 'http://classyfire.wishartlab.com/tax_nodes/C0003608'}],
 'molecular_framework': 'Aliphatic acyclic compounds',
 'substituents': ['Alpha-keto acid',
  'Ketone',
  'Monocarboxylic acid or derivatives',
  'Carboxylic acid',
  'Carboxylic acid derivative',
  'Organic oxygen compound',
  'Organic oxide',
  'Hydrocarbon derivative',
  'Organooxygen compound',
  'Carbonyl group',
  'Organic anion',
  'Aliphatic acyclic compound'],
 'description': 'This compound belongs to the class of organic compounds known as alpha-keto acids and derivatives. These are organic compounds containing an aldehyde substituted with a keto group on the adjacent carbon.',
 'external_descriptors': [{'source': 'CHEBI',
   'source_id': 'CHEBI:15361',
   'annotations': ['2-oxo monocarboxylic acid anion']},
  {'source': 'META CYC',
   'source_id': 'PYRUVATE',
   'annotations': ['a carboxylate', 'a 2-oxo acid']}],
 'ancestors': ['Alpha-keto acids and derivatives',
  'Carbonyl compounds',
  'Carboxylic acids',
  'Carboxylic acids and derivatives',
  'Chemical entities',
  'Hydrocarbon derivatives',
  'Keto acids and derivatives',
  'Ketones',
  'Monocarboxylic acids and derivatives',
  'Organic acids and derivatives',
  'Organic anions',
  'Organic compounds',
  'Organic oxides',
  'Organic oxygen compounds',
  'Organooxygen compounds'],
 'predicted_chebi_terms': ['ketone (CHEBI:17087)',
  'carbonyl compound (CHEBI:36586)',
  'carboxylic acid (CHEBI:33575)',
  'carboxylic acid anion (CHEBI:29067)',
  'organic oxide (CHEBI:25701)',
  'organic molecule (CHEBI:72695)',
  'organic anion (CHEBI:25696)',
  'oxo carboxylic acid (CHEBI:25754)',
  'chemical entity (CHEBI:24431)',
  'oxygen molecular entity (CHEBI:25806)',
  'organic molecular entity (CHEBI:50860)',
  'organooxygen compound (CHEBI:36963)'],
 'predicted_lipidmaps_terms': [],
 'classification_version': '2.1'}
```
