# eulagizer

A library and corpus for generating a fake End User License Agreement (EULA).

## Clean up the corpus

Raw EULAs have been copied from the web into the `corpus_raw` directory.
To clean and tokenize them, and put the cleaned corpus in the `corpus` directory, run

```
./parse_corpus.sh
```

## Generate an EULA

In python:

```
from eulagizer import Eulagizer

gizer = Eulagizer(indir='corpus')

eula_text = gizer.run(length=500,
					  product='Eulagizer',
		  			  company='Central Headquarters',
		  			  website='company.com')
```

This will generate an EULA at least 500 words long with the given parameters.
