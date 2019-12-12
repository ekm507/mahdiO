import notes


def create_music(notes_list, instrument, sampling_rate):
    note_duration = 4.0
    file_duration = 0
    for n, duration in notes_list:
        file_duration += duration
    file_duration += note_duration
    audio_wave = [0 for i in range(int(file_duration * sampling_rate))]
    note_frame = 0
    for number, duration in notes_list:
        note = notes.create_note((number, note_duration), instrument, sampling_rate)
        for i in range(len(note)):
            audio_wave[note_frame + i] += note[i]
        note_frame += int(duration * sampling_rate)

    return audio_wave
