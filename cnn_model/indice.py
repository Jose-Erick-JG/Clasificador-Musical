import pickle

# Cargar el archivo `class_indices.pkl`/

# Comprobación rápida de class_indices.pkl
with open('class_indices.pkl', 'rb') as f:
    class_indices = pickle.load(f)
print("Mapeo de clases:", class_indices)
