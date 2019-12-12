# used for editing wave files
import wave
# for basic mathematic operations
import numpy as np
# for using with wave functions
import struct
# generate functions for audio
import functions
# music instruments used
import instruments

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

# conversions:
"""
returns x / sr

x / sr : convert sample number to time
so it actually returns t
"""
# normalize
def norm(x):
    return  2 * np.pi *x / sampling_rate

# create a simple audio
# audio_wave1 = [functions.instrument1(frequency, norm(x)) for x in range(num_samples)]
#audio_wave2 = [functions.instrument_sin(frequency * 2, norm(x)) for x in range(num_samples * 4)]


def create_music(notes):
    audio_wave = []
    main_freq = 110.00 # A2
    for note, duration in notes:
        num_samples = int( sampling_rate * duration)
        audio_wave.append( [instruments.instrument1(main_freq * note, norm(x)) for x in range(num_samples)] )
    return audio_wave

fullNote = 0.3 # seconds

notes = [
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

audio_wave3 = create_music(notes)
audio_wave4 = []
for i in audio_wave3:
    audio_wave4 += i


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
for s in audio_wave4:
   wav_file.writeframes(struct.pack('h', int(s*amplitude)))
