from mrjob.job import MRJob
from datetime import datetime
class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        company, price, date = line.split(',')
        yield company, (float(price), date)

    def reducer(self, company, values):
        prices = []
        dates = []
        for price, date  in values:
            prices.append(price)
            dates.append(datetime.fromisoformat(date))
        
        prices = [x for y,x in sorted(zip(dates, prices))]

        if prices == sorted(prices):
            yield company, prices

if __name__ == '__main__':
    MRWordFrequencyCount.run()
