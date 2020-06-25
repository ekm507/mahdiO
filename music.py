import notes
from midi_conversions import midi2freq
from midi_conversions import any2freq
import sys

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
            (
                any2freq(k, note_type),
                note_duration
            ),
            instrument,
            sampling_rate)
    for k in notesSet
    } # what a messy line of code it was!

    # now that notes are generated, we are to mix them.
    for note, time in notes_list:
        for i in range(int(note_duration * sampling_rate)):
            audio_wave[i + int (time * sampling_rate)] += noteFiles[note][i]
    
    return audio_wave

# this should do with new version of notes only.
"""
    note version 2 is a list of tuples. each element of tuple is like this:
    (note number, note start time, note duration, note velocity)

    note number: usually midi number of note, but can also be frequency in float or note name in string)
    note start time: this can be relative or independant timing.
    note duration: how long a note should be present despite what amplitude envelope function it uses.
    note velocity: amplitude of a note. how hard a note is being played
"""
def create_music3(notes_list, instrument, sampling_rate:float=48000, note_type:str='midi', time_type='relative'): # for notes list version3
    
    max_note_duration = max(list(k[2] for k in notes_list))
    
    # how long music will be
    if time_type == 'relative':
        note_duration = max(list(k[1] for k in notes_list))
        file_duration = sum(list(k[1] for k in notes_list)) + note_duration
    elif time_type == 'independant':
        file_duration = max(list(k[1] for k in notes_list)) + max_note_duration

    print('allocating music file on ram')
    print(file_duration * sampling_rate)
    # generate a list as long as needed for music.
    audio_wave = [0] * int(file_duration * sampling_rate)

    # a set of notes by frequency (not midi or string)
    notesSet = set(k[0] for k in notes_list)

    print('generating notes')

    # generate notes files
    noteFiles = dict()
    q = len(notesSet)
    for k in notesSet:
        #print('\x1b[3D\x1b[1A')
        sys.stdout.write(repr(q))
        sys.stdout.write('    ')
        sys.stdout.write('\n')
        sys.stdout.write('\x1b[3D\x1b[1A')
        q -= 1
        noteFiles[k] = notes.create_note(
            (
                any2freq(k, note_type=note_type),
                max_note_duration
            ),
            instrument,
            sampling_rate
        )


    print('syntesising music')
    k = 0
    # now that notes are generated, we are to mix them.
    if time_type == 'independant':
        for note, time, duration, velocity in notes_list:
            k += 1
            #print('\x1b[3D\x1b[1A')
            sys.stdout.write(repr(k))
            sys.stdout.write('\n')
            sys.stdout.write('\x1b[3D\x1b[1A')
            for i in range(int(duration * sampling_rate)):
                try:
                    audio_wave[i + int (time * sampling_rate)] += noteFiles[note][i] * velocity
                except IndexError:
                    print('index to write:')
                    print(i + int (time * sampling_rate))
                    print('index to read:')
                    print(i)

    elif time_type == 'relative':
        last_time = 0

        for note, time, duration, velocity in notes_list:
            k += 1
            #print('\x1b[3D\x1b[1A')
            sys.stdout.write(repr(k))
            sys.stdout.write('\n')
            sys.stdout.write('\x1b[3D\x1b[1A')
            last_time += time
            for i in range(int(duration * sampling_rate)):
                audio_wave[i + int(last_time * sampling_rate)] += noteFiles[note][i] * velocity
    
    return audio_wave

