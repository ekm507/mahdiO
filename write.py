import wave
import functions
import struct

def write_to_file(audio_wave:list, filename:str='test.wav', sampling_rate:int=48000, amplitude:float=32000):
    
    # open a file for writing audio in
    wav_file = wave.open(filename, 'w')

    # file properties
    nframes=len(audio_wave)
    comptype="NONE"
    compname="not compressed"
    nchannels=1
    sampwidth=2

    # set properties
    wav_file.setparams((nchannels, sampwidth, sampling_rate, nframes, comptype, compname))

    print('writing to disk')

    # convert list to bytearray so it is writeable on disk
    writable_audio = bytearray()
    for s in audio_wave:
        gs = functions.guard(s, -1, 1)
        writable_audio += struct.pack('h', int(gs*amplitude))

    # write audio into file
    wav_file.writeframes(writable_audio)

