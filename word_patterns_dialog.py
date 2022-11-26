from PyQt6.QtWidgets import QDialog, QTableWidgetItem
from PyQt6.uic import loadUi

import util.cipher_analysis

class WordPatternsDialog(QDialog):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        loadUi("ui/WordPatternsDialogUI.ui", self)

        self.text = text
        self.wordanalyzer = util.cipher_analysis.WordAnalyzer(self.text)

    def displayData(self, encoder):
        words = self.wordanalyzer.getWords()
        charpatterns = self.wordanalyzer.getLetterPatterns(encoder)
        olfpatterns = self.wordanalyzer.getRawObsFreqPatterns()
        elfpatterns = self.wordanalyzer.getRawExpFreqPatterns()
        golfpatterns = self.wordanalyzer.getGenFreqPatterns(olfpatterns)
        gelfpatterns = self.wordanalyzer.getGenFreqPatterns(elfpatterns)

        self.wordTable.setRowCount(len(words))
        i = 0
        for word in words:
            self.wordTable.setItem(i, 0, QTableWidgetItem(word))
            i += 1
        i = 0
        for pattern in charpatterns:
            self.wordTable.setItem(i, 1, QTableWidgetItem(pattern))
            i += 1
        i = 0
        for pattern in olfpatterns:
            self.wordTable.setItem(i, 2, QTableWidgetItem(pattern))
            i += 1
        i = 0
        for pattern in elfpatterns:
            self.wordTable.setItem(i, 3, QTableWidgetItem(pattern))
            i += 1
        i = 0
        for pattern in golfpatterns:
            self.wordTable.setItem(i, 4, QTableWidgetItem(pattern))
            i += 1
        i = 0
        for pattern in gelfpatterns:
            self.wordTable.setItem(i, 5, QTableWidgetItem(pattern))
            i += 1