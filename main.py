# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from janela_principal import Ui_MainWindow
from janela_secundaria import Ui_OtherWindow

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Janelas com PyQt')

        self.button_principal = QPushButton('Abrir Janela Secundária', self)
        self.button_principal.setGeometry(150, 150, 200, 50)
        self.button_principal.clicked.connect(self.abrir_janela_secundaria)

    def abrir_janela_secundaria(self):
        self.janela_secundaria = Ui_OtherWindow()
        self.janela_secundaria.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = App()
    mainWindow.show()
    sys.exit(app.exec_())
