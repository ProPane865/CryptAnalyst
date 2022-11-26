import sys

from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi

import util.cipher_encoding
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

        self.encodeButton.clicked.connect(self.encode)
        self.actionLetter_Frequency.triggered.connect(self.openLetterFrequencyDialog)
        self.actionWord_Patterns.triggered.connect(self.openWordPatternsDialog)
        self.actionAbout_CryptAnalyst.triggered.connect(self.openAboutCADialog)

    def getPlaintext(self):
        return self.plaintextEdit.toPlainText()

    def openLetterFrequencyDialog(self):
        self.lfd = letter_frequency_dialog.LetterFrequencyDialog(self.getPlaintext().upper(), self.encoder.getKey())
        self.lfd.exec()

    def openWordPatternsDialog(self):
        self.wpd = word_patterns_dialog.WordPatternsDialog(self.getPlaintext())
        self.wpd.displayData(self.encoder)

        self.wpd.exec()

    def openKeyCreatorDialog(self):
        self.kcd = key_creator_dialog.KeyCreatorDialog()
        self.kcd.exec()

    def openAboutCADialog(self):
        self.acad = about_CA_dialog.AboutCADialog()
        self.acad.exec()

    def encode(self):
        self.encoder = util.cipher_encoding.Encoder(self.getPlaintext().upper())
        if self.keyType.currentText() != "<Key>" and self.cipherType.currentText() != "<Cipher Type>":
            if self.cipherType.currentText() == "Aristocrat":
                if self.keyType.currentText() == "Random":
                    self.encoder.genRandomKey("monoalphasub")
                elif self.keyType.currentText() == "Custom...":
                    self.openKeyCreatorDialog()
                    self.encoder.setKey(self.kcd.getKey())

                ciphertext = self.encoder.encodeAristocrat()

                self.ciphertextEdit.clear()
                self.ciphertextEdit.append(ciphertext)

            elif self.cipherType.currentText() == "Patristocrat":
                if self.keyType.currentText() == "Random":
                    self.encoder.genRandomKey("monoalphasub")
                elif self.keyType.currentText() == "Custom...":
                    self.openKeyCreatorDialog()
                    self.encoder.setKey(self.kcd.getKey())

                ciphertext = self.encoder.encodePatristocrat()

                self.ciphertextEdit.clear()
                self.ciphertextEdit.append(ciphertext)

            elif self.cipherType.currentText() == "Caesar":
                if self.keyType.currentText() == "Random":
                    self.encoder.genRandomKey("caesarsub")
                elif self.keyType.currentText() == "Custom...":
                    self.openKeyCreatorDialog()
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