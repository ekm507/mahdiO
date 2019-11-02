"""
This code is copied from:
https://pythonhosted.org/audiolazy/
exact source:
https://pythonhosted.org/audiolazy/_modules/audiolazy/lazy_midi.html
Note that some modifications might be here.
"""

# -*- coding: utf-8 -*-
# This file is part of AudioLazy, the signal processing Python package.
# Copyright (C) 2012-2016 Danilo de Jesus da Silva Bellini
#
# AudioLazy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
MIDI representation data & note-frequency relationship
"""

import itertools as it
import math

__all__ = [
    "MIDI_A4", "FREQ_A4", "SEMITONE_RATIO", "str2freq",
    "str2midi", "freq2str", "freq2midi", "midi2freq", "midi2str",
    "octaves"
]

# Useful constants
MIDI_A4 = 69   # MIDI Pitch number
FREQ_A4 = 440. # Hz
SEMITONE_RATIO = 2. ** (1. / 12.) # Ascending

def midi2freq(midi_number):
  """
  Given a MIDI pitch number, returns its frequency in Hz.
  """
  return FREQ_A4 * 2 ** ((midi_number - MIDI_A4) * (1./12.))

def str2midi(note_string):
  """
  Given a note string name (e.g. "Bb4"), returns its MIDI pitch number.
  """
  data = note_string.strip().lower()
  name2delta = {"c": -9, "d": -7, "e": -5, "f": -4, "g": -2, "a": 0, "b": 2}
  accident2delta = {"b": -1, "#": 1, "x": 2}
  accidents = list(it.takewhile(lambda el: el in accident2delta, data[1:]))
  octave_delta = int(data[len(accidents) + 1:]) - 4
  return (MIDI_A4 +
          name2delta[data[0]] + # Name
          sum(accident2delta[ac] for ac in accidents) + # Accident
          12 * octave_delta # Octave
         )

def str2freq(note_string):
  """
  Given a note string name (e.g. "F#2"), returns its frequency in Hz.
  """
  return midi2freq(str2midi(note_string))

def freq2midi(freq):
  """
  Given a frequency in Hz, returns its MIDI pitch number.
  """
  result = 12 * (math.log2(freq) - math.log2(FREQ_A4)) + MIDI_A4
  return result

def midi2str(midi_number, sharp=True):
  """
  Given a MIDI pitch number, returns its note string name (e.g. "C3").
  """
  num = midi_number - (MIDI_A4 - 4 * 12 - 9)
  note = (num + .5) % 12 - .5
  rnote = int(round(note))
  error = note - rnote
  octave = str(int(round((num - note) / 12.)))
  if sharp:
    names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
  else:
    names = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
  names = names[rnote] + octave
  if abs(error) < 1e-4:
    return names
  else:
    err_sig = "+" if error > 0 else "-"
    err_str = err_sig + str(round(100 * abs(error), 2)) + "%"
    return names + err_str

def freq2str(freq):
  """
  Given a frequency in Hz, returns its note string name (e.g. "D7").
  """
  return midi2str(freq2midi(freq))

def octaves(freq, fmin=20., fmax=2e4):
  """
  Given a frequency and a frequency range, returns all frequencies in that
  range that is an integer number of octaves related to the given frequency.

  Parameters
  ----------
  freq :
    Frequency, in any (linear) unit.
  fmin, fmax :
    Frequency range, in the same unit of ``freq``. Defaults to 20.0 and
    20,000.0, respectively.

  Returns
  -------
  A list of frequencies, in the same unit of ``freq`` and in ascending order.

  Examples
  --------
  >>> octaves(440.)
  [27.5, 55.0, 110.0, 220.0, 440.0, 880.0, 1760.0, 3520.0, 7040.0, 14080.0]
  >>> octaves(440., fmin=3000)
  [3520.0, 7040.0, 14080.0]
  """
  # Input validation
  if any(f <= 0 for f in (freq, fmin, fmax)):
    raise ValueError("Frequencies have to be positive")

  # If freq is out of range, avoid range extension
  while freq < fmin:
    freq *= 2
  while freq > fmax:
    freq /= 2
  if freq < fmin: # Gone back and forth
    return []

  # Finds the range for a valid input
  return list(it.takewhile(lambda x: x > fmin,
                           (freq * 2 ** harm for harm in it.count(0, -1))
                          ))[::-1] \
       + list(it.takewhile(lambda x: x < fmax,
                           (freq * 2 ** harm for harm in it.count(1))
                          ))
