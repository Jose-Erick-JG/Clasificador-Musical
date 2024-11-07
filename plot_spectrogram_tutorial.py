# import soundfile as sf
# from pathlib import Path
# import librosa
# import numpy as np
# import matplotlib.pyplot as plt
#
# def plot_spectrogram_and_save(signal,sample_rate, output_path: Path):
#     stft = librosa.stft(signal)
#     spectrogram = np.abs(stft)
#     spectrogram_db = librosa.amplitude_to_db(spectrogram)
#
#     plt.figure(figsize=(10,4))
#     img = librosa.display.specshow(spectrogram_db,y_axis='log',x_axis='time',
#     sr=sample_rate, cmap='inferno')
#     plt.show()
#
#
# def main():
#     signal, sample_rate = sf.read(Path('data') / '')
#     print(f'Sample rate: {sample_rate}')
#     plot_spectrogram_and_save(signal,sample_rate, Path('img') / 'spectrogram.png')
#
# if __name__ == '__main__':
#     main()