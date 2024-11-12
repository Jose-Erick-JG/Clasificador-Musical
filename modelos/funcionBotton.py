# main.py
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtCore import QFileInfo
from main_windows import Ui_MainWindow  # Importa la interfaz generada

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Establece el lineEdit_2 como de solo lectura
        self.lineEdit_2.setReadOnly(True)

        # Conecta el botón de selección de archivos a la función `select_audio_file`
        self.pushButton_2.clicked.connect(self.select_audio_file)

    def select_audio_file(self):
        # Abre el cuadro de diálogo para seleccionar un archivo de audio
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Selecciona un archivo de audio",  # Título de la ventana de diálogo
            "",  # Directorio de inicio (vacío para iniciar en el directorio actual)
            "Audio Files (*.mp3 *.wav *.ogg)"  # Filtro de archivos
        )

        # Si el usuario selecciona un archivo, obtiene solo el nombre del archivo
        if file_path:
            file_info = QFileInfo(file_path)  # Crea un objeto QFileInfo con la ruta
            file_name = file_info.fileName()  # Obtiene solo el nombre del archivo
            self.lineEdit.setText(file_name)  # Muestra solo el nombre en el campo de texto

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())