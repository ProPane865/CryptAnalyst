from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi

class UpdateDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/UpdateAvailableUI.ui", self)