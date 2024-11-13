import tensorflow as tf
from keras import layers, models

def create_cnn_model(input_shape=(128, 128, 3), num_classes=3):
    """
    Crea un modelo de red neuronal convolucional (CNN) para la clasificación de espectrogramas.

    Parámetros:
        - input_shape: Dimensiones de entrada de las imágenes (espectrogramas).
        - num_classes: Número de clases de salida (géneros de música).

    Retorna:
        - Un modelo de CNN compilado.
    """
    model = models.Sequential()

    # Primera capa convolucional
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(layers.MaxPooling2D((2, 2)))

    # Segunda capa convolucional
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))

    # Tercera capa convolucional
    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))

    # Cuarta capa convolucional
    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))

    # Aplanamiento para las capas densas
    model.add(layers.Flatten())

    # Capa completamente conectada (densa)
    model.add(layers.Dense(512, activation='relu'))

    # Capa de salida con 'num_classes' salidas
    #Genera posibilidades de pertenencia a cada clase!
    model.add(layers.Dense(num_classes, activation='softmax'))

    # Compilación del modelo
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model
