import random
import os
import string

"""
Usage:

from generator import Markov
gen = Markov()
gen.run('path/to/corpus/dir', 'path/to/output.txt',
        'Extra Fake Co', 500)
"""


class Markov(object):
    # See http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/
    def __init__(self):
        # cache of all triples
        self.cache = {}

    def run(self, indir=None, outfile='EULA.txt',
            company='My Company', website='www.mysite.com', parent='Parent Co',
            length=500):
        """
        Generates a random EULA
        for a company named 'company'
        that is 'length' words long,
        based on the corpus files in directory 'indir',
        and writes the EULA to 'outfile'.
        """
        # load corpus if needed
        if indir:
            for filename in os.listdir(indir):
                self.add_to_corpus(os.path.join(indir, filename))

        # generate and detokenize text
        tokenized_output = self.generate_markov_text(length=length)
        detokenized_output = self.detokenize(tokenized_output, company, parent, website)

        # write output
        with open(outfile, 'w') as f:
            f.write(detokenized_output)

    def add_to_corpus(self, filename):
        # read file
        with open(filename) as f:
            f.seek(0)
            data = f.read()

        # split file contents to words
        words = data.split()

        # create triples and cache
        triples = self.words_to_triples(words)
        self.add_to_cache(triples)

    def words_to_triples(self, words):
        """ Generates triples from the given data string. So if our string were
                "What a lovely day", we'd generate (What, a, lovely) and then
                (a, lovely, day).
        """
        if len(words) < 3:
            return

        for i in range(len(words) - 2):
            yield (words[i], words[i+1], words[i+2])

    def add_to_cache(self, triples):
        for w1, w2, w3 in triples:
            key = (w1, w2)

            # add to cache
            if key in self.cache:
                self.cache[key].append(w3)
            else:
                self.cache[key] = [w3]

    def generate_markov_text(self, length):
        # seed from cache keys
        seed_word, next_word = 'Terms', 'of'

        # set up to generate
        w1, w2 = seed_word, next_word
        gen_words = []
        finished = False

        while not finished:
            # add word
            gen_words.append(w1)

            # check if finished
            if len(gen_words) >= length and w1 == '{{{NEWLINE}}}':
                finished = True

            # if not finished, run Markov chain
            else:
                w1, w2 = w2, random.choice(self.cache[(w1, w2)])

        # return
        return ' '.join(gen_words)

    def detokenize(self, text, company, parent, website):
        """
        Detokenizes text and inserts company name.
        Based on tokenization in `parse_corpus.py`
        """
        # replace company name and variants, and newlines
        to_replace = [
            ('{{{COMPANY}}}', company),
            ('{{{WEBSITE}}}', website),
            ('{{{PARENT_CO}}}', parent),
            ('{{{COMPANY_LOWER}}}', company.lower()),
            ('{{{COMPANY_UPPER}}}', company.upper()),
            (' {{{NEWLINE}}} ', '\n\n'),
            ('{{{NEWLINE}}}', '\n'),
        ]
        for old, new in to_replace:
            text = string.replace(text, old, new)

        # return
        return text
