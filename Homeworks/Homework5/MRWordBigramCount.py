
from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")

class MRWordBigramCount(MRJob):

    def mapper(self, _, line):
        lastword=""
        for word in WORD_RE.findall(line):
            yield (lastword.lower(),word.lower(), 1
             lastword=word
                   
    def combiner(self, bigram, counts):
        yield bigram, sum(counts)

    def reducer(self, word, counts):
        yield bigram, sum(counts)


if __name__ == '__main__':
    MRWordBigramCount.run()