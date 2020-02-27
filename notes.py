# used for mapping step to phase.
import functions

# this function gets instrument and note informations and
# generates a list worth of note.
def create_note(note, instrument, sampling_rate):

    # calculate size of list needed to store note in
    num_samples = int( sampling_rate * duration)

    # check if instrument is to be called with a pressure function
    # if a pressure function exists in note:
    if len(note) > 2:     
        # unpack note info
        frequency, duration, pressure = note
        # generate a list worth of note. as big as num_samples.
        # call instrument with a pressure function.
        audio_wave = [instrument(frequency, functions.pi_norm(x, sampling_rate), pressure=pressure) for x in range(num_samples)]
    # if pressure function is not needed:
    else:
        # unpack note info
        frequency, duration = note
        # generate a list worth of note. as big as num_samples.
        # call instrument without setting a pressure function.
        audio_wave = [instrument(frequency, functions.pi_norm(x, sampling_rate)) for x in range(num_samples)]
    # return the generated note.
    return audio_wave
