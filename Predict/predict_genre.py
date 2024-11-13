import tensorflow as tf
import numpy as np
import sys
from PIL import Image
import pickle
from audio_conversion.mel_spectrogram_generator import generate_and_save_mel_spectrogram

# Ruta al modelo entrenado y a los índices de clase
MODEL_PATH = 'C:/Users/Usuario/Documents/GitHub/Clasificador-Musical/cnn_model/cnn_music_genre_classifier.h5'
CLASS_INDICES_PATH = 'class_indices.pkl'

# Cargar el modelo
model = tf.keras.models.load_model(MODEL_PATH)

# Cargar los índices de clase
with open(CLASS_INDICES_PATH, 'rb') as f:
    class_indices = pickle.load(f)
class_indices_inv = {v: k for k, v in class_indices.items()}

# Función para preprocesar la imagen
def preprocess_image(image_path, target_size=(128, 128)):
    image = Image.open(image_path).convert('RGB')
    image = image.resize(target_size)
    image_array = np.array(image) / 255.0  # Normalización
    image_array = np.expand_dims(image_array, axis=0)  # Añadir dimensión batch
    return image_array

# Función principal de predicción
def predict_genre(audio_path):
    # Generar el espectrograma y guardar la imagen temporalmente
    temp_image_path = 'temp_spectrogram.png'
    generate_and_save_mel_spectrogram(audio_path, 'temp', '')

    # Preprocesar la imagen del espectrograma
    image_array = preprocess_image(temp_image_path)

    # Hacer la predicción
    predictions = model.predict(image_array)
    predicted_class = np.argmax(predictions)

    # Mapear la clase predicha al género correspondiente
    predicted_genre = class_indices_inv[predicted_class]

    print(f'El género de la canción es: {predicted_genre}')

# Ejecutar el script desde la línea de comandos
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Por favor, proporciona la ruta del archivo de audio.")
    else:
        audio_path = sys.argv[1]
        predict_genre(audio_path)
