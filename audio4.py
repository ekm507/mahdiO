import instruments
import music
import functions
from write import write_to_file
from read_midi import read_midi


notes = read_midi('1.mid')

print('generating audio')

audio_wave = music.create_music2(notes, instruments.instrument4, note_duration=1)

audio_wave = functions.audio_normalize(audio_wave, 1)

write_to_file(audio_wave, filename='lol.wav')