from PyQt6.QtWidgets import QFileDialog, QTableWidget

import csv

class DataWriter():
    def __init__(self):
        pass

    def dialogSaveCSV(self, table: QTableWidget, columns: list):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        dialog.setNameFilter("CSV files (*.csv)")
        filenames = []

        if dialog.exec():
            filenames = dialog.selectedFiles()

        for file in filenames:
            with open(f"{file}.csv", "w+") as f:
                fw = csv.writer(f)
                fw.writerow(columns)
                for i in range(table.rowCount()):
                    row = []
                    for j in range(table.columnCount()):
                        try:
                            row.append(table.item(i, j).text())
                        except AttributeError:
                            row.append("")
                    fw.writerow(row)