import numpy  as np
import csv

class Searcher:

    def __init__(self,indexpath):
        self.indexpath = indexpath

    def search(self,queryfeature,limit=10):
        # create the dictionary where keys are image ids and values are its distance metric
        results = {}

        with open("index.csv") as input_file:
            reader = csv.reader(input_file)

            for row in reader:

                # we extract the image features from each row
                # its taken after 1 coz at 0th postion image id is stored

                extracted_features = [float(fets) for fets in row[1:]]
                # we compute chi square distance between extracted and queried features to find similarity
                d = self.chi_square(extracted_features,queryfeature)

                # we store the keys as image ids and values as distance metric
                # in each and every row 0th index contains image id followed by features
                results[row[0]] = d

            input_file.close()

        # we sort the results such that images with minimum distance metric comes first
        # items() returns tuples as (key,value)
        results = sorted([(v,k) for (k,v) in results.items()])

        # sorted returns a list so taking only top limited images
        return results[:limit]

    def chi_square(self,histA,histB,eps = 1e-10):

        # formula is X^2 = sigma((xi-yi)^2)/(xi+yi))

        chi_dist = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)

                    for (a,b) in zip(histA,histB)])
        
        return chi_dist










