#!/usr/bin/env python

import sys
from eulagizer import tokenize

# path to input file
infile = sys.argv[1]

# path to output file
outfile = sys.argv[2]

# product name
product = sys.argv[3]

# website
website = sys.argv[4]

# company
company = sys.argv[5]

# log
print '%s (%s)' % (product, company)

# read file
with open(infile) as f:
    raw = f.read()

# tokenize company name and variants, and newlines
parsed = tokenize(raw, product, company, website)

# write file
with open(outfile, 'w') as f:
    f.write(parsed)
