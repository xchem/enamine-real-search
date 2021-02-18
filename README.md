# enamine-real-search
Wrapper around similarity and substructure searching functionality on enaminestore.com

## Installation
``pip install ers``

## Usage

To do a similarity search:

```python
from search import EnamineSession

session = EnamineSession()
similarity_results = session.similarity_search(smiles='C1=CC=C(C=C1)O', threshold=0.1)
```

To do a substructure search:

```python
from search import EnamineSession

session = EnamineSession()
substructure_results = session.substructure_search(smiles='C1=CC=C(C=C1)O')
```

## Output

For both types of search, a list of dictionaries our output, with one dictionary in the list for each molecule that is a match from the search. 
It's super easy to turn these into a dataframe with pandas and view the results as a table (there's a full example in ``example.ipynb``.

The keys in the molecule dictionaries and their meanings are:
- ``vendorId`` - the vendor ID that enamine uses (use this if asking for a quote from Enamine)
- ``smiles`` - the smiles string of the matching molecule
- ``fsp3`` - the fraction of sp3 carbon atoms
- ``hac`` - the heavy atom count
- ``hba`` - the number of hydrogen-bond acceptors
- ``hbd`` - the number of hydrogen bond donors
- ``logP`` - the log of the partition coefficient between octanol and water (hydrophobicity)
- ``mw`` - molecular weight
- ``rotb`` - the number of rotatable bonds
- ``tpsa`` - topological polar surface area
- ``priceCategory`` - S=simple, M=Advanced (check with Enamine)

And for the similarity search, there is an additional field for ``similarity``, where a value of to 1 indicates
the molecule is an exact match to the input molecule (probably not inc. tautomers etc.) and 0 is not a match at all.
