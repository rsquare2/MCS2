
# NumberSelect.py

"""Iterates through 1-10 & picks a random number each iteration and checks if there is a match.
   Creates a List to summarize the number of cumulative matches for each of 1-10 over all the rounds
   and uses that List to build a Dictionary.
   Dictionary is then used to build 2 vars: keyList & valueList which are
   used to print the results of the sim
"""

import random

class Compare:

    def __init__(self,rounds):
        self.rounds = rounds
        self.match = 0
        self.maxMatchesSoFar = 0
        self.overallMatchesList = []
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

            self.overallMatchesList.append(self.maxMatches)

        for i in self.overallMatchesList:
            if i not in self.fullResults:
                self.fullResults[i] = 1

            else:
                self.fullResults[i] += 1    # self.fullResults[i] + 1

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
            print("{0} Match Rounds: {1}%".format(self.keyList[counter],
                                                  ((self.valueList[counter]/self.rounds))*100))

        print()
        for counter in range(len(self.keyList)):
            intCalc = int((self.valueList[counter]/self.rounds)*100)
            if intCalc < 1:
                intCalc = "Less than 1% but greater than 0"
            print("{0} Match Rounds (Integer): {1}%".format(self.keyList[counter],intCalc))


def main():
    a = Compare(10000)
    b = a.selectRandom()

if __name__ == '__main__': main()

