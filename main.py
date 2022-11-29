import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi

import util.cipher_encoding
import util.data_storage

import dialogs.letter_frequency_dialog
import dialogs.key_creator_dialog
import dialogs.word_patterns_dialog
import dialogs.about_CA_dialog
import dialogs.update_dialog
import dialogs.update_fail_dialog

import requests

class Application(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi(util.data_storage.resource_path("ui/CryptAnalystUI.ui"), self)

        self.version = [0, 1, 1]
        self.builddate = "28, November 2022"

        self.encoder = util.cipher_encoding.Encoder("")
        self.encoder.setKey({})

        self.datawriter = util.data_storage.DataWriter()
        self.datareader = util.data_storage.DataReader()

        self.encodeButton.clicked.connect(self.encode)
        self.actionLetter_Frequency.triggered.connect(self.openLetterFrequencyDialog)
        self.actionWord_Patterns.triggered.connect(self.openWordPatternsDialog)
        self.actionAbout_CryptAnalyst.triggered.connect(self.openAboutCADialog)
        self.actionImport_Plaintext.triggered.connect(self.importPlaintext)
        self.actionCheck_for_Updates.triggered.connect(self.checkForUpdates)

    def checkForUpdates(self):
        try:
            response = requests.get("https://propane865.netlify.app/software/cryptanalyst/latestversion.txt")
            latest_version_str = response.text.split(".")
            latest_version = [int(n) for n in latest_version_str]

            avail = False

            if (latest_version[0] > self.version[0]):
                avail = True
            elif (latest_version[0] == self.version[0]) and (latest_version[1] > self.version[1]):
                avail = True
            elif (latest_version[0] == self.version[0]) and (latest_version[1] == self.version[1]) and (latest_version[2] > self.version[2]):
                avail = True
            else:
                avail = False

            if avail:
                self.openUpdateDialog("A new update for CryptAnalyst is now available!", self.getCurrentVersion(), response.text)
            else:
                self.openUpdateDialog("No new update for CryptAnalyst is available.", self.getCurrentVersion(), response.text)
        except requests.exceptions.ConnectionError:
            self.openUpdateFailDialog()

    def getCurrentVersion(self):
        return ".".join([str(n) for n in self.version])
    
    def getBuildDate(self):
        return self.builddate

    def getPlaintext(self):
        return self.plaintextEdit.toPlainText()
    
    def openUpdateDialog(self, text, cv, lv):
        self.upd = dialogs.update_dialog.UpdateDialog()
        self.upd.title.setText(text)

        self.upd.currentVersion.clear()
        self.upd.latestVersion.clear()

        self.upd.currentVersion.insert(cv)
        self.upd.latestVersion.insert(lv)

        self.upd.exec()

    def openUpdateFailDialog(self):
        self.updf = dialogs.update_fail_dialog.UpdateFailDialog()
        self.updf.exec()

    def openLetterFrequencyDialog(self):
        self.lfd = dialogs.letter_frequency_dialog.LetterFrequencyDialog(self.getPlaintext().upper(), self.encoder.getKey(), self.datawriter)
        self.lfd.exec()

    def openWordPatternsDialog(self):
        self.wpd = dialogs.word_patterns_dialog.WordPatternsDialog(self.getPlaintext(), self.datawriter)
        self.wpd.displayData(self.encoder)

        self.wpd.exec()

    def openKeyCreatorDialogMAS(self):
        self.kcd = dialogs.key_creator_dialog.KeyCreatorDialogMAS()
        self.kcd.exec()

    def openKeyCreatorDialogCS(self):
        self.kcd = dialogs.key_creator_dialog.KeyCreatorDialogCS()
        self.kcd.exec()

    def openKeyCreatorDialogA(self):
        self.kcd = dialogs.key_creator_dialog.KeyCreatorDialogA()
        self.kcd.exec()

    def openKeyCreatorDialogAT(self):
        self.kcd = dialogs.key_creator_dialog.KeyCreatorDialogAT()
        self.kcd.exec()

    def openAboutCADialog(self):
        self.acad = dialogs.about_CA_dialog.AboutCADialog()
        self.acad.version.setText(f"Version: {self.getCurrentVersion()}")
        self.acad.buildDate.setText(f"Build Date: {self.getBuildDate()}")
        self.acad.exec()

    def importPlaintext(self):
        self.plaintextEdit.clear()
        self.plaintextEdit.append(self.datareader.dialogGetDataFile())

    def encodeAristocrat(self):
        if self.keyType.currentText() == "Random":
            self.encoder.genRandomKey("monoalphasub")
        elif self.keyType.currentText() == "Custom...":
            self.openKeyCreatorDialogMAS()
            self.encoder.setKey(self.kcd.getKey())

        ciphertext = self.encoder.encodeWithSpaces()

        self.ciphertextEdit.clear()
        self.ciphertextEdit.append(ciphertext)

    def encodePatristocrat(self):
        if self.keyType.currentText() == "Random":
            self.encoder.genRandomKey("monoalphasub")
        elif self.keyType.currentText() == "Custom...":
            self.openKeyCreatorDialogMAS()
            self.encoder.setKey(self.kcd.getKey())

        ciphertext = self.encoder.encodeWithoutSpaces()

        self.ciphertextEdit.clear()
        self.ciphertextEdit.append(ciphertext)

    def encodeCaesar(self):
        if self.keyType.currentText() == "Random":
            self.encoder.genRandomKey("caesarsub")
        elif self.keyType.currentText() == "Custom...":
            self.openKeyCreatorDialogCS()
            self.encoder.setKey(self.kcd.getKey())

        ciphertext = self.encoder.encodeWithSpaces()

        self.ciphertextEdit.clear()
        self.ciphertextEdit.append(ciphertext)

    def encodeAffine(self):
        if self.keyType.currentText() == "Random":
            self.encoder.genRandomKey("affine")
        elif self.keyType.currentText() == "Custom...":
            self.openKeyCreatorDialogA()
            self.encoder.setKey(self.kcd.getKey())

        ciphertext = self.encoder.encodeWithSpaces()

        self.ciphertextEdit.clear()
        self.ciphertextEdit.append(ciphertext)

    def encodeAtbash(self):
        if self.keyType.currentText() == "Random":
            self.encoder.genRandomKey("atbash")
        elif self.keyType.currentText() == "Custom...":
            self.openKeyCreatorDialogAT()
            self.encoder.genRandomKey("atbash")

        ciphertext = self.encoder.encodeWithSpaces()

        self.ciphertextEdit.clear()
        self.ciphertextEdit.append(ciphertext)

    def encode(self):
        self.encoder = util.cipher_encoding.Encoder(self.getPlaintext().upper())
        if self.keyType.currentText() != "<Key>" and self.cipherType.currentText() != "<Cipher Type>":
            try:
                if self.cipherType.currentText() == "Aristocrat":
                    self.encodeAristocrat()
                elif self.cipherType.currentText() == "Patristocrat":
                    self.encodePatristocrat()
                elif self.cipherType.currentText() == "Caesar":
                    self.encodeCaesar()
                elif self.cipherType.currentText() == "Affine":
                    self.encodeAffine()
                elif self.cipherType.currentText() == "Atbash":
                    self.encodeAtbash()
            except Exception:
                self.ciphertextEdit.clear()
                self.ciphertextEdit.append("An error has occurred while attempting to encode (make sure the inputs are valid).")
        else:
            self.ciphertextEdit.clear()
            self.ciphertextEdit.append("Please select a key type or cipher type from the corresponding dropdown(s).")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)

    frame = Application()
    frame.show()
    
    sys.exit(app.exec())