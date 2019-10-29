from random import random
from secrets import randbelow
import numpy as np


def module(x, b):
    return x - (int(x / b) * b)

def square(x):
    return int(x) % 2

def sawtooth(x):
    return module(x, 2)

def triangle(x):
    a = module(x, 1)
    b = square(x)
    c = (b * a) + (1 - b) * (1 - a)
    return c

def whiteNoise1(x):
    return random()

def whiteNoise2(x):
    detail = 1000.0
    a = randbelow(int(detail)) / detail
    return a

def harmonics(func, main_freq, harmonics_list, step):
    sum = 0
    for h in harmonics_list:
        sum += h[1] * func(h[0] * main_freq * step)
    return sum

def instrument1(main_freq, step):
    baseHarmonics = [
        (1, 1),
        (2, 0.8),
        (3, 0.5),
        (4, 0.5),
        (5, 0.9),
        (6, 0.3),
        (7, 0.3),
    ]
    
    harmonics_list = []

    for i in range(len(baseHarmonics)):
        harmonic_number, amplitude = baseHarmonics[i]
        amplitude *= push_instrument1(step)
        harmonics_list.append((harmonic_number,amplitude))
    return harmonics(np.sin, main_freq, harmonics_list, step)


def push_instrument1(step):
    if step <= 0:
        return 1
    else:
        b =  1 - np.log(step / 3000.0 + 1)
        if b > 0:
            return b
        else:
            return 0

def lol(freq, step):
    hrm = [
        (1, 1),
        (3, 0.5)
    ]
    return harmonics(np.sin, freq, hrm, step)
