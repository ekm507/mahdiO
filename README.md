# python audio

In this branch (`pressure`) we are to add pressure function support for project.

Generate sound effects using mathematics

files in this repo include:

* `functions.py` for generating basic audio functions.
* `notes.py` for generating notes.
* `midi_conversions.py` for converting note number to frequency.
* `instruments.py` for describing each instrument.
* `music.py` for generating music.
* `audio*.py` for test.

## how it works

any note we hear is consisted of a sine function with a main frequency summed up with it's harmonics- each with it's own amplitude.  
adding up sine functions, we create a new function for each instrument which is it's basic sound. see `harmonics` function in `functions.py`.

but this is not enough by itself to make a nice sound.  
amplitude of a sound changes dampingly over time. this is also a unique property of an instrument.
see `instrument*` and `push_instrument*` functions in `instruments.py`.

different notes have different frequencies. harmonics change respecting to main frequency. see `notes.py` to learn more.

combining notes by synthesizing them, we create a music. each note has a duration and a note number. look up `music.py` to see how it works.

now we are ready to generate a music from zero!  
look up `audio*.py` to see how a list of notes by time and some more details can make a nice music!  
finally we should save generated audio wave into a .wav (wave) file. when done, it's done!

## TODO

1. create a plain function for simply saving audio as wav files.
2. add key pressure function support for instruments.
3. using threshold of hearing function, help creating better musics.
