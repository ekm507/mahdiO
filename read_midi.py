import mido

def read_midi(filename:str) -> list:
    midiFile = mido.MidiFile(filename)
    tempoRate = 1
    tickTime = 1
    time_scale = midiFile.ticks_per_beat * tempoRate
    tempo = 500000 # default tempo
    time_scale = mido.tick2second(1, midiFile.ticks_per_beat , tempo)

    notes_temp = dict()
    notes = []

    for track in midiFile.tracks:
        time = 0
        for note in track:
            if note.type in ['note_on', 'note_off']:
                #TODO: get true time scale from midi file data
                time += note.time * time_scale
            if note.type == 'note_on':
                notes_temp[note.note] = (time, note.velocity)
            elif note.type == 'note_off':
                try:
                    noteNumber = note.note
                    startTime, velocity = notes_temp.pop(noteNumber)
                    noteDuration = time - startTime
                    notes.append( (noteNumber, startTime, noteDuration, velocity) )
                except KeyError:
                    pass
            elif note.type == 'set_tempo':
                tempo = note.tempo
                time_scale = mido.tick2second(tickTime, midiFile.ticks_per_beat , tempo)
            # else:
            #     print(note) # for debugging and deveeloping

    return notes
