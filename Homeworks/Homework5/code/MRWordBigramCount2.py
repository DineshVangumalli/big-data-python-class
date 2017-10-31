
from mrjob.job import MRJob
from mrjob.step import MRStep

class MRWordBigramCount2(MRJob):
    
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                  combiner = self.combiner,
                  reducer=self.reducer),
            MRStep(reducer=self.reducer_top10)
        ]

    def mapper(self, _, line):                   # The mapper() method takes a key and a value as args  (in this case, the key is ignored and a single line of text input is the value) 
        line = line.lower().split()              # converts the line to lowercase and splits it on whitespace            
        for words in zip(line, line[1:]):        
            yield list((words[0], words[1])), 1  # yields list of as many key-value pairs as it likes 
            
    def combiner(self, bigram, counts):
        yield bigram, sum(counts)                # Each call to the combiner gets 2 words as the key and a list of 1s as the value. It sums the 1s and outputs the original key and the sum
                               
    def reducer(self, bigram, counts):           # The reduce() method takes a key and an iterator of values and also yields as many key-value pairs as it likes
        yield None, (bigram, sum(counts))
                   
    def reducer_top10(self, _, bigram_count):
        for i in sorted(bigram_count, key=lambda x:x[1], reverse=True)[:10]:
                   yield i

            
if __name__ == '__main__':
    MRWordBigramCount2.run()           # pass control over the command line arguments and execution to mrjob