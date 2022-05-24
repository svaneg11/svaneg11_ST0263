from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        company, price, date = line.split(',')
        yield company, (float(price), date)

    def reducer(self, company, values):
        lowest_date = ''
        highest_date = ''

        lowest_price = 9999999999999
        highest_price = -1
        
        for price, date  in values:
            if price < lowest_price:
                lowest_price = price
                lowest_date = date

            if price > highest_price:
                highest_price = price
                highest_date = date
                
        yield company, (lowest_date, highest_date)

if __name__ == '__main__':
    MRWordFrequencyCount.run()
