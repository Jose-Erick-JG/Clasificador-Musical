import numpy as np
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator
from cnn_model.model import create_cnn_model
import os
import pickle  # Importa pickle para guardar el mapeo de clases



def train_model(data_dir, input_shape=(128, 128, 3), batch_size=32, epochs=10):
    """
    Entrena el modelo de CNN usando los espectrogramas de los géneros musicales.

    Parámetros:
        - d ata_dir: Directorio donde están los espectrogramas por género.
        - input_shape: Dimensiones de las imágenes de entrada.
        - batch_size: Tamaño del lote para el entrenamiento.
        - epochs: Número de épocas para entrenar el modelo.
    """
    # Generador de datos para cargar las imágenes desde carpetas
    datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)  # Normaliza los píxeles

    # Carga de datos de entrenamiento
    train_generator = datagen.flow_from_directory(
        data_dir,
        target_size=(input_shape[0], input_shape[1]),
        batch_size=batch_size,
        class_mode='categorical',
        subset='training'
    )

    # Guardar los índices de las clases
    with open('class_indices.pkl', 'wb') as f:
        pickle.dump(train_generator.class_indices, f)
    print("Archivo class_indices.pkl generado con éxito.")

    # Carga de datos de validación
    validation_generator = datagen.flow_from_directory(
        data_dir,
        target_size=(input_shape[0], input_shape[1]),
        batch_size=batch_size,
        class_mode='categorical',
        subset='validation'
    )

    # Crear el modelo de CNN
    model = create_cnn_model(input_shape=input_shape, num_classes=len(train_generator.class_indices))

    # Entrenamiento del modelo
    model.fit(
        train_generator,
        epochs=epochs,
        validation_data=validation_generator
    )

    # Guardar el modelo entrenado
    model.save('cnn_music_genre_classifier.h5')

if __name__ == "__main__":
    base_dir = 'C:\\Users\\Usuario\\Documents\\GitHub\\Clasificador-Musical'
    data_dir = os.path.join(base_dir, 'dataset', 'spectrograms')

    # Verificación de la ruta
    if not os.path.exists(data_dir):
        print(f"El directorio {data_dir} no existe.")
    else:
        print(f"El directorio {data_dir} existe.")
        # Entrenar el modelo
        train_model(data_dir=data_dir)
