import csv
import sigfig

class LFAnalyzer():
    def __init__(self, text):
        self.text = text.upper()

    def getLetterFrequency(self):
        frequency = {}
        for i in range(26):
            frequency[str(chr(ord("A") + i))] = self.text.count(str(chr(ord("A") + i)))
        return frequency

    def getDefaultFrequencyPercentage(self):
        frequency = {}

        with open("data/default_frequencies.csv", "r") as f:
            fr = csv.DictReader(f)
            sum = 4374127904
            
            for row in fr:
                try:
                    frequency[row["Character"]] = float(row["Count"]) / sum
                except TypeError:
                    pass

        return frequency

    def getLetterFrequencyPercentage(self):
        frequency = {}

        for char in self.getLetterFrequency().keys():
            try:
                frequency[char] = float(self.getLetterFrequency()[char]) / self.getLetterCount()
            except ZeroDivisionError:
                frequency[char] = 0

        return frequency

    def getLetterCount(self):
        count = 0

        for i in range(26):
            count += self.text.count(str(chr(ord("A") + i)))
        
        return count

    def findMostCommonLetters(self):
        frequency = self.getLetterFrequency()

        keys = frequency.keys()
        values = frequency.values()

        maxFreq = max(values)

        letters = []

        for key in keys:
            if frequency[key] == maxFreq:
                letters.append(key)

        return letters

    def calculateChiSquare(self):
        observed_frequency = self.getLetterFrequencyPercentage()
        expected_frequency = self.getDefaultFrequencyPercentage()

        chi_square = 0

        for i in range(26):
            o = observed_frequency[str(chr(ord("A") + i))]
            e = expected_frequency[str(chr(ord("A") + i))]

            chi_square += ((o - e)**2) / e
        return sigfig.round(chi_square, sigfigs=3)