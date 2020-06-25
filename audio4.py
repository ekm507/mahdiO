import instruments
import music
import functions
from write import write_to_file
from read_midi import read_midi
import sys


filename = sys.argv[1]

notes = read_midi(filename)

#notes = [(76, 0)]

print('generating audio')
note_duration = notes[1][1] - notes[0][1]
audio_wave = music.create_music3(notes, instruments.instrument2, time_type='independant')

audio_wave = functions.audio_normalize(audio_wave, 1)

write_to_file(audio_wave, filename='lol.wav')