import functions

def create_note(note, instrument, sampling_rate):
    number, duration = note
    main_freq = 110.00
    freq = main_freq * number
    num_samples = int( sampling_rate * duration)
    audio_wave = [instrument(freq, functions.pi_norm(x, sampling_rate)) for x in range(num_samples)]
    return audio_wave
