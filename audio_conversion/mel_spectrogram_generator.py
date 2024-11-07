import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os
from audio_conversion.converter import load_audio_file


def generate_and_save_mel_spectrogram(audio_path, save_dir, genre_label, sr=22050, n_mels=128, fmax=8000):
    """
    Genera y guarda un espectrograma de Mel a partir de un archivo de audio.

    Parámetros:
        - audio_path: Ruta del archivo de audio.
        - save_dir: Carpeta raíz para guardar los espectrogramas.
        - genre_label: Nombre de la carpeta para el género de música.
        - sr: Frecuencia de muestreo.
        - n_mels: Número de bandas de Mel.
        - fmax: Frecuencia máxima a mostrar en el espectrograma.
    """
    # Cargar el archivo de audio
    y, sr = load_audio_file(audio_path, sr=sr)
    if y is None:
        return

    # Generar el espectrograma de Mel
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels, fmax=fmax)
    S_dB = librosa.power_to_db(S, ref=np.max)

    # Crear la ruta de guardado para el género
    genre_dir = os.path.join(save_dir, genre_label)
    os.makedirs(genre_dir, exist_ok=True)

    # Definir el nombre del archivo de salida
    file_name = os.path.join(genre_dir, os.path.basename(audio_path).replace('.wav', '.png'))

    # Guardar el espectrograma de Mel como imagen
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(S_dB, sr=sr, hop_length=512, x_axis='time', y_axis='mel')
    plt.colorbar(format='%+2.0f dB')
    plt.title(f'Mel spectrogram - {genre_label}')
    plt.tight_layout()
    plt.savefig(file_name)
    plt.close()

    print(f"Espectrograma guardado en {file_name}")
