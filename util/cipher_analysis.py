import csv
import sigfig

import util.cipher_encoding
import util.data_storage

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

        with open(util.data_storage.resource_path("data/default_frequencies.csv"), "r") as f:
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

class WordAnalyzer():
    def __init__(self, text):
        self.lfanalyzer = LFAnalyzer(text)
        self.text = text.upper()

    def getWords(self):
        rawwords = self.text.split(" ")
        words = []

        for word in rawwords:
            filtered = filter(lambda x: x in self.lfanalyzer.getLetterFrequency().keys(), word)
            newword = ""

            for x in filtered:
                newword += x
            words.append(newword)
        return words

    def getLetterPatterns(self, encoder: util.cipher_encoding.Encoder):
        patterns = []
        key = encoder.getKey()
        for word in self.getWords():
            pattern = []
            i = 0
            for char in word:
                try:
                    pattern.append(key[char])
                except KeyError:
                    pass
            patterns.append("".join(pattern))
        return patterns

    def getRawObsFreqPatterns(self):
        frequency = self.lfanalyzer.getLetterFrequency()
        patterns = []

        for word in self.getWords():
            pattern = []
            i = 0
            for char in word:
                try:
                    pattern.append(str(frequency[char]))
                except KeyError:
                    pass
            patterns.append(" ".join(pattern))
        return patterns

    def getRawExpFreqPatterns(self):
        frequency = self.lfanalyzer.getDefaultFrequencyPercentage()
        total = self.lfanalyzer.getLetterCount()
        patterns = []

        for word in self.getWords():
            pattern = []
            i = 0
            for char in word:
                try:
                    pattern.append(str(round(frequency[char] * total)))
                except KeyError:
                    pass
            patterns.append(" ".join(pattern))
        return patterns

    def getGenFreqPatterns(self, patterns):
        total = self.lfanalyzer.getLetterCount()
        newpatterns = []

        for pattern in patterns:
            newpattern = []
            frequencies = pattern.split(" ")
            gen_frequencies = {}

            for frequency in frequencies:
                try:
                    i_frequency = int(frequency)
                    if i_frequency / total > 0.08:
                        gen_frequencies[str(i_frequency)] = "H"
                    elif i_frequency / total > 0.05:
                        gen_frequencies[str(i_frequency)] = "M"
                    elif i_frequency / total < 0.05:
                        gen_frequencies[str(i_frequency)] = "L"

                    newpattern.append(gen_frequencies[frequency])
                except ValueError:
                    pass

            newpatterns.append("".join(newpattern))
        return newpatterns