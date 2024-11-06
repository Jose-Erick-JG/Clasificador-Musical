import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox
from audio_conversion.converter import batch_convert_audio

class AudioConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Audio Converter")
        self.setGeometry(100, 100, 400, 300)

        # Variables
        self.input_folder = ""
        self.output_folder = ""
        self.target_sr = 22050  # Default sample rate

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Carpeta de entrada
        self.input_label = QLabel("Input Folder:")
        self.input_entry = QLineEdit(self)
        self.input_button = QPushButton("Select Input Folder", self)
        self.input_button.clicked.connect(self.select_input_folder)
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_entry)
        layout.addWidget(self.input_button)

        # Carpeta de salida
        self.output_label = QLabel("Output Folder:")
        self.output_entry = QLineEdit(self)
        self.output_button = QPushButton("Select Output Folder", self)
        self.output_button.clicked.connect(self.select_output_folder)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_entry)
        layout.addWidget(self.output_button)

        # Frecuencia de muestreo
        self.sample_rate_label = QLabel("Sample Rate:")
        self.sample_rate_entry = QLineEdit(self)
        self.sample_rate_entry.setText("22050")
        layout.addWidget(self.sample_rate_label)
        layout.addWidget(self.sample_rate_entry)

        # Botón de conversión
        self.convert_button = QPushButton("Convert Audio", self)
        self.convert_button.clicked.connect(self.convert_audio)
        layout.addWidget(self.convert_button)

        # Configurar el layout
        self.setLayout(layout)

    def select_input_folder(self):
        folder_selected = QFileDialog.getExistingDirectory(self, "Select Input Folder")
        if folder_selected:
            self.input_folder = folder_selected
            self.input_entry.setText(self.input_folder)

    def select_output_folder(self):
        folder_selected = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if folder_selected:
            self.output_folder = folder_selected
            self.output_entry.setText(self.output_folder)

    def convert_audio(self):
        try:
            self.target_sr = int(self.sample_rate_entry.text())
            if not self.input_folder or not self.output_folder:
                raise ValueError("Please select both input and output folders.")

            batch_convert_audio(self.input_folder, self.output_folder, self.target_sr)
            QMessageBox.information(self, "Success", "Audio conversion completed successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AudioConverterApp()
    window.show()
    sys.exit(app.exec_())
