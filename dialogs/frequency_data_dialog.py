from PyQt6.QtWidgets import QDialog, QTableWidgetItem
from PyQt6.uic import loadUi

import sigfig
import util.data_storage

class FrequencyDataDialog(QDialog):
    def __init__(self, lfanalyzer, parent=None):
        super().__init__(parent)
        loadUi(util.data_storage.resource_path("ui/FrequencyDataDialogUI.ui"), self)

        self.lfanalyzer = lfanalyzer

        self.totalLetterCount.clear()
        self.totalLetterCount.insert(str(self.lfanalyzer.getLetterCount()))

        self.mostCommonLetter.clear()
        self.mostCommonLetter.insert(str(self.lfanalyzer.findMostCommonLetters()))

        self.expectedFrequencyChiSquare.clear()
        self.expectedFrequencyChiSquare.insert(str(self.lfanalyzer.calculateChiSquare()))

        for i in range(26):
            self.expectedFreqTable.setItem(i, 0, QTableWidgetItem(str(sigfig.round(100 * self.lfanalyzer.getDefaultFrequencyPercentage()[str(chr(ord("A") + i))], sigfigs=3)) + "%"))