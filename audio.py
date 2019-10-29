# used for editing wave files
import wave
# for basic mathematic operations
import numpy as np
# for using with wave functions
import struct
# generate functions for audio
import functions

# frequency is the number of times a wave repeats a second
frequency = 100
# The sampling rate of the analog to digital convert
sampling_rate = 48000.0
# file length in secounds
duration = 1 # secounds
# number of samples to generate
num_samples = int( sampling_rate * duration)
# amplitude of the audio
amplitude = 16000
# audio file to be saved into
file = "test.wav"

# conversions:
"""
returns 2 * pi * f * x / sr
2 * pi * f : convert f to w. time frequency to angular frequency.
x / sr : convert sample number to time
so it actually returns w * t
"""
# normalize
def norm(x):
    return 2 * np.pi * frequency * x / sampling_rate

# create a simple audio
audio_wave = [functions.lol(frequency, norm(x) / 1.0) for x in range(num_samples)]

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
   wav_file.writeframes(struct.pack('h', int(s*amplitude)))
