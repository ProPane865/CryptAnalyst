from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi

class KeyCreatorDialogMAS(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/KeyCreatorDialogMASUI.ui", self)

        self.key = {}

    def getKey(self):
        for i in range(26):
            self.key[self.keyTable.item(i, 0).text()] = self.keyTable.item(i, 1).text()
        return self.key
    
class KeyCreatorDialogCS(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/KeyCreatorDialogCSUI.ui", self)

        self.key = {}

    def getKey(self):
        s = int(self.shiftAmount.text()) % 26
        x = lambda c: ord(c) - 65

        for i in range(26):
            char = ((x(str(chr(ord("A") + i)))) + s) % 26
            self.key[str(chr(ord("A") + i))] = chr(char + 65)

        return self.key
    
class KeyCreatorDialogA(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/KeyCreatorDialogAUI.ui", self)

        self.key = {}

    def getKey(self):
        a = int(self.a.text())
        b = int(self.b.text())
        x = lambda c: ord(c) - 65

        for i in range(26):
            char = ((a * x(str(chr(ord("A") + i)))) + b) % 26
            self.key[str(chr(ord("A") + i))] = chr(char + 65)

        return self.key

class KeyCreatorDialogAT(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/KeyCreatorDialogATUI.ui", self)

        self.key = {}

    def getKey(self):
        pass