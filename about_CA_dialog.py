from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

class AboutCADialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/AboutCADialogUI.ui", self)