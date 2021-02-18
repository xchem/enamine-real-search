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
