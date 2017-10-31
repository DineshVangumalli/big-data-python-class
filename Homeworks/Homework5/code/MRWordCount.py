from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")


class MRWordCount(MRJob):
    
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                  combiner=self.combiner,
                  reducer=self.reducer),
            MRStep(reducer=self.reducer_top10)
        ]
    

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield word.lower(), 1

    def combiner(self, word, counts):
        yield word, sum(counts)

    def reducer(self, word, counts):
        yield word, sum(counts)
        
    def reducer_top10(self, _, count):
        for i in sorted(count, key=lambda x:x[1], reverse=True)[:10]:
                   yield i


if __name__ == '__main__':
    MRWordCount.run()