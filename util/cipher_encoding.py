import random

class Encoder():
    def __init__(self, plaintext="", key={}):
        self.key = key
        self.plaintext = plaintext

    def genRandomKey(self, keyType):
        charlist = []
        chardict = {}

        if keyType == "monoalphasub":
            for i in range(26):
                charlist.append(str(chr(ord("A") + i)))

            for i in range(26):
                char = str(chr(ord("A") + i))

                while char == str(chr(ord("A") + i)):
                    char = random.choice(charlist)
                
                chardict[str(chr(ord("A") + i))] = char
                del charlist[charlist.index(char)]

        elif keyType == "affine":
            a = random.randint(2, 100)
            b = random.randint(1, 25)
            x = lambda c: ord(c) - 65

            for i in range(26):
                char = ((a * x(str(chr(ord("A") + i)))) + b) % 26
                chardict[str(chr(ord("A") + i))] = chr(char + 65)
    
        elif keyType == "caesarsub":
            s = random.randint(1, 25)
            x = lambda c: ord(c) - 65

            for i in range(26):
                char = ((x(str(chr(ord("A") + i)))) + s) % 26
                chardict[str(chr(ord("A") + i))] = chr(char + 65)

        elif keyType == "atbash":
            a = 25
            b = 25
            x = lambda c: ord(c) - 65

            for i in range(26):
                char = ((a * x(str(chr(ord("A") + i)))) + b) % 26
                chardict[str(chr(ord("A") + i))] = chr(char + 65)

        self.key = chardict
    
    def getKey(self):
        return self.key

    def setKey(self, keydict):
        self.key = keydict

    def encodeWithSpaces(self):
        plaintext_words = self.plaintext.split(" ")
        ciphertext_words = []

        for word in plaintext_words:
            new_word = []
            for char in word:
                if char in self.key.keys():
                    new_word.append(self.key[char])
                else:
                    new_word.append(char)
            new_word = "".join(new_word)
            ciphertext_words.append(new_word)

        ciphertext = " ".join(ciphertext_words)
        return ciphertext

    def encodeWithoutSpaces(self):
        plaintext_words = self.plaintext.split(" ")
        ciphertext_words = []

        for word in plaintext_words:
            new_word = []
            for char in word:
                if char in self.key.keys():
                    new_word.append(self.key[char])
                else:
                    pass
            new_word = "".join(new_word)
            ciphertext_words.append(new_word)

        ciphertext = "".join(ciphertext_words)
        return ciphertext