# eulagizer

A library and corpus for generating a fake End User License Agreement (EULA).

## Clean up the corpus

Raw EULAs have been copied from the web into the `corpus_raw` directory.
(Many came from https://tldrlegal.com; some came from other sources.)
To clean and tokenize them, and put the cleaned corpus in the `corpus` directory, run

```
./parse_corpus.sh
```

## Generate an EULA

In python:

```
# import class
from eulagizer import Eulagizer

# create an instance and load contents of corpus directory
gizer = Eulagizer('corpus')

# optional: add an additional file to corpus
gizer.add_to_corpus('path/to/other.txt')

# generate EULA text string
# feel free to run this repeatedly until you get one you like :)
eula_text = gizer.run(length=500, product='Eulagizer', company='Central Headquarters', website='company.com')

# optional: write to file
with open('path/to/output.txt', 'w') as f:
	f.write(eula_text)
```

This will generate an EULA at least 500 words long with the given parameters.
