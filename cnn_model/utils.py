import os
from tensorflow.keras.preprocessing.image import load_img, img_to_array

def load_image(image_path, target_size=(128, 128)):
    """
    Carga una imagen y la convierte a un array adecuado para la CNN.
    """
    img = load_img(image_path, target_size=target_size)
    img_array = img_to_array(img)
    img_array = img_array / 255.0  # Normalizar los valores de la imagen
    return img_array
