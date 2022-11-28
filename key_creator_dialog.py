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
        shift = int(self.shiftAmount.text()) % 26

        for i in range(26):
            if (ord("A") + i + shift) > 90:
                char = str(chr(ord("A") + i + shift - 26))
            else:
                char = str(chr(ord("A") + i + shift))
            self.key[str(chr(ord("A") + i))] = char

        return self.key