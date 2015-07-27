import random
import os
import string


class Eulagizer(object):
    # See http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/
    def __init__(self, indir=None):
        # cache of all triples
        self.cache = {}

        # list of seeds
        self.seeds = []

        # load corpus if requested
        if indir:
            for filename in os.listdir(indir):
                self.add_to_corpus(os.path.join(indir, filename))

    def run(self, product, website, company, length=500):
        """
        Generates a string containing a random EULA
        for a 'product' made by a 'company'
        that is 'length' words long.
        """
        tokenized_output = self.generate_markov_text(length)
        detokenized_output = self.detokenize(tokenized_output, product, company, website)
        return detokenized_output

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

        # add first two words as seed
        self.seeds.append(words[:2])

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
        # seed
        seed_word, next_word = random.choice(self.seeds)

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
                w1, w2 = self.markov_step(w1, w2)

        # return
        return ' '.join(gen_words)

    def markov_step(self, w1, w2):
        # only take moves that have a next move after
        success = False
        while not success:
            w3 = random.choice(self.cache[(w1, w2)])
            if (w2, w3) in self.cache:
                success = True
        return w2, w3

    def detokenize(self, text, product, company, website):
        """
        Detokenizes text and inserts product and company names.
        Based on tokenization in `parse_corpus.py`
        """
        # replace product and company names and variants, and newlines
        to_replace = [
            ('{{{PRODUCT}}}', product),
            ('{{{PRODUCT_LOWER}}}', product.lower()),
            ('{{{PRODUCT_UPPER}}}', product.upper()),
            ('{{{COMPANY}}}', company),
            ('{{{COMPANY_LOWER}}}', company.lower()),
            ('{{{COMPANY_UPPER}}}', company.upper()),
            ('{{{WEBSITE}}}', website),
            (' {{{NEWLINE}}} ', '\n\n'),
            ('{{{NEWLINE}}}', '\n'),
        ]
        for old, new in to_replace:
            text = string.replace(text, old, new)

        # return
        return text
