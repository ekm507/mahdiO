# used for editing wave files
import wave
# for basic mathematic operations
import math
# for using with wave functions
import struct
# generate instrument notes for audio
import instruments
# for creating music
import music
# mathematical functions 
import functions

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

notes = [
    (71, 0),
    (72, 0.5),
    (75, 1),
    (78, 1.5),
    (77, 2.5),
    (76, 3),
    (75, 3.5),
    (74, 4)
]

audio_wave = music.create_music2(notes, instruments.instrument1)


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
for s in audio_wave:
    gs = functions.guard(s, -1, 1)
    wav_file.writeframes(struct.pack('h', int(gs*amplitude)))

