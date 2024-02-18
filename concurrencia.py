import sys
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
from datetime import datetime, timedelta

#Funcion para imprimir el tiempo actual en el label_actual y repetirlo
def display_time():
    captura_tiempo = datetime.now()
    label_actual.setText("Current Time: " + captura_tiempo.strftime("%H:%M:%S"))
    QTimer.singleShot(1000, display_time)  #Repetir la funcion cada segundo para correseguido

#Funcion para imprimir el tiempo actual mas 4 horas en el label_futuro y repetirlo
def display_time_futuro():
    captura_tiempo = datetime.now()
    label_futuro.setText("Tiempo actual más 4 horas: " + (captura_tiempo + timedelta(hours=4)).strftime("%H:%M:%S"))
    QTimer.singleShot(1000, display_time_futuro) #Repetir la funcion cada segundo para correseguido

#Preparando el GUI
app = QApplication(sys.argv)
window = QMainWindow()
window.setGeometry(100, 100, 300, 100)

central_widget = QWidget()
window.setCentralWidget(central_widget)

#Creando el espaciadpo
layout = QVBoxLayout()

label_actual = QLabel("Tiempo actual: ")
layout.addWidget(label_actual)

label_futuro = QLabel("Tiempo actual más 4 horas: ")
layout.addWidget(label_futuro)

central_widget.setLayout(layout)

#Thread que maneja el label y el contador de tirmpo futuro
thread_futuro = threading.Thread(target=display_time_futuro())
thread_futuro.daemon = True
thread_futuro.start()

#Thread que maneja el label y el contador de tiempo actual
thread_presente = threading.Thread(target=display_time())
thread_presente.daemon = True
thread_presente.start()

window.show()
sys.exit(app.exec_())
