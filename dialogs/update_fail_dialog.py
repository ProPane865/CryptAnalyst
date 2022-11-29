from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi

import util.data_storage

class UpdateFailDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi(util.data_storage.resource_path("ui/UpdateFailureUI.ui"), self)