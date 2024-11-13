import os
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
                                 "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 254, 236, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                 "}")

        # Establecer el directorio base en relación a la ubicación de main_windows.py
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # Construir rutas relativas a las imágenes desde el directorio base
        image_path_1 = os.path.join(base_dir, "..", "imagenes", "28605e26-ba08-440f-948e-08c676a693ad.jpeg")
        image_path_2 = os.path.join(base_dir, "..", "imagenes", "icons8-music-100.png")

        # Configuración de la ventana central y widgets
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Configuración del primer label (label grande)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 20, 271, 81))
        self.label.setStyleSheet("font: 700 48pt \"Georgia\";\n"
                                 "color: black")
        self.label.setObjectName("label")

        # Configuración de label_4 para la imagen principal
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 371, 576))
        self.label_4.setText("")
        if os.path.exists(image_path_1):
            self.label_4.setPixmap(QtGui.QPixmap(image_path_1))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        # Configuración de label_7 para el ícono
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(400, 20, 80, 80))
        self.label_7.setText("")
        if os.path.exists(image_path_2):
            self.label_7.setPixmap(QtGui.QPixmap(image_path_2))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")

        # Configuración de label_5 para el texto "Carga tu música aquí"
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 140, 191, 31))
        self.label_5.setStyleSheet("font: 700 12pt \"Georgia\";")
        self.label_5.setObjectName("label_5")

        # Configuración de label_6 para el texto "El género de tu música es"
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(390, 290, 221, 31))
        self.label_6.setStyleSheet("font: 700 12pt \"Georgia\";")
        self.label_6.setObjectName("label_6")

        # Configuración del primer botón
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 240, 81, 31))
        self.pushButton.setStyleSheet("font: 700 9pt \"Georgia\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(243, 90, 41);")
        self.pushButton.setObjectName("pushButton")

        # Configuración del primer cuadro de texto
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(390, 180, 361, 41))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")

        # Configuración del segundo cuadro de texto
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(390, 330, 381, 41))
        self.lineEdit_2.setStyleSheet("")
        self.lineEdit_2.setObjectName("lineEdit_2")

        # Configuración del segundo botón
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(760, 180, 31, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(243, 90, 41);\n"
                                        "font: 12pt \"Gill Sans Ultra Bold\";\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")

        # Agregar widgets a la ventana principal
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Traducción de textos
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SONIFY"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Carga tu música aqui:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>El género de tu música es:</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Analizar"))
        self.pushButton_2.setText(_translate("MainWindow", "..."))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
