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

## License

This software is covered by the MIT License: http://aschn.mit-license.org/

Copyright © 2015 Anna Schneider

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
