#!/usr/bin/env python

import sys
import string

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
    contents = f.read()

# tokenize company name and variants, and newlines
to_replace = [
    (product, '{{{PRODUCT}}}'),
    (product.lower(), '{{{PRODUCT_LOWER}}}'),
    (product.upper(), '{{{PRODUCT_UPPER}}}'),
    (company, '{{{COMPANY}}}'),
    (company.lower(), '{{{COMPANY_LOWER}}}'),
    (company.upper(), '{{{COMPANY_UPPER}}}'),
    (website, '{{{WEBSITE}}}'),
    ('\n\n', ' {{{NEWLINE}}} '),
    ('\n', ' {{{NEWLINE}}} '),
]
for old, new in to_replace:
    contents = string.replace(contents, old, new)

# write file
with open(outfile, 'w') as f:
    f.write(contents)
