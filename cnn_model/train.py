import os
import numpy as np
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator
from cnn_model.model import create_cnn_model

# Ruta a los espectrogramas
data_dir = 'dataset/spectrograms'

# Configuración del generador de datos
datagen = ImageDataGenerator(validation_split=0.2, rescale=1./255)
train_generator = datagen.flow_from_directory(
    data_dir,
    target_size=(128, 128),
    batch_size=32,
    class_mode='sparse',
    subset='training'
)
validation_generator = datagen.flow_from_directory(
    data_dir,
    target_size=(128, 128),
    batch_size=32,
    class_mode='sparse',
    subset='validation'
)

# Crear y entrenar el modelo
model = create_cnn_model(input_shape=(128, 128, 3), num_classes=len(train_generator.class_indices))
history = model.fit(train_generator, validation_data=validation_generator, epochs=10)

# Guardar el modelo entrenado
model.save('cnn_model/music_genre_classifier.h5')
