from bark import SAMPLE_RATE, generate_audio
import numpy as np

def generate_audio(text: str, speaker: str):
    audio_array = generate_audio(text, speaker)
    audio_data = audio_array.astype(np.int16)
    return audio_data