from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QDialog
from PyQt5.uic import loadUi

import csv

import util.cipher_analysis
import frequency_data_dialog

class LetterFrequencyDialog(QDialog):
    def __init__(self, plaintext, key, parent=None):
        super().__init__(parent)
        loadUi("ui/LetterFrequencyDialogUI.ui", self)

        self.plaintext = plaintext
        self.key = key

        self.lfanalyzer = util.cipher_analysis.LFAnalyzer(self.plaintext)

        self.calculateButton.clicked.connect(self.showLetterFrequency)
        self.analyzeButton.clicked.connect(self.showFrequencyData)
        self.saveButton.clicked.connect(self.saveLetterFrequency)

        for i in range(26):
            try:
                self.freqTable.setItem(i, 1, QTableWidgetItem(key[str(chr(ord("A") + i))]))
            except KeyError:
                pass

    def showFrequencyData(self):
        self.fdd = frequency_data_dialog.FrequencyDataDialog(self.lfanalyzer)
        self.fdd.exec()

    def saveLetterFrequency(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        dialog.setNameFilter("CSV files (*.csv)")
        filenames = []

        if dialog.exec():
            filenames = dialog.selectedFiles()

        for file in filenames:
            with open(file, "w+") as f:
                fw = csv.writer(f)
                fw.writerow(["Plaintext", "Ciphertext", "Frequency"])
                for i in range(26):
                    try:
                        fw.writerow([self.freqTable.item(i, 0).text(), self.freqTable.item(i, 1).text(), self.freqTable.item(i, 2).text()])
                    except AttributeError:
                        pass

    def showLetterFrequency(self):
        frequency = self.lfanalyzer.getLetterFrequency()

        for i in range(26):
            self.freqTable.setItem(i, 2, QTableWidgetItem(str(frequency[str(chr(ord("A") + i))])))