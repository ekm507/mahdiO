import functions

def create_note(note, instrument, sampling_rate):
    frequency, duration = note
    num_samples = int( sampling_rate * duration)
    audio_wave = [instrument(frequency, functions.pi_norm(x, sampling_rate)) for x in range(num_samples)]
    return audio_wave
