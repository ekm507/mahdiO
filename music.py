import notes
from midi_conversions import midi2freq
from midi_conversions import any2freq

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
        noteByFrequency.append((midi2freq(number), duration))

    for frequency, duration in noteByFrequency:
        note = notes.create_note((frequency, note_duration), instrument, sampling_rate)
        for i in range(len(note)):
            audio_wave[note_frame + i] += note[i]
        note_frame += int(duration * sampling_rate)

    return audio_wave


# create music function compatible with another standard for notes list.
#TODO: document this file

def create_music2(notes_list, instrument, sampling_rate=48000, note_duration=4.0, note_type='midi'):
    
    # how long music will be
    file_duration = max(list(k[1] for k in notes_list)) + note_duration

    # generate a list as long as needed for music.
    audio_wave = [0 for _ in range(int(file_duration * sampling_rate))]

    # a set of notes by frequency (not midi or string)
    notesSet = set(k[0] for k in notes_list)

    # generate notes files
    noteFiles = {
        k:
        notes.create_note(
            tuple(
                any2freq(k, note_type),
                note_duration
            ),
            instrument,
            sampling_rate)
    for k in notesSet
    } # what a messy line of code it was!

    # now that notes are generated, we are to mix them.

