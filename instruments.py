# used for generationg harmonical waveforms
from functions import guard, harmonics
# used for basic mathematical operations
import math


# a simple music instrument, made using harmonics function.
# main frequency is the music note frequency to be played
def instrument1(main_freq, step):
    # harmonics lists (like fourier series)
    # each tuple is like:
    # (harmonic number, amplitude)
    harmonics_list = [
        (1, 0.2),
        (2, 1.0),
        (3, 0.39),
        (4, 0.2),
        (5, 0.05),
        (6, 0.02),
        (7, 0.01),
    ]
        

    # amplitude changes over time.
    amplitude = push_instrument1(step)
    # frequency changes over time.
    base_freq = frequency_instrument1(main_freq, step)

    # generate a sample for the audio
    return harmonics(math.sin, base_freq, harmonics_list, step) * amplitude

# amplitude per time function for instrument 1
# using this, played note gets faded during time
# TODO: algorithm should be changed
def push_instrument1(step):
    min_amp = 0
    max_amp = 0.4
    if step <= 0:
        return max_amp
    else:
        # b =  (1 - math.log(step / 2 + 1) )* abs((math.cos(step * 4) ))
        b = max_amp * math.exp(-step / 2) * abs(math.sin(step * 4) )
        return guard(b, min_amp, max_amp)

# frequency per time function for instrument 1
# frequency in this function decreases over time.
def frequency_instrument1(main_freq, step):
    return main_freq

def instrument2(main_freq, step):

    harmonics_list=[
        (1, 0.8),
        (2, 1),
        (3, 0.5),
        (4, 0.4), 
        (5, 0.3),
        (6, 0.6),
        (7, 0.1),
        (8, 0.05)
    ]

    amplitude = push_instrument2(step)
    return harmonics(math.sin, main_freq, harmonics_list, step) * amplitude

def push_instrument2(step):
    min_amp = 0
    max_amp = 0.4
    if step <=0:
        b = max_amp
    elif step <= math.pi:
        b = max_amp * math.cos(step / 2)
    else:
        b = 0
    return guard(b, min_amp, max_amp)


def instrument3(main_freq, step):

    harmonics_list = [
        (1, 0.2),
        (2, 0.8),
        (3, 0.5),
        (4, 0.1),
        (5, 0.05),
        (6, 0.02),
        (7, 0.01)
    ]

    amplitude = push_instrument3(step)
    return harmonics(math.sin, main_freq, harmonics_list, step) * amplitude


def push_instrument3(step):
    k = - step  / 4
    q = step * 2
    push = math.exp(k) * (1 + abs(math.cos(q)))
    return push * 0.3