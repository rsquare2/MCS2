
# NumberSelect.py

"""Iterates through 1-10 & picks a random number each iteration and see if there is a match.
   Creates a List to summarize the number of matches for each of 1-10
   and uses that List to build a dictionary
"""

import random

class Compare:

    def __init__(self,rounds):
        self.rounds = rounds
        self.match = 0
        self.maxMatchesSoFar = 0
        self.overallMatchesList = []
        # self.match0 = 0
        # self.match1 = 0
        # self.match2 = 0
        # self.match3 = 0
        self.fullResults = {}
        self.keyList = []
        self.valueList = []

    def selectRandom(self):
        for round in range(self.rounds):
            self.maxMatches = 0
            for counter in range(1,11): # tests matches for each of 1-10
                pick = random.randint(1,10)
                if counter == pick:
                    self.match += 1 # tracks overall matches over all rounds
                    self.maxMatches +=1 # tracks just matches in individual 1-10 round and resets to zero after round

                if self.maxMatches > self.maxMatchesSoFar:
                    self.maxMatchesSoFar = self.maxMatches
            #
            # if self.maxMatches == 0:
            #    self.match0 += 1
            # if self.maxMatches == 1:
            #        self.match1 += 1
            # if self.maxMatches == 2:
            #        self.match2 += 1
            # if self.maxMatches == 3:
            #    self.match3 += 1

            self.overallMatchesList.append(self.maxMatches)

        for i in self.overallMatchesList:
            if i not in self.fullResults:
                self.fullResults[i] = 1

            else:
                self.fullResults[i] = self.fullResults[i] + 1

        for key in self.fullResults:
            self.keyList.append(key)
            # print('key: ',self.keyList)

        for value in range(len(self.fullResults)):
            self.valueList.append(self.fullResults[value])
            # print('value: ',self.valueList)




        print("Dictionary of Results: ",self.fullResults)
        print("Total Cumulative Matches : ",self.match)
        print("Rounds: ", self.rounds)
        print("Avg Matches Per Round: ", (self.match/self.rounds))
        print("Max Matches in a Round: ", self.maxMatchesSoFar)

        for counter in range(len(self.keyList)):
            print("{0} Match Rounds: {1}%".format(self.keyList[counter],(self.valueList[counter]/self.rounds)*100))

        # print("0 Match Rounds: {0}%".format(int((self.match0/self.rounds)*100)))
        # print("1 Match Rounds: {0}%".format(int((self.match1/self.rounds)*100)))
        # print("2 Match Rounds: {0}%".format(int((self.match2/self.rounds)*100)))
        # print("3 Match Rounds: {0}%".format(int((self.match3/self.rounds)*100)))

def main():
    a = Compare(10000)
    b = a.selectRandom()

if __name__ == '__main__': main()

