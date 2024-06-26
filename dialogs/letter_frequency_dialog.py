from PyQt6.QtWidgets import QTableWidgetItem, QFileDialog, QDialog
from PyQt6.uic import loadUi

import util.cipher_analysis
import util.data_storage
import dialogs.frequency_data_dialog

class LetterFrequencyDialog(QDialog):
    def __init__(self, plaintext, key, datawriter, parent=None):
        super().__init__(parent)
        loadUi(util.data_storage.resource_path("ui/LetterFrequencyDialogUI.ui"), self)

        self.plaintext = plaintext
        self.key = key

        self.lfanalyzer = util.cipher_analysis.LFAnalyzer(self.plaintext)
        self.showLetterFrequency()

        self.datawriter = datawriter

        self.analyzeButton.clicked.connect(self.showFrequencyData)
        self.saveButton.clicked.connect(self.saveLetterFrequency)

        for i in range(26):
            try:
                self.freqTable.setItem(i, 1, QTableWidgetItem(key[str(chr(ord("A") + i))]))
            except KeyError:
                pass

    def showFrequencyData(self):
        self.fdd = dialogs.frequency_data_dialog.FrequencyDataDialog(self.lfanalyzer)
        self.fdd.exec()

    def saveLetterFrequency(self):
        data = self.datawriter.getTableData(self.freqTable, ["Plaintext", "Ciphertext", "Frequency"])
        self.datawriter.dialogSaveCSV(data)

    def showLetterFrequency(self):
        frequency = self.lfanalyzer.getLetterFrequency()

        for i in range(26):
            self.freqTable.setItem(i, 2, QTableWidgetItem(str(frequency[str(chr(ord("A") + i))])))