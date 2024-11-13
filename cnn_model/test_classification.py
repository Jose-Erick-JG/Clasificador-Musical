import os
import pickle
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from keras._tf_keras.keras.models import load_model
from audio_conversion.converter import load_audio_file
#from mel_spectrogram_generator import generate_and_save_mel_spectrogram
from utils import load_image

def generate_mel_spectrogram_for_prediction(audio_path, target_size=(128, 128)):
    """
    Genera un espectrograma de Mel a partir de un archivo de audio y lo devuelve en formato adecuado para la predicción.
    """
    # Cargar el archivo de audio
    y, sr = load_audio_file(audio_path)
    if y is None:
        return None

    # Generar el espectrograma de Mel
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
    S_dB = librosa.power_to_db(S, ref=np.max)

    # Guardar el espectrograma en una imagen temporal
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(S_dB, sr=sr, hop_length=512, x_axis='time', y_axis='mel')
    plt.axis('off')  # Eliminar ejes
    plt.savefig("temp_mel_spectrogram.png", bbox_inches='tight', pad_inches=0)
    plt.close()

    # Cargar la imagen y prepararla para el modelo
    img_array = load_image("temp_mel_spectrogram.png", target_size=target_size)
    os.remove("temp_mel_spectrogram.png")  # Eliminar imagen temporal
    return np.expand_dims(img_array, axis=0)  # Expande dimensiones para la entrada del modelo

def predict_genre(audio_path, model, class_indices):
    """
    Predice el género de una música dada.
    """
    # Generar espectrograma de Mel para la predicción
    mel_spectrogram = generate_mel_spectrogram_for_prediction(audio_path)
    if mel_spectrogram is None:
        print("Error al generar el espectrograma de Mel.")
        return

    # Realizar predicción
    predictions = model.predict(mel_spectrogram)
    predicted_class = np.argmax(predictions)

    # Obtener el mapeo inverso de índices a géneros
    index_to_genre = {v: k for k, v in class_indices.items()}
    predicted_genre = index_to_genre.get(predicted_class, "Desconocido")

    print(f"Predicción: {predicted_genre}")

if __name__ == "__main__":
    # Ruta al archivo de audio para probar
    audio_path = "C:\\Users\\HP\\Documents\\ARCHIVOS_MAYCOL\\IA\\classical.00003.wav"

    # Cargar el modelo
    model = load_model("cnn_music_genre_classifier.h5")

    # Cargar el mapeo de clases
    with open('class_indices.pkl', 'rb') as f:
        class_indices = pickle.load(f)

    # Realizar la predicción
    predict_genre(audio_path, model, class_indices)
