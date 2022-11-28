from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QFileDialog
from PyQt6.uic import loadUi

import util.cipher_analysis

class WordPatternsDialog(QDialog):
    def __init__(self, text, datawriter, parent=None):
        super().__init__(parent)
        loadUi("ui/WordPatternsDialogUI.ui", self)

        self.text = text
        self.wordanalyzer = util.cipher_analysis.WordAnalyzer(self.text)

        self.datawriter = datawriter

        self.saveButton.clicked.connect(self.saveData)

    def displayData(self, encoder):
        words = self.wordanalyzer.getWords()
        charpatterns = self.wordanalyzer.getLetterPatterns(encoder)
        olfpatterns = self.wordanalyzer.getRawObsFreqPatterns()
        elfpatterns = self.wordanalyzer.getRawExpFreqPatterns()
        golfpatterns = self.wordanalyzer.getGenFreqPatterns(olfpatterns)
        gelfpatterns = self.wordanalyzer.getGenFreqPatterns(elfpatterns)

        tabledata = [words, charpatterns, olfpatterns, elfpatterns, golfpatterns, gelfpatterns]

        rowsCount = len(words)
        columnsCount = len(tabledata)

        self.wordTable.setRowCount(rowsCount)

        for i in range(rowsCount):
            for j in range(columnsCount):
                self.wordTable.setItem(i, j, QTableWidgetItem(tabledata[j][i]))

    def saveData(self):
        data = self.datawriter.getTableData(self.wordTable, ["Word", "C-Text Pattern", "Obs. LF Pattern", "Exp. LF Pattern", "GObs. LF Pattern", "GExp. LF Pattern"])
        self.datawriter.dialogSaveCSV(data)
