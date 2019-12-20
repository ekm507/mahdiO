# used for editing wave files
import wave
# for basic mathematic operations
import numpy as np
# for using with wave functions
import struct
# generate instrument notes for audio
import instruments
# for creating music
import music

# frequency is the number of times a wave repeats a second
frequency = 349.23
# The sampling rate of the analog to digital convert
sampling_rate = 48000.0
# file length in secounds
duration = 0.268 + 0.3 # secounds
# number of samples to generate
num_samples = int( sampling_rate * duration)
# amplitude of the audio
amplitude = 16000
# audio file to be saved into
file = "test.wav"

# normalize
def norm(x):
    return  2 * np.pi *x / sampling_rate

# guard a number between infimum and suprimum
def guard(number, low, high):
    if number < low:
        return low
    elif number > high:
        return high
    else:
        return number

# create a note
# note is a tuple(note number, duration)
def create_note(note):
    number, duration = note
    main_freq = 110.00
    freq = main_freq * number
    num_samples = int( sampling_rate * duration)
    audio_wave = [instruments.instrument2(freq, norm(x)) for x in range(num_samples)]
    return audio_wave



def create_music(notes):
    note_duration = 4.0
    file_duration = 0
    for _, duration in notes:
        file_duration += duration
    file_duration += note_duration
    audio_wave = [0 for i in range(int(file_duration * sampling_rate))]
    note_frame = 0
    for number, duration in notes:
        note = create_note((number, note_duration))
        for i in range(len(note)):
            audio_wave[note_frame + i] += note[i]
        note_frame += int(duration * sampling_rate)

    return audio_wave

fullNote = 0.6 # seconds

notes1 = [
    (1, fullNote),
    (1, fullNote),
    (5, fullNote),
    (5, fullNote),
    (6, fullNote),
    (6, fullNote),
    (5, fullNote * 2),
    (4, fullNote),
    (4, fullNote),
    (3, fullNote), 
    (3, fullNote),
    (2, fullNote),
    (2, fullNote),
    (1, fullNote)
]

notes2 = [
    (71, fullNote),
    (75, fullNote),
    (78, fullNote),
    (77, fullNote)
]

notes3 = [
    (72, fullNote)
]

audio_wave3 = music.create_music(notes3, instruments.instrument1, sampling_rate)


# file properties
nframes=num_samples
comptype="NONE"
compname="not compressed"
nchannels=1
sampwidth=2

# open wave file
wav_file=wave.open(file, 'w')
# set properties
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

# write the audio to file
for s in audio_wave3:
    gs = guard(s, -1, 1)
    wav_file.writeframes(struct.pack('h', int(gs*amplitude)))

