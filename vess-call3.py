import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class MainPage(QDialog):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('HomePage.ui', self)
        self.pushButton.clicked.connect(self.takeText)
        self.fillCombobox()

    def fillCombobox(self):
        gender = ["M", "W"]
        self.comboBox.addItems(gender)

    def takeText(self):
        gender = self.comboBox.currentText()
        heigh = int(self.plainTextEdit.toPlainText())
        if gender == "M":
            r = int(((heigh * 4 / 2.54) - 128) * 0.453)
        elif gender == "W":
            r = int(((heigh * 3.5 / 2.54) - 108) * 0.453)

        self.textEdit.setText(str(r))


if __name__ == "__main__":
    app=QApplication(sys.argv)
    widget=MainPage()
    widget.show()
    sys.exit(app.exec_())
