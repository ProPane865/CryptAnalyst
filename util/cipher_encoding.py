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
    
        elif keyType == "caesarsub":
            shift = random.randint(1, 25)

            for i in range(26):
                if (ord("A") + i + shift) > 90:
                    char = str(chr(ord("A") + i + shift - 26))
                else:
                    char = str(chr(ord("A") + i + shift))
                chardict[str(chr(ord("A") + i))] = char

        self.key = chardict
    
    def getKey(self):
        return self.key

    def setKey(self, keydict):
        self.key = keydict

    def encodeAristocrat(self):
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

    def encodePatristocrat(self):
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