from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class KeyCreatorDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/KeyCreatorDialogUI.ui", self)

        self.key = {}

    def getKey(self):
        for i in range(26):
            self.key[self.keyTable.item(i, 0).text()] = self.keyTable.item(i, 1).text()
        return self.key