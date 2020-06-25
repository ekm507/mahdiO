import instruments
import music
import functions
from write import write_to_file

notes = [
    (71, 0),
    (72, 0.5),
    (75, 1),
    (78, 1.5),
    (77, 2.5),
    (76, 3),
    (75, 3.5),
    (74, 4),
    (75, 5),
    (74, 5.5),
]

print('generating audio')

audio_wave = music.create_music2(notes, instruments.instrument4, note_duration=1)

audio_wave = functions.audio_normalize(audio_wave, 1)

write_to_file(audio_wave, filename='lol.wav')