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


def geo_system(self):
    api_key = keys.api_key

    geo_loc = requests.get(url=f"http://api.openweathermap.org/geo/1.0/direct?q=Brasília,"
                               f" Federal District &limit=5&appid={api_key}")
    geo_loc.raise_for_status()
    geo_data = geo_loc.json()
    self.user_lat = geo_data[0]['lat']
    self.user_long = geo_data[0]["lon"]
    print(self.user_lat, self.user_long)


def weather_system(self):
    weather_key = keys.weather_key
    wheather_endp = "http://api.weatherapi.com/v1/forecast.json"
    wheather_param = {
        "q": (self.user_lat, self.user_long),
        'key': weather_key,
        "days": 7,
        "hour": 16
    }

    weather_connection = requests.get(wheather_endp, params=wheather_param)
    weather_connection.raise_for_status()
    weather_data = weather_connection.json()

    self.seven_days = []
    for i in range(0, 7):
        self.seven_days.append(weather_data['forecast']['forecastday'][i]['day']['condition'])


def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "Previsão do Tempo"))
    self.local_button.setText(_translate("MainWindow", "Buscar localização"))

    data = datetime.datetime.now()
    dia = data.strftime('%m/%d')
    self.dia.setText(_translate("MainWindow", "<html><head/><body><p><span style=\""
                                              " font-size:12pt; font-weight:700; "
                                              f"color:#797979;\">{dia}</span></p></body></html>"))

    self.temp.setText(_translate("MainWindow", "<html><head/><body><p><span style="
                                               " font-size:12pt; font-weight:700;"
                                               " font-style:italic; color:#7a7a7a;\""
                                               ">23°</span></p></body></html>"))
    self.latitude_entry.setPlaceholderText(_translate("MainWindow", "Latitude"))
    self.longitude_entry.setPlaceholderText(_translate("MainWindow", "Longitude"))