import sys

from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi

import util.cipher_encoding
import util.data_storage

import letter_frequency_dialog
import key_creator_dialog
import word_patterns_dialog
import about_CA_dialog

class ApplicationFrame(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/CryptAnalystUI.ui", self)

        self.encoder = util.cipher_encoding.Encoder("")
        self.encoder.setKey({})

        self.datawriter = util.data_storage.DataWriter()
        self.datareader = util.data_storage.DataReader()

        self.encodeButton.clicked.connect(self.encode)
        self.actionLetter_Frequency.triggered.connect(self.openLetterFrequencyDialog)
        self.actionWord_Patterns.triggered.connect(self.openWordPatternsDialog)
        self.actionAbout_CryptAnalyst.triggered.connect(self.openAboutCADialog)
        self.actionImport_Plaintext.triggered.connect(self.importPlaintext)

    def getPlaintext(self):
        return self.plaintextEdit.toPlainText()

    def openLetterFrequencyDialog(self):
        self.lfd = letter_frequency_dialog.LetterFrequencyDialog(self.getPlaintext().upper(), self.encoder.getKey(), self.datawriter)
        self.lfd.exec()

    def openWordPatternsDialog(self):
        self.wpd = word_patterns_dialog.WordPatternsDialog(self.getPlaintext(), self.datawriter)
        self.wpd.displayData(self.encoder)

        self.wpd.exec()

    def openKeyCreatorDialogMAS(self):
        self.kcd = key_creator_dialog.KeyCreatorDialogMAS()
        self.kcd.exec()

    def openKeyCreatorDialogCS(self):
        self.kcd = key_creator_dialog.KeyCreatorDialogCS()
        self.kcd.exec()

    def openAboutCADialog(self):
        self.acad = about_CA_dialog.AboutCADialog()
        self.acad.exec()

    def importPlaintext(self):
        self.plaintextEdit.clear()
        self.plaintextEdit.append(self.datareader.dialogGetDataFile())

    def encode(self):
        self.encoder = util.cipher_encoding.Encoder(self.getPlaintext().upper())
        if self.keyType.currentText() != "<Key>" and self.cipherType.currentText() != "<Cipher Type>":
            if self.cipherType.currentText() == "Aristocrat":
                if self.keyType.currentText() == "Random":
                    self.encoder.genRandomKey("monoalphasub")
                elif self.keyType.currentText() == "Custom...":
                    self.openKeyCreatorDialogMAS()
                    self.encoder.setKey(self.kcd.getKey())

                ciphertext = self.encoder.encodeAristocrat()

                self.ciphertextEdit.clear()
                self.ciphertextEdit.append(ciphertext)

            elif self.cipherType.currentText() == "Patristocrat":
                if self.keyType.currentText() == "Random":
                    self.encoder.genRandomKey("monoalphasub")
                elif self.keyType.currentText() == "Custom...":
                    self.openKeyCreatorDialogMAS()
                    self.encoder.setKey(self.kcd.getKey())

                ciphertext = self.encoder.encodePatristocrat()

                self.ciphertextEdit.clear()
                self.ciphertextEdit.append(ciphertext)

            elif self.cipherType.currentText() == "Caesar":
                if self.keyType.currentText() == "Random":
                    self.encoder.genRandomKey("caesarsub")
                elif self.keyType.currentText() == "Custom...":
                    self.openKeyCreatorDialogCS()
                    self.encoder.setKey(self.kcd.getKey())

                ciphertext = self.encoder.encodeAristocrat()

                self.ciphertextEdit.clear()
                self.ciphertextEdit.append(ciphertext)
        else:
            self.ciphertextEdit.clear()
            self.ciphertextEdit.append("Please select a key type or cipher type from the corresponding dropdown(s).")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)

    frame = ApplicationFrame()
    frame.show()
    
    sys.exit(app.exec())