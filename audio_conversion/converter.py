import librosa


def load_audio_file(audio_path, sr=22050):
    """
    Carga un archivo de audio y devuelve la señal de audio y la frecuencia de muestreo.

    Parámetros:
        - audio_path: Ruta del archivo de audio.
        - sr: Frecuencia de muestreo (22050 Hz por defecto).

    Retorna:
        - y: Señal de audio.
        - sr: Frecuencia de muestreo.
    """
    try:
        y, sr = librosa.load(audio_path, sr=sr)
        return y, sr
    except Exception as e:
        print(f"Error al cargar el archivo {audio_path}: {e}")
        return None, None
