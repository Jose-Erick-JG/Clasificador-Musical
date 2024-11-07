import os
from audio_conversion.mel_spectrogram_generator import generate_and_save_mel_spectrogram

# Directorio raíz de los archivos de audio
audio_base_dir = 'data/raw_audio'
# Directorio para guardar los espectrogramas
save_dir = 'data/spectrograms'
# Lista de géneros
genres = ['clasica', 'jazz', 'pop','rock']

# Crear espectrogramas para todos los géneros
for genre in genres:
    genre_audio_dir = os.path.join(audio_base_dir, genre)
    for audio_file in os.listdir(genre_audio_dir):
        if audio_file.endswith('.wav'):  # Verifica que sea un archivo de audio .wav
            audio_path = os.path.join(genre_audio_dir, audio_file)
            generate_and_save_mel_spectrogram(audio_path, save_dir, genre)
