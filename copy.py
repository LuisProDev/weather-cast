def __init__(self):
    super().__init__()
    self.data_atual = datetime.datetime.today()

def comando_direito(self):
    _translate = QtCore.QCoreApplication.translate
    self.data_atual += datetime.timedelta(days=1)
    data_formatada = self.data_atual.strftime('%d/%m')
    self.dia.setText(_translate("MainWindow", "<html><head/><body><p><span style=\""
                                              " font-size:12pt; font-weight:700; "
                                              f"color:#797979;\">{data_formatada}</span></p></body></html>"))

def comando_esquerdo(self):
    _translate = QtCore.QCoreApplication.translate
    self.data_atual -= datetime.timedelta(days=1)
    data_formatada = self.data_atual.strftime('%d/%m')
    self.dia.setText(_translate("MainWindow", "<html><head/><body><p><span style=\""
                                              " font-size:12pt; font-weight:700; "
                                              f"color:#797979;\">{data_formatada}</span></p></body></html>"))

data = datetime.datetime.now()
dia = data.strftime('%m/%d')
self.dia.setText(_translate("MainWindow", "<html><head/><body><p><span style=\""
                                          " font-size:12pt; font-weight:700; "
                                          f"color:#797979;\">{dia}</span></p></body></html>"))