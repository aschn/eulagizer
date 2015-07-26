#!/usr/bin/env python

import sys
import string

# path to input file
infile = sys.argv[1]

# path to output file
outfile = sys.argv[2]

# company name
company = sys.argv[3]

# website
website = sys.argv[4]

# parent company, if any
if len(sys.argv) > 5:
    parent = sys.argv[5]
else:
    parent = 'NOPARENT'

# log
print '%s (%s)' % (company, parent)

# read file
with open(infile) as f:
    contents = f.read()

# tokenize company name and variants, and newlines
to_replace = [
    (company, '{{{COMPANY}}}'),
    (website, '{{{WEBSITE}}}'),
    (parent, '{{{PARENT_CO}}}'),
    (company.lower(), '{{{COMPANY_LOWER}}}'),
    (company.upper(), '{{{COMPANY_UPPER}}}'),
    ('\n\n', ' {{{NEWLINE}}} '),
    ('\n', ' {{{NEWLINE}}} '),
]
for old, new in to_replace:
    contents = string.replace(contents, old, new)

# write file
with open(outfile, 'w') as f:
    f.write(contents)
