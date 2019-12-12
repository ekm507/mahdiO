# generate music notes ( and some more options)
"""
Written by an engineer who is curious about audio.
Erfan Kheyrollahi Qaroglu. I don't know how to music!
"""
# music is mathematics!
import math

# floating point modulo operation
"""
same as fmod function in C++ STL
Given two floating-point numbers, this finds the remainder (module).
for more info visit wiki page: https://en.wikipedia.org/wiki/Modulo_operation
x mod b
"""
def module(x, b):
    return x - (int(x / b) * b)


# works like sin function but gives a squarewave.
def square(x):
    # mirror x on [0 - 2*pi] period
    a = module(x, 2 * math.pi)
    if a < math.pi:
        return 1
    else:
        return -1

# normalizes a number from any range to range (-1, 1)
def norm(x, low, high):
    return 2 * x / math.fabs(high - low) - 1

# works like sin function but gives a sawtooth.
def sawtooth(x):
    # mirror x on [0 - 2*pi] period
    res = module(x, 2 * math.pi) 
    return norm(res, 0, 2 * math.pi)

# works like sin function but gives a triangle.
def triangle(x):
    # mirror x on [0 - 2*pi] period
    a = module(x, 2 * math.pi)
    # normalize a
    a = norm(a, 0, 2 * math.pi)
    # generate triangular wave
    a = math.fabs(a)
    # normalize a
    return norm(a, 0, 1)


# generate harmonics for a waveform
"""
this gets 4 paramethers.
func: the function to generate harmonics using it. use sin for typical mode.
func should work like sin function.
main_freq: main wave frequency. (first harmonic frequency)
harmonics_list: a list of requested harmonics numbers and their amplitude
step: the variable. like time.
"""
def harmonics(func, main_freq, harmonics_list, step):
    # a moment of sound
    sum = 0
    # add all harmonics
    for h in harmonics_list:
        # TODO: do h with namedTuple
        # h[0] = harmonic number, h[1] = harmonic amplitude.
        sum += h[1] * func(h[0] * main_freq * step)
    return sum

