import notes
from midi_conversions import midi2freq

def create_music(notes_list, instrument, sampling_rate):
    note_duration = 4.0
    file_duration = 0
    for n, duration in notes_list:
        file_duration += duration
    file_duration += note_duration
    audio_wave = [0 for i in range(int(file_duration * sampling_rate))]
    note_frame = 0
    noteByFrequency = []
    for number, duration in notes_list:
        noteByFrequency.append(tuple(midi2freq(number), duration))

    for frequency, duration in noteByFrequency:
        note = notes.create_note((frequency, note_duration), instrument, sampling_rate)
        for i in range(len(note)):
            audio_wave[note_frame + i] += note[i]
        note_frame += int(duration * sampling_rate)

    return audio_wave
