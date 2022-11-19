from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import loadUi

class FrequencyDataDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/FrequencyDataDialogUI.ui", self)