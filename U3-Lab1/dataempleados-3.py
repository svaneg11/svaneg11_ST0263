
from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        idemp, sector, salary, year = line.split(',')
        yield idemp, sector

    def reducer(self, idemp, values):
        s = set(values)
        yield idemp, len(s)

if __name__ == '__main__':
    MRWordFrequencyCount.run()
