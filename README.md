# python audio

Generate sound effects using mathematics

files in this repo include:

* `functions.py` for generating basic audio functions.
* `notes.py` for generating notes.
* `midi_conversions.py` for converting note number to frequency.
* `instruments.py` for describing each instrument.
* `music.py` for generating music.
* `write.py` for writing generated audio into a wave file
* `read_midi.py` for reading notes data from `.mid` files
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
1. different tracks in midi file, each have their own instrument. add a support for this

2. get timing info from midi file

3. write better instruments.

4. make documentation for code. maybe rewrite this README file too.

5. make a wiki for developers so it will be easier to develope.
