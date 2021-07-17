#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import logging
import os.path
import sys
import multiprocessing

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
'''
class LineSentence:
    def __init__(self, source, max_sentence_length=MAX_WORDS_IN_BATCH, limit=None)
        self.source = source
        self.max_sentence_length = max_sentence_length
        self.limit = limit

    def __iter__(self):
        """Iterate through the lines in the source."""
        try:
            # Assume it is a file-like object and try treating it as such
            # Things that don't have seek will trigger an exception
            self.source.seek(0)
            for line in itertools.islice(self.source, self.limit):
                line = utils.to_unicode(line).split()
                i = 0
                while i < len(line):
                    yield line[i: i + self.max_sentence_length]
                    i += self.max_sentence_length
        except AttributeError:
            # If it didn't work like a file, use it as a string filename
            with utils.open(self.source, 'rb') as fin:
                for line in itertools.islice(fin, self.limit):
                    line = utils.to_unicode(line).split()
                    i = 0
                    while i < len(line):
                        yield line[i: i + self.max_sentence_length]
                        i += self.max_sentence_length
'''


if __name__ == '__main__':
    #program = os.path.basename(sys.argv[0])
    #logger = logging.getLogger(program)
 
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
    logging.root.setLevel(level=logging.INFO)
    #logger.info("running %s" % ' '.join(sys.argv))
 
    # check and process input arguments
 
    #if len(sys.argv) < 3:
        #sys.exit(1)
    #inp, outp = sys.argv[1:3]
    inp = 'E:/clean_wiki.txt'
    outp = 'E:/word2vec300.model'
 
    model = Word2Vec(LineSentence(inp), size=300, window=5, min_count=5, negative=15, workers=multiprocessing.cpu_count(), sample = 1e-4)
 
    model.save(outp)