# for creating noise
from random import random
# for creating noise
from secrets import randbelow
# for simple mathematics operations
import numpy as np

# floating point modulo operation
"""
same as fmod function in C++ STL
Given two floating-point numbers, this finds the remainder (module).
for more info visit wiki page: https://en.wikipedia.org/wiki/Modulo_operation
"""
def module(x, b):
    return x - (int(x / b) * b)

# works like sin function but gives a squarewave.
def square(x):
    # mirror x on [0 - 2*pi] period
    a = module(x, 2 * np.pi)
    if a < np.pi:
        return 1
    else:
        return -1

# works like sin function but gives a sawtooth.
def sawtooth(x):
    # mirror x on [0 - 2*pi] period
    return module(x, 2 * np.pi)

# works like sin function but gives a triangle.
def triangle(x):
    # mirror x on [0 - 2*pi] period
    a = module(x, 2 * np.pi)
    # normalize a
    a /= np.pi
    if a < 1:
        return a - 0.5
    else:
        return 1.5 - a

# generate white noise using random.random function
def whiteNoise1(x):
    return random()

# generate white noise using secrets lib random.
def whiteNoise2(x):
    # amplitude detail
    detail = 1000.0
    return randbelow(int(detail)) / detail

# guard a number between infimum and suprimum
def guard(number, low, high):
    if number < low:
        return low
    elif number > high:
        return high
    else:
        return number


# normalize
def pi_norm(x, max_x):
    return  2 * np.pi *x / max_x


# generate harmonics for a waveform
"""
this gets 4 paramethers.
func: the function to generate harmonics using it. use sin for typical mode
main_freq: main wave frequency. (first harmonic frequency)
harmonics_list: a list of requested harmonics numbers and their amplitude
step: the variable. like time.
"""
def harmonics(func, main_freq, harmonics_list, step):
    sum = 0
    for h in harmonics_list:
        sum += h[1] * func(h[0] * main_freq * step)
    return sum


def instrument_sin(freq, step):
    h = [
        (1, 1)
    ]

    a = 1

    return a * harmonics(square, freq, h, step)
